import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "postgres" 
database = "vacancysanalize"
port = "5432"


def db_get_cities():
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    cur.execute('SELECT * FROM cities')
    res = cur.fetchall()
    cur.close()
    con.close()
    return res

def db_get_vacancy_list():
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    cur.execute('SELECT * FROM vacancies')
    res = cur.fetchall()
    cur.close()
    con.close()
    return res

def db_save_vacancy_info(vacancy_info, vacancy_id, vacancy_city):
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    query = """INSERT INTO vacancy_info (id, fk_vacancy, vacancy_date, vacancy_country, fk_vacancy_city, 
    vacancy_salary_from, vacancy_salary_to, vacancy_currency, vacancy_gross) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (id) DO NOTHING"""
    sf = -1; st = -1; currency = ''; gross = None
    if vacancy_info['salary'] is not None:
        sf = vacancy_info['salary']['from']
        st = vacancy_info['salary']['to']
        currency = vacancy_info['salary']['currency']
        gross = vacancy_info['salary']['gross']
    cur.execute(query, (vacancy_info['id'], vacancy_id, vacancy_info['published_at'], vacancy_info['area']['name'], vacancy_city, sf, st, currency, gross))
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
    cur.execute('SELECT * FROM skills')
    res = cur.fetchall()
    cur.close()
    con.close()
    return res

def db_get_vacancy_info(name):
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    cur.execute('SELECT id FROM vacancies WHERE vacancy_name=%s', (name,))
    res = cur.fetchone()
    cur.close()
    con.close()
    return res

def db_save_programms(programm):
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    try:
        programmName = programm.find('h2', class_='list__h').find('a').text
        programmPaid = int(programm.find('span', class_='visible-mid', string=['Платных мест 2024', 'Платных мест 2023', 'Платных мест 0']).find_next().text.lstrip().replace(' ', ''))
        programmFree = int(programm.find('span', class_='visible-mid', string=['Бюджетных мест 2024', 'Бюджетных мест 2023', 'Бюджетных мест 0']).find_next().text.lstrip().replace(' ', ''))
        cur.execute('INSERT INTO programms (programm_name, programm_count_free, programm_count_paid) VALUES(%s,%s,%s)', (programmName, programmFree, programmPaid)) 
    except Exception:
        pass
    con.commit() 
    cur.close()
    con.close()
    
def db_save_courses(course):
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    try:
        course_name = course.find('div', class_='style_heading__WaLQK style_headingTopPadding__sB1tl _ptw42j').string
        organization_name = course.find('img', class_='style_logo__r1hDN style_logoBorder__xa_Xd').get('title')
        price = int(course.find('div', class_='style_price__vSy5p').find('span', class_='style_nowrap__12nI5 _1qco5vz _18gj9po').text.lstrip().replace(u'\xa0', '').replace('₽', ''))
        rating = float(course.find('span', class_='style_wrapper__Q5XQE').find('span', class_='').text)
        cur.execute('INSERT INTO courses (course_name, fk_vacancy, course_org, course_price, course_rating) VALUES(%s,%s,%s,%s,%s)', (course_name, 1, organization_name, price, rating)) 
        con.commit()
    except Exception as e:
        print(e)
    # con.commit() 
    cur.close()
    con.close()