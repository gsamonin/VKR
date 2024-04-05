import requests
import time
import random
from database import *
from bs4 import BeautifulSoup
from time import sleep
import traceback
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

# Функция для получения списка вакансий
def get_vacancies(cityName, cityId, vacancy, page):
    params = {'text': f"{vacancy} {cityName}", 'area': cityId, 'per_page': 2, 'page': page}
    response = requests.get('https://api.hh.ru/vacancies', params=params)

    # Возвращаем результат запроса в формате JSO
    return response.json()

# Функция для обработки навыков для вакансии
def process_vacancy_skills(vacancy_id):
    response = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}')
    data = response.json()
    done_list = []
    # Перебираем ключевые навыки из данных вакансии
    for vacancy_skill in data['key_skills']:
        for skill in db_get_skills():
            cosine_sim = fuzz.token_sort_ratio(vacancy_skill['name'], skill[1])
            print(cosine_sim) # Выводим результат сравнения для отладки
            # Если сходство больше или равно 70, добавляем навык в список
            if cosine_sim >= 70:
                done_list.append(skill[0])

    # Сохраняем список совпадающих навыков для вакансии в базу данных            
    db_save_vacancy_skills(vacancy_id, done_list)

# Функция для парсинга вакансий
def parse_vacancies():
    # Перебираем все города из базы данных
    for city_id in db_get_cities():
        # Перебираем все вакансии из списка вакансий в базе данных
        for vacancy in db_get_vacancy_list():
            page = 0
            try:
                # Парсим страницы с вакансиями
                while True:
                    if page == 5: break
                    data = get_vacancies(city_id[1], city_id[0], vacancy[1], page)
                    if not data.get('items'):
                            break
                    for item in data['items']:
                        db_save_vacancy_info(item, vacancy[0] ,city_id[0])
                        process_vacancy_skills(item['id'])
                    # Увеличиваем номер страницы и добавляем случайную задержку
                    page+=1
                    time.sleep(random.uniform(1, 2))
            except Exception:
                print('Test')
                traceback.print_exc()

def parse_programms():
    for p in range (1, 32): #32
        print(p)
        
        url = f"https://postupi.online/professiya/razrabotchik/programmi/?page_num={p}"
        r =requests.get(url)
        sleep(3) 
        soup = BeautifulSoup(r.text, 'lxml')

        programms = soup.find_all('div', class_='list__info')

        for programm in programms:
            # db_save_programms(programm)
            print(programm.find('h2', class_='list__h').find('a').text)
            print('Бюджетных мест: '+programm.find('span', class_='visible-mid', string=['Бюджетных мест 2024', 'Бюджетных мест 2023', 'Бюджетных мест 0']).find_next().text.lstrip())
            print('Платных мест: '+programm.find('span', class_='visible-mid', string=['Платных мест 2024', 'Платных мест 2023', 'Платных мест 0']).find_next().text.lstrip())
        
def parse_courses():
    CourseNames = ["languagePython", "languageJava","languageCPlusPlus","languageGo", "languageOneS", "languageRuby", "languageCSharp", "languageSwift", "languagePHP", "android", "front", "back"]
    for name in CourseNames:
        print('@@@@@@@@@@@'+ name)
        url = f"https://www.sravni.ru/kursy/programmirovanie/?coursesThematics={name}&courseLevels=beginner&courseLevels=advanced"
        r =requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        
        courses = soup.find('div', class_='style_wrapperRows__XOdZm').find_all('div', class_='style_wrapper__JdiJD')
        
        for course in courses:
            try:
                db_save_courses(course)
                course_name = course.find('div', class_='style_heading__WaLQK style_headingTopPadding__sB1tl _ptw42j').string
                organization_name = course.find('img', class_='style_logo__r1hDN style_logoBorder__xa_Xd').get('title')
                price = int(course.find('div', class_='style_price__vSy5p').find('span', class_='style_nowrap__12nI5 _1qco5vz _18gj9po').text.lstrip().replace(u'\xa0', '').replace('₽', ''))
                rating = float(course.find('span', class_='style_wrapper__Q5XQE').find('span', class_='').text)
                
                print("Название курса:", course_name)
                print("Название организации:", organization_name)
                print("Цена:", price)
                print("Рейтинг:", rating)
                print("-" * 50)
            except Exception:
                pass 
    
parse_vacancies()
# Вызываем функцию парсинга вакансий                

















