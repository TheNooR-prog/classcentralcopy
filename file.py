from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent
from random import randrange
from datetime import datetime
import time
from bs4 import BeautifulSoup
import json
import html
from urllib.parse import quote_plus

a = ['https://www.classcentral.com/about/privacy-policy', 'https://www.classcentral.com/subject/reverse-engineering', 'https://www.classcentral.com/university/duke', 'https://www.classcentral.com/subject/disease-and-disorders', 'https://www.classcentral.com/report/writing-free-online-courses/', 'https://www.classcentral.com/subject/mathematical-logic', 'https://www.classcentral.com/university/umich', 'https://www.classcentral.com/subject/music', 'https://www.classcentral.com/subject/strategic-management', 'https://www.classcentral.com/subject/accounting', 'https://www.classcentral.com/report/author/manoel/', 'https://www.classcentral.com/provider/futurelearn', 'https://www.classcentral.com/subject/algorithms-and-data-structures', 'https://www.classcentral.com/subject/textiles', 'https://www.classcentral.com/subject/journalism', 'https://www.classcentral.com/report/author/ruima/', 'https://www.youtube.com/classcentral', 'https://www.classcentral.com/institution/british-council', 'https://www.classcentral.com/subject/psychology', 'https://www.classcentral.com/course/hy-2353', 'https://www.classcentral.com/institution/salesforce', 'https://www.classcentral.com/subject/k12', 'https://www.classcentral.com/university/iitm', 'https://www.classcentral.com/report/harvard-cs50-guide/', 'https://www.classcentral.com/subject/chemical-engineering', 'https://www.classcentral.com/collection/ivy-league-moocs', 'https://www.classcentral.com/providers', 'https://www.classcentral.com/report/mooc-based-masters-degree/', 'https://www.classcentral.com/subject/management-and-leadership', 'https://www.classcentral.com/subject/test-prep', 'https://www.classcentral.com/report/google-free-certificates/', 'https://www.classcentral.com/subject/ethical-hacking', 'https://www.classcentral.com/report/most-popular-online-courses/', 'https://www.classcentral.com/report/emoocs-2023-cfp/', 'https://www.classcentral.com/subject/visual-arts', 'https://www.classcentral.com/subject/foundations-of-mathematics', 'https://www.classcentral.com/subject/public-health', 'https://www.classcentral.com/subject/nursing', 'https://www.classcentral.com/subject/veterinary-science', 'https://www.classcentral.com/subject/cme', 'https://www.classcentral.com/subject/blockchain', 'https://www.classcentral.com/subject/innovation', 'https://www.classcentral.com/collection/ivy-league-moocs ', 'https://www.classcentral.com/report/author/dhawal/', 'https://www.classcentral.com/subject/industry-specific', 'https://www.classcentral.com/collection/top-free-online-courses ', 'https://www.classcentral.com/university/harvard', 'https://www.classcentral.com/subject/blue-team', 'https://www.classcentral.com/contact', 'https://www.classcentral.com/subject/communication-skills', 'https://www.classcentral.com/report/most-popular-courses-2023/ ', 'https://www.classcentral.com/starting-this-month', 'https://www.classcentral.com/subject/cs ', 'https://www.classcentral.com/subject/trigonometry', 'https://www.classcentral.com/institution/google', 'https://www.classcentral.com/report/author/heba/', 'https://www.classcentral.com/report/free-certificates/', 'https://www.classcentral.com/subject/law', 'https://www.classcentral.com/provider/edx', 'https://www.classcentral.com/subject/career-development', 'https://www.classcentral.com/university/stanford ', 'https://www.classcentral.com/report/author/pat-bowden/', 'https://www.classcentral.com/subject/cybersecurity', 'https://www.classcentral.com/collection/sustainability-online-courses ', 'https://www.classcentral.com/course/edx-monitoring-volcanoes-and-magma-movements-13227', 'https://www.classcentral.com/course/compstrategy-706', 'https://www.classcentral.com/university/gatech', 'https://www.classcentral.com/institution/linuxfoundation', 'https://www.classcentral.com/report/most-popular-courses-2022/', 'https://www.classcentral.com/subject/jupyter', 'https://www.classcentral.com/subject/operating-systems', 'https://www.classcentral.com/report/cs50-free-certificate/', 'https://www.classcentral.com/report/chinese-mooc-platforms/', 'https://www.classcentral.com/lists', 'https://www.classcentral.com/subject/food', 'https://www.classcentral.com/report/review-china-economic-transformation/', 'https://www.classcentral.com/report/coursera-google-new-deal/', 'https://www.classcentral.com/subject/devsecops', 'https://www.classcentral.com/subject/design-thinking', 'https://www.classcentral.com/report/india-online-degrees/', 'https://www.classcentral.com/report/best-free-online-courses-2021/', 'https://www.classcentral.com/subject/forensic-science', 'https://www.classcentral.com/report/most-cited-mooc-research/', 'https://www.classcentral.com/institution/amazon ', 'https://www.classcentral.com/subject/information-technology', 'https://www.classcentral.com/most-popular-courses', 'https://www.classcentral.com/subject/nutrition-and-wellness', 'https://www.classcentral.com/subject/sales', 'https://www.classcentral.com/subject/sustainability', 'https://www.classcentral.com/university/purdue', 'https://www.classcentral.com/report/udemy-top-courses/', 'https://www.classcentral.com/subject/calculus', 'https://www.classcentral.com/institution/smithsonian', 'https://www.classcentral.com/subject/energy-systems', 'https://www.classcentral.com/subject/ai', 'https://www.classcentral.com/subject/human-resources', 'https://www.classcentral.com/provider/udemy', 'https://www.classcentral.com/about', 'https://www.classcentral.com/subject/software-development', 'https://www.classcentral.com/university/iit-kharagpur', 'https://www.classcentral.com/report/open-university-insiders-perspective/', 'https://www.classcentral.com/subject/earth-science', 'https://www.twitter.com/classcentral', 'https://www.classcentral.com/collection/top-free-online-courses', 'https://www.classcentral.com/subject/philosophy', 'https://www.classcentral.com/report/review-academic-writing-made-easy/', 'https://www.classcentral.com/subject/computer-networking', 'https://www.classcentral.com/report/coursera-free-online-courses/', 'https://www.classcentral.com/login', 'https://www.classcentral.com/institution/ibm', 'https://www.classcentral.com/report/feed/', 'https://www.classcentral.com/subject/game-development', 'https://www.classcentral.com/subject/governance', 'https://www.classcentral.com/institution/google ', 'https://www.classcentral.com/report/best-elm-courses/', 'https://www.classcentral.com/subject/cad', 'https://www.classcentral.com/subject/bim', 'https://www.classcentral.com/subject/nonprofit', 'https://www.classcentral.com/university/mit ', 'https://www.classcentral.com/university/rice', 'https://www.classcentral.com/subject/grammar-writing', 'https://www.classcentral.com/subject/higher-education', 'https://www.classcentral.com/provider/swayam', 'https://www.classcentral.com/subject/algebra', 'https://www.classcentral.com/subject/anthropology', 'https://www.classcentral.com/subject/bioinformatics', 'https://www.classcentral.com/report/edx-top-courses/', 'https://www.classcentral.com/subject/resilience', 'https://www.classcentral.com/subject/project-management', 'https://www.classcentral.com/subject/literature', 'https://www.classcentral.com/new-online-courses', 'https://www.classcentral.com/subject/chemistry', 'https://www.classcentral.com/subject/human-rights', 'https://www.classcentral.com/report/linkedin-learning-free-learning-paths/', 'https://www.classcentral.com/subject/number-theory', 'https://www.classcentral.com/subject/finance', 'https://www.classcentral.com/subject/hci', 'https://www.classcentral.com/subject/language-learning', 'https://www.classcentral.com/subject/design-and-creativity', 'https://www.classcentral.com/institution/microsoft', 'https://www.classcentral.com/report/list-of-mooc-based-microcredentials/', 'https://www.classcentral.com/subject/gis', 'https://www.classcentral.com/subject/self-improvement', 'https://www.classcentral.com/subject/web-development', 'https://www.classcentral.com/institutions', 'https://www.classcentral.com/report/udemy-layoffs/', 'http://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.classcentral.com%2F', 'https://www.classcentral.com/report/best-resume-writing-courses/', 'https://www.classcentral.com/subject/operations-management', 'https://www.classcentral.com/university/stanford', 'https://www.classcentral.com/institution/united-nations', 'https://www.classcentral.com/subject/economics', 'https://www.classcentral.com/subject/culture', 'https://www.classcentral.com/subject/business-software', 'https://www.classcentral.com/subject/red-team', 'https://www.classcentral.com/subject/archaeology', 'https://www.classcentral.com/university/mit', 'https://www.classcentral.com/subject/statistics', 'https://www.classcentral.com/subject/risk-management', 'https://www.classcentral.com/report/best-davinci-resolve-courses/', 'https://www.classcentral.com/subject/urban-planning', 'https://www.classcentral.com/subject/stem', 'https://www.classcentral.com/subject/childhood-development', 'https://www.classcentral.com/subject/business ', 'https://www.classcentral.com/subject/customer-service', 'https://www.classcentral.com/subject/databases', 'https://www.classcentral.com/institution/amazon', 'https://www.classcentral.com/subject/teacher-development', 'https://www.classcentral.com/subject/mobile-development', 'https://www.classcentral.com/subject/digital-media', 'https://www.classcentral.com/report/100-most-popular-online-courses-2021/', 'https://www.classcentral.com/subject/pedagogy', 'https://www.classcentral.com/subject/geometry', 'https://www.classcentral.com/subject/health-care', 'https://www.classcentral.com/report/2022-year-in-review/', 'https://www.classcentral.com/subject/precalculus', 'https://www.classcentral.com/university/edinburgh', 'https://www.classcentral.com/subject/malware-analysis', 'https://www.classcentral.com/help/moocs', 'https://www.classcentral.com/university/cornell', 'https://www.classcentral.com/subject/manufacturing', 'https://www.classcentral.com/subject/applied-science', 'https://www.classcentral.com/subject/history', 'https://www.classcentral.com/subject/computer-graphics', 'https://www.classcentral.com/subject/civil-engineering', 'https://www.classcentral.com/subject/aerospace-engineering', 'https://www.classcentral.com/subject/linguistics', 'https://www.classcentral.com/subject/agriculture', 'https://www.classcentral.com/report/free-certificates/ ', 'https://www.classcentral.com/report/best-ocaml-courses/', 'https://www.classcentral.com/subject/astronomy', 'https://www.classcentral.com/subject/crisis-management', 'https://www.classcentral.com/subject/discrete-mathematics', 'https://www.classcentral.com/help', 'https://www.classcentral.com/subject/quantum-computing', 'https://www.classcentral.com/subject/library-science', 'https://www.classcentral.com/provider/coursera', 'https://www.classcentral.com/subject/presentation-skills', 'https://www.classcentral.com/subject/devops', 'https://www.classcentral.com/subject/religion', 'https://www.classcentral.com/report/best-digital-art-courses/', 'https://www.classcentral.com/subject/pentesting', 'https://www.classcentral.com/collection/ivy-league-moocs/', 'https://www.classcentral.com/university/penn', 'https://www.classcentral.com/report/coursera-top-courses/', 'https://www.classcentral.com/subject/esl', 'https://www.classcentral.com/subject/threat-intelligence', 'https://www.classcentral.com/subject/infosec-certifications', 'https://www.classcentral.com/subject/data-visualization', 'https://www.classcentral.com/report/best-free-online-courses-2022/', 'https://www.classcentral.com/subject/electrical-engineering', 'https://www.classcentral.com/university/columbia', 'https://www.classcentral.com/subject/physics', 'https://www.classcentral.com/subject/linear-programming', 'https://www.classcentral.com/provider/linkedin-learning', 'https://www.classcentral.com/subject/data-analysis', 'https://www.classcentral.com/subject/internet-of-things', 'https://www.classcentral.com/subject/network-security', 'https://www.classcentral.com/subject/materials-science', 'https://www.classcentral.com/about/careers', 'https://www.classcentral.com/subject/robotics', 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.classcentral.com%2F&text=&via=classcentral', 'https://www.classcentral.com/subject/anatomy', 'https://www.classcentral.com/subject/course-development', 'https://www.classcentral.com/subject/big-data', 'https://www.classcentral.com/subject/cloud-computing', 'https://www.classcentral.com/provider/skillshare', 'https://www.classcentral.com/subject/nanotechnology', 'https://www.classcentral.com/subject/entrepreneurship', 'https://www.classcentral.com/subject/sports', 'https://www.classcentral.com/provider/udacity', 'https://www.classcentral.com/subject/environmental-science', 'https://www.classcentral.com/report/free-google-certifications/', 'https://www.classcentral.com/subject/biology', 'https://www.classcentral.com/subject/political-science', 'https://www.classcentral.com/subject/programming-languages', 'https://www.classcentral.com/report/class-central-ddos-attack/', 'https://www.classcentral.com/signup', 'https://www.classcentral.com/subject/csr', 'https://www.classcentral.com/subject/reading', 'https://www.classcentral.com/subject/sociology', 'https://www.classcentral.com/report/futurelearn-expands-paywall/', 'https://www.linkedin.com/company/classcentral', 'https://www.classcentral.com/subject/data-mining', 'https://www.classcentral.com/subject/digital-forensics', 'https://www.classcentral.com/subject/online-education', 'https://www.classcentral.com/subject/combinatorics', 'https://www.classcentral.com/subject/machine-learning', 'https://www.classcentral.com/subject/ethics', 'https://www.classcentral.com/subject/deep-learning', 'https://www.classcentral.com/subject/distributed-systems', 'https://www.classcentral.com/report/online-learning-deals/ ', 'https://www.classcentral.com/subject/social-work', 'https://www.facebook.com/classcentral', 'https://www.classcentral.com/subject/osint', 'mailto:?subject=&body=%20https%3A%2F%2Fwww.classcentral.com%2F', 'https://www.classcentral.com/subject/cryptography', 'https://www.classcentral.com/subject/mechanical-engineering', 'https://www.classcentral.com/report/udemy-by-the-numbers/', 'https://www.classcentral.com/subject/business-intelligence', 'https://www.classcentral.com/report/category/best-courses/ ', 'https://www.classcentral.com/subject/marketing']

errors = ""
urls = a
print(urls)
for url in urls:
    try:
        if url[-1] != '/':
            url = url + '/'
        print("URL", "\n", url)
        webpage_directory = url.split("//")[1]
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

        def get_translation(word):
            try:
                with open('dictionary.json', 'r') as f:
                    dictionary = json.load(f)
            except FileNotFoundError:
                return None

            if word in dictionary:
                return dictionary[word]
            else:
                return None

        # translator
        def translate_term(text, target_lang, source_lang="en"):
            translation = 'N/A'

            try:
                browser.get(f"https://translate.google.com/?sl={source_lang}&tl={target_lang}&text={text}&op=translate")
                i = 1
                translation = []
                while i < 200:
                    if i == 1:
                        condition = EC.presence_of_element_located((By.XPATH, f'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span/span'))
                        element = WebDriverWait(browser, 10).until(condition)
                        translation.append(element.text)
                        i += 2
                    else:
                        condition = EC.presence_of_element_located((By.XPATH, f'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[1]/span[1]/span[{i}]/span'))
                        element = WebDriverWait(browser, 10).until(condition)
                        translation.append(element.text)
                        i += 2
                time.sleep(randrange(2))
            except Exception:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Something went wrong at: ", current_time)

            return translation


        # to json
        try:
            with open(original_index_path, encoding='utf-8') as fp:
                soup = BeautifulSoup(fp, 'html.parser')
        except:
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

        def text_list_creating(json_data, text_list):
            if isinstance(json_data, dict):
                if 'tag' in json_data:
                    if json_data['tag'] in ['script', 'style']:
                        return  # ignore text in script and style tags
                    if 'text' in json_data:
                        if not get_translation(json_data['text'].strip()):
                            text_list.append(json_data['text'])
                    if 'children' in json_data:
                        for child in json_data['children']:
                            text_list_creating(child, text_list)
                else:
                    for key in json_data:
                        text_list_creating(json_data[key], text_list)
            elif isinstance(json_data, list):
                for item in json_data:
                    text_list_creating(item, text_list)


        text_list = []
        text_list_creating(json_data,  text_list)
        #
        i = 0
        translated_list = []
        while i <= len(text_list):
            text_str = "" + "\n".join(map(str, text_list[i:i+100]))
            translated_list_part = translate_term(quote_plus(text_str), "hi")
            translated_list += translated_list_part
            i += 100
        print(text_list, "\n", len(text_list), "\n")
        print(translated_list, "\n", len(translated_list), "\n")

        def add_translation(word, translation):
            try:
                with open('dictionary.json', 'r') as f:
                    dictionary = json.load(f)
            except FileNotFoundError:
                dictionary = {}

            if translation != 'N/A':
                dictionary[word] = translation

                with open('dictionary.json', 'w') as f:
                    json.dump(dictionary, f)

                print(f'Added "{word}": "{translation}" to dictionary.')

        # add translations to dictionary
        for i in range(0, len(text_list)):
            if get_translation(text_list[i]):
                print(f'"{text_list[i]}" is in dictionary.')
            else:
                if text_list[i] == '':
                    text_list[i] = ' '
                if translated_list[i] == '':
                    translated_list[i] = ' '
                add_translation(text_list[i], translated_list[i])

    except Exception as err:
        print("Error:", err, url)
        errors += f"Error: {err} | {url}"
        continue
print(errors)