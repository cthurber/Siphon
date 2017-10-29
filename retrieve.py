import os
import time
import arrow
import requests
from tldextract import extract
from random import randrange
from splinter import Browser
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# get_proxy / set_ip

# Returns a list of User Agents stored in a file, defaults to ...
def load_useragents(filename):
    try:
        user_agents = []

        with open(filename, 'r') as user_agent_file:
            for line in user_agent_file:
                user_agents.append(line.replace('\n',''))

    except:

        # Log this: "Failed, defaulting to 1 User Agent"
        user_agents = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"]

    return user_agents

# Returns a random User Agent for our browser given a file with User Agents
def get_useragent(filename = "user_agents.txt"):
    user_agents = load_useragents(filename)
    log_state = "Selected User Agent:"

    if len(user_agents) > 1:
        user_agent = user_agents[randrange(0,len(user_agents)-1,1)]
        print(log_state,user_agent)
        return user_agent
    else:
        print(log_state,user_agents[0])
        return user_agents[0]

# Returns a random integer for delay between page grabs
def get_delay(min_d=0,max_d=3):
    return randrange(min_d,max_d,1)

def get_google(url):
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = get_useragent()
    browser = Browser('phantomjs',desired_capabilities=dcap) #
    browser.driver.set_window_size(1124, 850)

    browser.visit(url)
    time.sleep(get_delay(1,3))
    source = browser.html

    browser.quit()

    return source

# Retrieves page from 'url'
def get_page(url):
    time.sleep(get_delay())

    headers = {
        'User-Agent': get_useragent()
    }

    page = requests.get(url, headers=headers)

    if page.status_code == 200:
        return str(page.text)
    else:
        return "Oops"

# Returns date as YYYY-MM-DD format
def make_date():
    made_date = str(arrow.now().format('YYYY-MM-DD'))
    return made_date

# Returns uniform filename
def make_filename(url):
    return url.split('/')[-1] + '.html'

# TODO - Clean up URL stripping to config/json
# Saves page at 'url' to 'location'
def save_page(url, location = "./data"):

    if "bing.com" in url:
        return False
    if "yahoo.com" in url:
        try:
            url = url.split("RU=")[1].split("/RK")[0]
        except:
            print(url)

    page = get_page(url)
    root = location
    date_str = make_date() + '/'
    site_name = extract(url).domain + '/'

    if not os.path.exists(root+date_str):
        os.makedirs(root+date_str)
    if not os.path.exists(root+date_str+site_name):
        os.makedirs(root+date_str+site_name)

    location = root + date_str + site_name + make_filename(url)

    with open(location, 'w') as save_loc:
        print(page, file=save_loc)

    return True
