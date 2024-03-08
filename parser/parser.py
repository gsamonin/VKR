import requests
import time
import random
from database import *
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
                
# Вызываем функцию парсинга вакансий                
parse_vacancies()

















