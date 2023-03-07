from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
#from fake_useragent import UserAgent
from random import randrange
from datetime import datetime
import time
from bs4 import BeautifulSoup
import json
import html
from urllib.parse import quote_plus

webpage_directory = "www.classcentral.com/"
original_index_path = webpage_directory + f"original_index.html"
json_path = webpage_directory + f"index.json"
index_path = webpage_directory + f"index.html"


# ua = UserAgent()
# userAgent = ua.random
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)s Chrome/92.0.4515.131 Safari/537.36"
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={userAgent}")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

# translator
def translate_term(text, target_lang, source_lang="en"):
    translation = 'N/A'

    try:
        browser.get(f"https://translate.google.com/?sl={source_lang}&tl={target_lang}&text={text}&op=translate")
        condition = EC.presence_of_element_located((By.XPATH, f'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span'))
        element = WebDriverWait(browser, 10).until(condition)
        translation = element.text
        time.sleep(randrange(2))
    except Exception as err:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(err, "Something went wrong at: ", current_time)

    return translation


# to json
with open(original_index_path) as fp:
    soup = BeautifulSoup(fp, 'html.parser')

def parse_element(element):
    json_element = {}
    json_element['tag'] = element.name
    if element.attrs:
        json_element['attrs'] = element.attrs
    if element.string:
        json_element['text'] = element.string.strip()
    if element.contents:
        json_element['children'] = [parse_element(child) for child in element.contents if child.name is not None]
    return json_element

json_data = parse_element(soup)

with open(json_path, 'w') as f:
    f.write(json.dumps(json_data, indent=4))

#translate json
with open(json_path, 'r') as f:
    json_data = json.load(f)

# add translated text to json
def translate_text(json_data):
    if isinstance(json_data, dict):
        if 'tag' in json_data:
            if json_data['tag'] in ['script', 'style']:
                return  # ignore text in script and style tags
            if 'text' in json_data:
                json_data['text'] = translate_term(json_data['text'], "hi")
            if 'children' in json_data:
                for child in json_data['children']:
                    translate_text(child)
        else:
            for key in json_data:
                translate_text(json_data[key])
    elif isinstance(json_data, list):
        for item in json_data:
            translate_text(item)

translate_text(json_data)
with open(json_path, 'w') as f:
    json.dump(json_data, f, indent=4)

# to html
with open(json_path, 'r') as f:
    json_data = json.load(f)

def json_to_html(json_data):
    if isinstance(json_data, dict):
        tag_name = json_data.get('tag', '')
        tag_text = json_data.get('text', '')
        tag_attrs = ''
        if 'attrs' in json_data:
            attrs = json_data['attrs']
            attrs_strs = []
            for k, v in attrs.items():
                if isinstance(v, list):
                    v = ' '.join(v)
                # Escape special characters in attribute values
                v = html.escape(str(v))
                attrs_strs.append(f'{k}="{v}"')
            tag_attrs = ' '.join(attrs_strs)
        if tag_name:
            opening_tag = f'<{tag_name} {tag_attrs}>'
            closing_tag = f'</{tag_name}>'
            children = ''.join([json_to_html(child) for child in json_data.get('children', [])])
            # Skip escaping tag text if the tag is either "script" or "style"
            if tag_name.lower() in ['script', 'style']:
                return f'{opening_tag}{tag_text}{children}{closing_tag}'
            else:
                # Escape special characters in tag text
                tag_text = html.escape(str(tag_text))
                return f'{opening_tag}{tag_text}{children}{closing_tag}'
        else:
            # Escape special characters in tag text
            tag_text = html.escape(str(tag_text))
            return tag_text
    elif isinstance(json_data, list):
        return ''.join([json_to_html(item) for item in json_data])
    else:
        # Escape special characters in tag text
        return html.escape(str(json_data))


html = json_to_html(json_data)
html = html.replace('<[document] >', '').replace('</[document]>', '')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(html)



