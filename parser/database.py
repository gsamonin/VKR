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
    cur.execute('SELECT vacancy_name FROM vacanciesЫ')
    res = cur.fetchall()
    cur.close()
    con.close()
    return res

def db_save_vacancy_info():
    pass

def db_save_vacancy_skills():
    pass

def db_get_skills():
    pass