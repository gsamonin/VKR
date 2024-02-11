import logging
import requests
import psycopg2
import time
import random

from config import host, user, password, database, port
from tqdm.auto import tqdm
from sentence_transformers import util
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def get_vacancies(city, vacancy, page):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': f"{vacancy} {city}",
        'area': city,
        'per_page': 2,
        'page': page
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.771 YaBrowser/23.11.2.771 Yowser/2.5 Safari/537.36"
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()

# Функция для получения навыков вакансии
def get_vacancy_skills(vacancy_id, cursor):
    url = f'https://api.hh.ru/vacancies/{vacancy_id}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.771 YaBrowser/23.11.2.771 Yowser/2.5 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()
    skills = [skill['name'] for skill in data.get('key_skills', [])]
    # insert_skills_to_db(skills, cursor)
    return ', '.join(skills)

def insert_skills_to_db(skills, cursor):
    for skill_name in skills:
        check_query = """
            SELECT 1 FROM skills WHERE skill_name = %s LIMIT 1
        """

        cursor.execute(check_query, (skill_name,))
        existing_record = cursor.fetchone()

        if not existing_record:
            insert_query = """
                INSERT INTO skills 
                (skill_name) 
                VALUES (%s)
            """
            cursor.execute(insert_query, (skill_name,))

def parse_vacancies():
    cities = {
        'Москва': 1
    }

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port
    )

    with connection.cursor() as curr:
        for city, city_id in cities.items():
            curr.execute('''SELECT vacancy_name FROM vacancy_names''')
            resVacancies = curr.fetchall()
            for vacancy in resVacancies:
                print('________________________________')
                print(vacancy[0])
                print('________________________________')
                page = 0
                while True:
                    try:
                        data = get_vacancies(city_id, vacancy[0], page)
                        if not data.get('items'):
                            break
                        with connection.cursor() as cursor:
                            for item in data['items']:
                                # if vacancy.lower() not in item['name'].lower():
                                #     continue  # Пропустить, если название вакансии не совпадает                            
                                vacancy_name = f"{item['name']} ({city})"
                                vacancy_date = item['published_at']
                                vacancy_area = item['area'].get('name', '')
                                keywords = item['snippet'].get('requirement', '')
                                vac_skill_name = get_vacancy_skills(item['id'], cursor)
                                curr.execute('''SELECT skill_name FROM skills''')
                                resSkills = curr.fetchall() 
                                for dbSkill in resSkills:
                                    for vacSkill in vac_skill_name:
                                        skills_list = vac_skill_name.split(', ')  # Разбиваем строку на подстроки по запятой
                                        for skillT in skills_list:
                                            # print('Навык проверки - ', dbSkill)
                                            # print('Навык вакансии -', skillT) 
                                            question_embedding = model.encode(dbSkill)
                                            compare_embedding = model.encode(skillT)
                                            cosine_sim = util.pytorch_cos_sim(question_embedding, compare_embedding)
                                            # print('Процент совпадения - ', cosine_sim)
                                company = item['employer']['name']
                                salary = item['salary']
                                vacancy_schedule = item['schedule']['name']
                                if salary is None:
                                    salary = "з/п не указана"
                                else:
                                    salary_from = salary.get('from', '')
                                    salary_to = salary.get('to', '')
                                    salary_currency = salary.get('currency', '')
                                url = item['alternate_url']

                                print(f"Вакансия: {vacancy_name} Компания: {company}\nЗанятость: {vacancy_schedule}\nМестоположение: {vacancy_area}\nСсылка: {url}, \nКлючевые навыки: {vac_skill_name}")
                                # print(f"Заработная плата: от {salary_from} до {salary_to} {salary_currency}")
                                # print(f'Дата публикации вакансии: {vacancy_date}')
                                # print('____________________________________________')

                                # insert_query = """
                                #      INSERT INTO vacancy_name 
                                #      (vacancy_name) 
                                #      VALUES (%s)
                                #  """
                                # cursor.execute(insert_query,(vacancy_name,))
                            if page == 0:
                                break
                            # if page >= data['pages'] - 1:


                            # page += 1

                            # Задержка между запросами в пределах 1-2 секунд
                            time.sleep(random.uniform(1, 2))

                    except requests.HTTPError as e:
                        logging.error(f"Ошибка при обработке города {city}: {e}")
                        continue  # Перейти к следующему городу, если произошла ошибка

        connection.commit()

    print("Парсинг завершен. Данные сохранены в базе данных PostgreSQL.")

parse_vacancies()

















