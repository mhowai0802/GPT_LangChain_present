from langchain.agents import Tool
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def movie_summary(input):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_path = r"chromedriver"
    service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(options=chrome_options,service=service)
    driver.get('https://hkmovie6.com/showing')
    time.sleep(10)
    master = []
    movie_table = driver.find_element(By.CSS_SELECTOR, f'.shows')
    for element in movie_table.find_elements(By.CSS_SELECTOR, '.movie'):
        try:
            dict = {
                'Movie_name': element.find_element(By.CSS_SELECTOR, '.name').text,
                'Movie_rating': element.find_element(By.CSS_SELECTOR, '.ratingText').text
            }
            master.append(dict)
        except:
            break
    df = pd.DataFrame(master).sort_values(by='Movie_rating', ascending=False).head(3)
    return df["Movie_name"].tolist()

movie_summary_tool = Tool(
    name="movie_summary",
    func=movie_summary,
    description="Use this tool to list out the movies from list of dict.",
    return_direct=True
)
