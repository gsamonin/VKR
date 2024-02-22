import logging
import requests
import psycopg2
import time
import random

from config import host, user, password, database, port
from tqdm.auto import tqdm
from sentence_transformers import util
from sentence_transformers import SentenceTransformer



def db_get_cities():
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    cur.execute('SELECT id FROM cities')
    res = cur.fetchall()
    cur.close()
    con.close()
    return res

def db_get_vacancy_list():
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    cur.execute('SELECT vacancy_name FROM vacancies')
    res = cur.fetchall()
    cur.close()
    con.close()
    return res

def db_save_vacancy_info(vacancy_info, vacancy_id, vacancy_city):
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    query = """INSERT INTO vacancy_info (fk_vacancy, vacancy_date, vacancy_country, vacancy_city, 
    vacancy_salary_from, vacancy_salary_to, vacancy_currency, vacancy_gross, vacancy_gross,
      fk_vacancy_schedule) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cur.execute(query, (vacancy_id, vacancy_info))
    con.commit()
    cur.close()
    con.close()

def db_save_vacancy_skills(vacancy_id, skillList):
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    for skill_id in skillList:
        cur.execute('INSERT INTO vacancy_skills (fk_vacancy, fk_skills) VALUES(%s,%s)', (vacancy_id, skill_id))
    con.commit()
    cur.close()
    con.close()

def db_get_skills():
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    cur.execute('SELECT id, skill_name FROM skills')
    res = cur.fetchall()
    cur.close()
    con.close()
    return res