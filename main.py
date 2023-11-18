import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import os

storage = [
    "https://tenchat.ru/komarov",
    "https://tenchat.ru/sboiko",
    "https://tenchat.ru/pasha_napishi",
    "https://tenchat.ru/Chayrev",
    "https://tenchat.ru/AnnaKulik",
    "https://tenchat.ru/ViktorReshetov",
    "https://tenchat.ru/theplotnikov",
    "https://tenchat.ru/stanislavlarin",
    "https://tenchat.ru/VeronikaRazina",
    "https://tenchat.ru/gbakhin",
    "https://tenchat.ru/mrsklrv",
    "https://tenchat.ru/IraFedotova",
    "https://tenchat.ru/1071771",
    "https://tenchat.ru/Stefan",
    "https://tenchat.ru/morozova_proffi",
    "https://tenchat.ru/0621812",
    "https://tenchat.ru/0644275",
    "https://tenchat.ru/daria_del",
    "https://tenchat.ru/nezhdanov",
    "https://tenchat.ru/2072639",
    "https://tenchat.ru/0368643",
    "https://tenchat.ru/Andrey-Karpov-PVS-Studio",
    "https://tenchat.ru/dima_b2b_marketing",
    "https://tenchat.ru/uli_on_air",
    "https://tenchat.ru/gellerad",
    "https://tenchat.ru/1234487",
    "https://tenchat.ru/0557592",
    "https://tenchat.ru/platon_maks",
    "https://tenchat.ru/1789089",
    "https://tenchat.ru/akret",
    "https://tenchat.ru/andrey_belozerov",
    "https://tenchat.ru/1267230",
    "https://tenchat.ru/shcherbakov",
    "https://tenchat.ru/0534411",
    "https://tenchat.ru/Dasha_astafeva",
    "https://tenchat.ru/galinskiy_alexandr",
    "https://tenchat.ru/0808117",
    "https://tenchat.ru/0326545",
    "https://tenchat.ru/pavelsedykh",
    "https://tenchat.ru/1192482",
    "https://tenchat.ru/egor_muravev",
    "https://tenchat.ru/stanislavski",
    "https://tenchat.ru/1987892",
    "https://tenchat.ru/mnikolaeva",
    "https://tenchat.ru/SergeyVetkin",
    "https://tenchat.ru/kseniya_gde_leto",
    "https://tenchat.ru/olesmil",
    "https://tenchat.ru/annalarionova",
    "https://tenchat.ru/STACE",
    "https://tenchat.ru/marketolog_ot_boga",
    "https://tenchat.ru/alextimokhov",
    "https://tenchat.ru/2220706",
    "https://tenchat.ru/valentinapavlichuk",
    "https://tenchat.ru/dolgushev_a",
    "https://tenchat.ru/0595812",
    "https://tenchat.ru/ViktorBrs",
    "https://tenchat.ru/0538454",
    "https://tenchat.ru/1390300",
    "https://tenchat.ru/2051724",
    "https://tenchat.ru/0995885",
    "https://tenchat.ru/0772196",
    "https://tenchat.ru/0566739",
    "https://tenchat.ru/0545267",
    "https://tenchat.ru/soboleva_irene",
    "https://tenchat.ru/2201706",
    "https://tenchat.ru/aleksmell",
    "https://tenchat.ru/1135791",
    "https://tenchat.ru/ddoynikov",
    "https://tenchat.ru/2003633",
    "https://tenchat.ru/0614289",
    "https://tenchat.ru/0604020",
    "https://tenchat.ru/0773301",
    "https://tenchat.ru/veron-i-ca",
    "https://tenchat.ru/m_nikitin_pro",
    "https://tenchat.ru/artles",
    "https://tenchat.ru/your_fetishhhhh",
    "https://tenchat.ru/a_ermakov",
    "https://tenchat.ru/0657438",
    "https://tenchat.ru/2332482",
    "https://tenchat.ru/1963424",
    "https://tenchat.ru/Bolshakov_Alex",
    "https://tenchat.ru/sazkv",
    "https://tenchat.ru/lisapanova",
    "https://tenchat.ru/0533686",
    "https://tenchat.ru/1182044",
    "https://tenchat.ru/2534768",
    "https://tenchat.ru/1682063",
    "https://tenchat.ru/1916333",
    "https://tenchat.ru/2391251",
    "https://tenchat.ru/afanasevp",
    "https://tenchat.ru/StrateGeek",
    "https://tenchat.ru/vchernov",
    "https://tenchat.ru/mazur_online",
    "https://tenchat.ru/any2any",
    "https://tenchat.ru/2536607",
    "https://tenchat.ru/1111358",
    "https://tenchat.ru/zvezda",
    "https://tenchat.ru/0762987",
    "https://tenchat.ru/1931855",
    "https://tenchat.ru/0829828",
    "https://tenchat.ru/julia_lazovaya",
    "https://tenchat.ru/adam_grig",
    "https://tenchat.ru/babchihin",
    "https://tenchat.ru/pavel-levshin",
    "https://tenchat.ru/dpochtarenko",
    "https://tenchat.ru/boretskiyad",
    "https://tenchat.ru/imazitova",
    "https://tenchat.ru/0231176",
    "https://tenchat.ru/0507922",
    "https://tenchat.ru/0498632",
    "https://tenchat.ru/shramkel",
    "https://tenchat.ru/1070964",
    "https://tenchat.ru/0623066",
    "https://tenchat.ru/zenmarketing",
    "https://tenchat.ru/mikrobird",
    "https://tenchat.ru/UncleZombie",
    "https://tenchat.ru/0685318",
    "https://tenchat.ru/natalie_marketing",
    "https://tenchat.ru/0269755",
    "https://tenchat.ru/rookeed",
    "https://tenchat.ru/1125552",
    "https://tenchat.ru/sergey_pro",
    "https://tenchat.ru/ivan_fefeloff",
    "https://tenchat.ru/0557835",
    "https://tenchat.ru/alexbelkov",
    "https://tenchat.ru/0774734",
    "https://tenchat.ru/0863840",
    "https://tenchat.ru/1350903",
    "https://tenchat.ru/dimaushurlyak",
    "https://tenchat.ru/0297142",
    "https://tenchat.ru/1876088",
    "https://tenchat.ru/0627598",
    "https://tenchat.ru/tarakanova",
    "https://tenchat.ru/0738252",
    "https://tenchat.ru/OlgaB",
    "https://tenchat.ru/0607507",
    "https://tenchat.ru/mara_morevna",
    "https://tenchat.ru/Julia_A",
    "https://tenchat.ru/igoravdasev",
    "https://tenchat.ru/paismar",
    "https://tenchat.ru/vladimir_zholobov",
    "https://tenchat.ru/mtrusov",
    "https://tenchat.ru/PLAYESTATE",
    "https://tenchat.ru/1470382",
    "https://tenchat.ru/alexeykhodykin",
    "https://tenchat.ru/1531982"
]

