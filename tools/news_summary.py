from langchain.agents import Tool
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def news_summary(input):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("window-size=1024,768")
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.get(
        'https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE5vTmpRU0JYcG9MVWhMS0FBUAE?hl=zh-HK&gl=HK&ceid=HK%3Azh-Hant')
    time.sleep(10)
    master = []
    news_table = driver.find_element(By.XPATH, f'/html/body/c-wiz/div/main/c-wiz/div[2]/c-wiz')
    for element in news_table.find_elements(By.TAG_NAME, 'c-wiz'):
        try:
            master.append(
                f"{element.find_element(By.CSS_SELECTOR, '.vr1PYe').text}: {element.find_element(By.CSS_SELECTOR, '.gPFEn').text}")
        except:
            break
    return master


news_summary_tool = Tool(
    name="news_summary",
    func=news_summary,
    description="Use this tool to list out the news from list of dict.",
    return_direct=True
)
