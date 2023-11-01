import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import os

# first version: parse from local file
# with open('TenChat.html',  'r', encoding='utf-8') as webpage:
#     soup = BeautifulSoup(webpage, 'html.parser')
#     people = soup.find_all(class_='text-gray-900 mr-3 min-w-0 flex-1')
#     for person in people:
#         job_info = person.find(class_='mobile:color-gray-300 mt-3 text-sm mobile:mt-1 mobile:text-xs')
#         job_place = job_info.find(class_='tc-break-word mb-1 line-clamp-2')
#         company_type = job_place.find(class_='tc-link tracking-smallest')
#
#         if company_type is not None:
#             company_type_text = company_type.text
#         else:
#             company_type_text = "N/A"  # or any other default value
#
#         if job_info is not None:
#             job_info_text = job_info.text
#         else:
#             job_info_text = "N/A"
#
#         if job_place is not None:
#             job_place_text = job_place.text
#         else:
#             job_place_text = "N/A"
#
#         if company_type_text != 'N/A' and "ООО" in company_type_text:
#             name = person.find(class_='relative flex items-center pr-5 font-medium text-gray-1100 mobile:text-sm')
#             tag_a = name.find('a', class_='tc-btn-focus block !decoration-solid hover:underline')
#             if tag_a:
#                 link = tag_a['href']
#                 print(link)

# second version: parse from website
# Set the path to the Firefox WebDriver executable
geckodriver_path = 'geckodriver.exe'

# Add the WebDriver path to the system's PATH variable
os.environ['PATH'] += os.pathsep + geckodriver_path

# Initialize the Firefox WebDriver
driver = webdriver.Firefox()

# 1. Navigate to the website
driver.get("https://tenchat.ru/auth/sign-in")

wait = WebDriverWait(driver, 60)  # Adjust the timeout as needed
time.sleep(60)
# Send an HTTP GET request to the URL
driver.get("https://tenchat.ru/search/people?searchStr=%D0%B4%D0%B8%D1%80%D0%B5%D0%BA%D1%82%D0%BE%D1%80+%D0%BF%D0%BE+%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D1%83")

# пролистывание вниз
n = 100 # количество человек, которое хочешь спарсить, советую начинать с небольшого количества(например 60-140)

# т.к. ты хочешь спарсить N человек, а на странице показывается 20 юзеров, то делает скролл вниз N // 20 раз
for i in range(n // 20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5) # ждем пару секунд, чтобы все прогрузилось и отработало

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

people = soup.find_all(class_='text-gray-900 mr-3 min-w-0 flex-1')
base_url = 'https://tenchat.ru'
# после пролистывания у нас не странице имеется N юзеров и начинаем их парсить
for person in people:
    job_info = person.find(class_='mobile:color-gray-300 mt-3 text-sm mobile:mt-1 mobile:text-xs')
    job_place = job_info.find(class_='tc-break-word mb-1 line-clamp-2')
    company_type = job_place.find(class_='tc-link tracking-smallest')

    if company_type is not None:
        company_type_text = company_type.text
    else:
        company_type_text = "N/A"  # or any other default value

    if job_info is not None:
        job_info_text = job_info.text
    else:
        job_info_text = "N/A"

    if job_place is not None:
        job_place_text = job_place.text
    else:
        job_place_text = "N/A"

    if company_type_text != 'N/A' and "ООО" in company_type_text:
        name = person.find(class_='relative flex items-center pr-5 font-medium text-gray-1100 mobile:text-sm')
        tag_a = name.find('a', class_='tc-btn-focus block !decoration-solid hover:underline')
        if tag_a:
            link = tag_a['href']
            full_link = base_url + link
            print(full_link)

driver.quit()