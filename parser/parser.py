import requests
import time
import random
from database import *
import traceback
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def get_vacancies(cityName, cityId, vacancy, page):
    params = {'text': f"{vacancy} {cityName}", 'area': cityId, 'per_page': 2, 'page': page}
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    return response.json()

def process_vacancy_skills(vacancy_id):
    response = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}')
    data = response.json()
    done_list = []
    for vacancy_skill in data['key_skills']:
        for skill in db_get_skills():
            cosine_sim = fuzz.token_sort_ratio(vacancy_skill['name'], skill[1])
            print(cosine_sim)
            if cosine_sim >= 70:
                done_list.append(skill[0])
    db_save_vacancy_skills(vacancy_id, done_list)


def parse_vacancies():
    for city_id in db_get_cities():
        for vacancy in db_get_vacancy_list():
            page = 0
            try:
                while True:
                    data = get_vacancies(city_id[1], city_id[0], vacancy[1], page)
                    if not data.get('items'):
                            break
                    for item in data['items']:
                        db_save_vacancy_info(item, vacancy[0] ,city_id[0])
                        process_vacancy_skills(item['id'])
                    page+=1
                    time.sleep(random.uniform(1, 2))
            except Exception:
                print('Жора лох')
                traceback.print_exc()
parse_vacancies()

