# # First version: parse from local file
# with open('source_PC.htm', 'r', encoding='utf-8') as webpage:
#     soup = BeautifulSoup(webpage, 'html.parser')
#     people = soup.find_all(class_='text-gray-900 mr-3 min-w-0 flex-1')
#     for person in people:
#         job_info = person.find(class_='mobile:color-gray-300 mt-3 text-sm mobile:mt-1 mobile:text-xs')
#         if job_info is not None:
#             job_place = job_info.find(class_='tc-break-word mb-1 line-clamp-2')
#             if job_place is not None:
#                 company_type = job_place.find(class_='tc-link tracking-smallest')
#
#                 if company_type is not None:
#                     company_type_text = company_type.text
#                 else:
#                     company_type_text = "N/A"  # or any other default value
#
#                 if job_info is not None:
#                     job_info_text = job_info.text
#                 else:
#                     job_info_text = "N/A"
#
#                 if job_place is not None:
#                     job_place_text = job_place.text
#                 else:
#                     job_place_text = "N/A"
#
#                 if company_type_text != 'N/A' and "АО" in company_type_text:
#                     name = person.find(class_='relative flex items-center pr-5 font-medium text-gray-1100 mobile:text-sm')
#                     tag_a = name.find('a', class_='tc-btn-focus block !decoration-solid hover:underline')
#                     if tag_a:
#                         link = tag_a['href']
#                         print(link)

# Second version: parse from website
# set the path to the Firefox WebDriver executable
geckodriver_path = 'geckodriver.exe'

# add the WebDriver path to the system's PATH variable
os.environ['PATH'] += os.pathsep + geckodriver_path

# initialize the Firefox WebDriver
driver = webdriver.Firefox()

# navigate to the website
driver.get("https://tenchat.ru/auth/sign-in")

wait = WebDriverWait(driver, 60)  # Adjust the timeout as needed
time.sleep(60)

# send an HTTP GET request to the URL
driver.get("https://tenchat.ru/search/people?searchStr=%D0%B4%D0%B8%D1%80%D0%B5%D0%BA%D1%82%D0%BE%D1%80+%D0%BF%D0%BE+%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D1%83")

# scroll down
n = 2000 # amount of people to parse

# we want to parse n people, but page has 20 users, то then we do N // 20 times
for i in range(n // 20):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5) # ждем пару секунд, чтобы все прогрузилось и отработало

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

people = soup.find_all(class_='text-gray-900 mr-3 min-w-0 flex-1')
base_url = 'https://tenchat.ru'

# after we have n elements on webpage and we start parse
for person in people:
    job_info = person.find(class_='mobile:color-gray-300 mt-3 text-sm mobile:mt-1 mobile:text-xs')
    if job_info is not None:
        job_place = job_info.find(class_='tc-break-word mb-1 line-clamp-2')
        if job_place is not None:
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
                    if full_link not in storage:
                        print(full_link)

driver.quit()