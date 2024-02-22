import requests
import time
import random
from database import *
from sentence_transformers import util
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

def get_vacancies(city, vacancy, page):
    params = {'text': f"{vacancy} {city}", 'area': city, 'per_page': 2, 'page': page}
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    return response.json()

def process_vacancy_skills(vacancy_id):
    response = requests.get(f'https://api.hh.ru/vacancies/{vacancy_id}')
    data = response.json()
    done_list = []
    for vacancy_skill in data['key_skills']:
        for skill in db_get_skills():
            skill_embedding = model.encode(vacancy_skill['name'])
            compare_skill_embedding = model.encode(skill[1])
            cosine_sim = util.pytorch_cos_sim(skill_embedding, compare_skill_embedding)
            if cosine_sim >= 0.8:
                done_list.append(skill[0])
    db_save_vacancy_skills(vacancy_id, done_list)


def parse_vacancies():
    for city_id in db_get_cities():
        for vacancy in db_get_vacancy_list():
            page = 0
            try:
                while True:
                    data = get_vacancies(city_id, vacancy[0], page)
                    if not data.get('items'):
                            break
                    for item in data['items']:
                        db_save_vacancy_info(item)
                        process_vacancy_skills(item['id'])
                    page+=1
                    time.sleep(random.uniform(1, 2))
            except Exception:
                pass
    #     cur.execute('''SELECT vacancy_name FROM vacancies'''))
    #     vacancies = cur.fetchall()
    #     for vacancy in vacancies:
    #         page = 0
    #         try:
    #             data = get_vacancies(city_id, vacancy[0], page)
    #             for item in data['items']:
    #                 cur.execute('INSERT INTO vacanciesInfo (fk_vacancy, vacancy_date, vacancy_country, vacancy_city, vacancy_salary_from, vacancy_salary_to, vacancy_currency, vacancy_gross, fk_vacancy_schedule)')
    #             while True:
    #                 try:
    #                     data = get_vacancies(city_id, vacancy[0], page)
    #                     if not data.get('items'):
    #                         break
    #                     with connection.cursor() as cursor:
    #                         for item in data['items']:
    #                             # if vacancy.lower() not in item['name'].lower():
    #                             #     continue  # Пропустить, если название вакансии не совпадает                            
    #                             vacancy_name = f"{item['name']} ({city})"
    #                             vacancy_date = item['published_at']
    #                             vacancy_area = item['area'].get('name', '')
    #                             keywords = item['snippet'].get('requirement', '')
    #                             vac_skill_name = get_vacancy_skills(item['id'], cursor)
    #                             curr.execute('''SELECT skill_name FROM skills''')
    #                             resSkills = curr.fetchall() 
    #                             for dbSkill in resSkills:
    #                                 for vacSkill in vac_skill_name:
    #                                     skills_list = vac_skill_name.split(', ')  # Разбиваем строку на подстроки по запятой
    #                                     for skillT in skills_list:
    #                                         # print('Навык проверки - ', dbSkill)
    #                                         # print('Навык вакансии -', skillT) 
    #                                         question_embedding = model.encode(dbSkill)
    #                                         compare_embedding = model.encode(skillT)
    #                                         cosine_sim = util.pytorch_cos_sim(question_embedding, compare_embedding)
    #                                         # print('Процент совпадения - ', cosine_sim)
    #                             company = item['employer']['name']
    #                             salary = item['salary']
    #                             vacancy_schedule = item['schedule']['name']
    #                             if salary is None:
    #                                 salary = "з/п не указана"
    #                             else:
    #                                 salary_from = salary.get('from', '')
    #                                 salary_to = salary.get('to', '')
    #                                 salary_currency = salary.get('currency', '')
    #                             url = item['alternate_url']

    #                             print(f"Вакансия: {vacancy_name} Компания: {company}\nЗанятость: {vacancy_schedule}\nМестоположение: {vacancy_area}\nСсылка: {url}, \nКлючевые навыки: {vac_skill_name}")
    #                             # print(f"Заработная плата: от {salary_from} до {salary_to} {salary_currency}")
    #                             # print(f'Дата публикации вакансии: {vacancy_date}')
    #                             # print('____________________________________________')

    #                             # insert_query = """
    #                             #      INSERT INTO vacancy_name 
    #                             #      (vacancy_name) 
    #                             #      VALUES (%s)
    #                             #  """
    #                             # cursor.execute(insert_query,(vacancy_name,))
    #                         if page == 0:
    #                             break
    #                         # if page >= data['pages'] - 1:


    #                         # page += 1

    #                         # Задержка между запросами в пределах 1-2 секунд
    #                         time.sleep(random.uniform(1, 2))

    #                 except requests.HTTPError as e:
    #                     logging.error(f"Ошибка при обработке города {city}: {e}")
    #                     continue  # Перейти к следующему городу, если произошла ошибка

    #     connection.commit()

    # print("Парсинг завершен. Данные сохранены в базе данных PostgreSQL.")

parse_vacancies()

















