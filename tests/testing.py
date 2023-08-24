from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
service = Service(executable_path='./chromedriver.exe')

chrome_path = r"./chromedriver.exe"
driver = webdriver.Chrome(options=chrome_options,service=service)
driver.get('https://hkmovie6.com/showing')
