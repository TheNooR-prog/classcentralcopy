from selenium import webdriver
import time
import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json
from bs4 import BeautifulSoup
import re
errors = ""
main_page_url = "https://www.classcentral.com/"

# Main Function
if __name__ == "__main__":

    # Enable Performance Logging of Chrome.
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

    # Create the webdriver object and pass the arguments
    options = webdriver.ChromeOptions()

    # Chrome will start in Headless mode
    options.add_argument('headless')

    # Ignores any certificate errors if there is any
    options.add_argument("--ignore-certificate-errors")

    # Startup the chrome webdriver with executable path and
    # pass the chrome options and desired capabilities as
    # parameters.
    driver = webdriver.Chrome(options=options,
                              desired_capabilities=desired_capabilities)

    # Send a request to the website and let it load
    driver.get(main_page_url)

    # Sleeps for 10 seconds
    time.sleep(10)

    html = driver.page_source
    with open(f'{main_page_url.split("//")[1]}original_index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    with open(f'{main_page_url.split("//")[1]}original_index.html', 'r') as f:
        html = f.read()

    # Parse the HTML file using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all script tags with a src attribute
    script_tags = soup.find_all('script', src=True)

    # Loop over the script tags and update the src attribute
    for script in script_tags:
        src = script['src']
        # Check if the src starts with "//"
        if src.startswith('//'):
            # Add "https:" to the beginning of the src
            new_src = 'https:' + src
            # Update the src attribute in the script tag
            script['src'] = new_src

    # Write the updated HTML back to the file
    with open(f'{main_page_url.split("//")[1]}original_index.html', 'w') as f:
        f.write(str(soup))

    # Gets all the logs from performance in Chrome
    logs = driver.get_log("performance")

    # Opens a writable JSON file and writes the logs in it
    with open("network_log.json", "w", encoding="utf-8") as f:
        f.write("[")

        # Iterates every logs and parses it using JSON
        for log in logs:
            network_log = json.loads(log["message"])["message"]

            # Checks if the current 'method' key has any
            # Network related value.
            if ("Network.response" in network_log["method"]
                    or "Network.request" in network_log["method"]
                    or "Network.webSocket" in network_log["method"]):
                # Writes the network log to a JSON file by
                # converting the dictionary to a JSON string
                # using json.dumps().
                f.write(json.dumps(network_log) + ",")
        f.write("{}]")

    print("Quitting Selenium WebDriver")
    driver.quit()


    # Read the JSON File and parse it using
    # json.loads() to find the urls containing images.
    json_file_path = "network_log.json"
    with open(json_file_path, "r", encoding="utf-8") as f:
        logs = json.loads(f.read())
    scripts_urls = []
    # Iterate the logs
    for log in logs:

        # Except block will be accessed if any of the
        # following keys are missing.
        try:
            # URL is present inside the following keys
            url = log["params"]["request"]["url"]
            if main_page_url.split("//")[1] in url:
                scripts_urls.append(url)
        except Exception as e:
            pass


    # scripts saving

    driver = webdriver.Chrome()
    for script_url in scripts_urls:
        if script_url != main_page_url:
            driver.get(script_url)

            # Wait for the page to fully load
            time.sleep(5)

            # Get the text content of the page without HTML tags
            text_content = driver.execute_script("return document.documentElement.textContent;")

            # Create a directory named "webpack" if it does not exist
            if not os.path.exists(f""+"/".join(map(str, ((script_url.split("//")[1]).split("/")[:-1])))):
                os.makedirs(f""+"/".join(map(str, ((script_url.split("//")[1]).split("/")[:-1]))))

            # Save the text content to a file in the directory
            with open(script_url.split("//")[1], 'w', encoding='utf-8') as f:
                f.write(text_content)

    # get first level links

    first_level_urls = []
    html_file = open(f'{main_page_url.split("//")[1]}original_index.html')
    soup = BeautifulSoup(html_file, "html.parser")

    # Find all anchor tags in the HTML file
    links = soup.find_all("a")

    # get first level urls
    for link in links:
        if link.get('href') != "/" and link.get('href') != main_page_url:
            if link.get('href').startswith('/'):
                first_level_url = main_page_url[:-1] + link.get('href')
                first_level_urls.append(first_level_url)
            else:
                first_level_url = link.get('href')
                first_level_urls.append(first_level_url)
    print(first_level_urls)

    # modify main_page links
    for link in links:
        href = link.get("href")
        if href.startswith("/"):
            href = "/www.classcentral.com" + href
            link["href"] = href

        if href.startswith("h"):
            href = "/" + href.split("//")[1]
            link["href"] = href

    # Save the modified HTML file
    try:
        with open(f'{main_page_url.split("//")[1]}original_index.html', "w", encoding="utf-8") as file:
            file.write(str(soup))
    except:
        with open(f'{main_page_url.split("//")[1]}original_index.html', "w") as file:
            file.write(str(soup))

    log = {}
    # first level pages files download
    for page_url in first_level_urls[19:]:
        try:
            if page_url[-1] != '/':
                page_url = page_url + '/'
            print("\n", "\n", page_url)

            # Enable Performance Logging of Chrome.
            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities["goog:loggingPrefs"] = {"performance": "ALL"}

            # Create the webdriver object and pass the arguments
            options = webdriver.ChromeOptions()

            # Chrome will start in Headless mode
            options.add_argument('headless')

            # Ignores any certificate errors if there is any
            options.add_argument("--ignore-certificate-errors")

            # Startup the chrome webdriver with executable path and
            # pass the chrome options and desired capabilities as
            # parameters.
            driver = webdriver.Chrome(options=options,
                                      desired_capabilities=desired_capabilities)

            # Send a request to the website and let it load
            driver.get(page_url)

            # Sleeps for 10 seconds
            time.sleep(10)

            # Create a directory if it does not exist
            if not os.path.exists(page_url.split("//")[1][:-1]):
                os.makedirs(page_url.split("//")[1][:-1])
                print(page_url.split("//")[1][:-1])

            html = driver.page_source
            try:
                with open(f'{page_url.split("//")[1]}original_index.html', 'w', encoding='utf-8') as f:
                    f.write(html)
            except:
                with open(f'{page_url.split("//")[1]}original_index.html', 'w') as f:
                    f.write(html)

            try:
                with open(f'{page_url.split("//")[1]}original_index.html', 'r', encoding='utf-8') as f:
                    html = f.read()
            except:
                with open(f'{page_url.split("//")[1]}original_index.html', 'r') as f:
                    html = f.read()

            # Parse the HTML file using BeautifulSoup
            soup = BeautifulSoup(html, 'html.parser')

            # Find all script tags with a src attribute
            script_tags = soup.find_all('script', src=True)

            # Loop over the script tags and update the src attribute
            for script in script_tags:
                src = script['src']
                # Check if the src starts with "//"
                if src.startswith('//'):
                    # Add "https:" to the beginning of the src
                    new_src = 'https:' + src
                    # Update the src attribute in the script tag
                    script['src'] = new_src

            # Write the updated HTML back to the file
            try:
                with open(f'{page_url.split("//")[1]}original_index.html', 'w', encoding='utf-8') as f:
                    f.write(str(soup))
            except:
                with open(f'{page_url.split("//")[1]}original_index.html', 'w') as f:
                    f.write(str(soup))

            # Gets all the logs from performance in Chrome
            logs = driver.get_log("performance")

            # Opens a writable JSON file and writes the logs in it
            try:
                with open("network_log.json", "w", encoding="utf-8") as f:
                    f.write("[")
            except:
                with open("network_log.json", "w") as f:
                    f.write("[")

                # Iterates every logs and parses it using JSON
                for log in logs:
                    network_log = json.loads(log["message"])["message"]

                    # Checks if the current 'method' key has any
                    # Network related value.
                    if ("Network.response" in network_log["method"]
                            or "Network.request" in network_log["method"]
                            or "Network.webSocket" in network_log["method"]):
                        # Writes the network log to a JSON file by
                        # converting the dictionary to a JSON string
                        # using json.dumps().
                        f.write(json.dumps(network_log) + ",")
                f.write("{}]")

            print("Quitting Selenium WebDriver")
            driver.quit()

            # Read the JSON File and parse it using
            # json.loads() to find the urls containing images.
            json_file_path = "network_log.json"
            try:
                with open(json_file_path, "r", encoding="utf-8") as f:
                    logs = json.loads(f.read())
            except:
                with open(json_file_path, "r") as f:
                    logs = json.loads(f.read())
            scripts_urls = []
            # Iterate the logs
            for log in logs:

                # Except block will be accessed if any of the
                # following keys are missing.
                try:
                    # URL is present inside the following keys
                    url = log["params"]["request"]["url"]
                    if page_url.split("//")[1] in url:
                        scripts_urls.append(url)
                except Exception as e:
                    pass

            # scripts saving

            driver = webdriver.Chrome()
            for script_url in scripts_urls:
                if script_url != page_url:
                    driver.get(script_url)

                    # Wait for the page to fully load
                    time.sleep(5)

                    # Get the text content of the page without HTML tags
                    text_content = driver.execute_script("return document.documentElement.textContent;")

                    # Create a directory if it does not exist
                    if not os.path.exists(f"" + "/".join(map(str, ((script_url.split("//")[1]).split("/")[:-1])))):
                        os.makedirs(f"" + "/".join(map(str, ((script_url.split("//")[1]).split("/")[:-1]))))

                    # Save the text content to a file in the directory
                    try:
                        with open(script_url.split("//")[1], 'w', encoding='utf-8') as f:
                            f.write(text_content)
                    except:
                        with open(script_url.split("//")[1], 'w') as f:
                            f.write(text_content)

                # get first level links

                first_level_urls = []
                html_file = open(f'{page_url.split("//")[1]}original_index.html')
                soup = BeautifulSoup(html_file, "html.parser")

                # Find all anchor tags in the HTML file
                links = soup.find_all("a")

                # modify page links
                for link in links:
                    href = link.get("href")
                    if href.startswith("/"):
                        href = page_url.split('com/')[0] + "com" + href
                        link["href"] = href
                        print(href)

                # Save the modified HTML file
                try:
                    with open(f'{page_url.split("//")[1]}original_index.html', "w", encoding='utf-8') as file:
                        file.write(str(soup))
                except:
                    with open(f'{page_url.split("//")[1]}original_index.html', "w") as file:
                        file.write(str(soup))

                print("Added", page_url)

        except Exception as err:
            print("Error:", err, page_url)
            raise err
            # errors += f"Error: {err} | {page_url}"
            # continue
print(errors)