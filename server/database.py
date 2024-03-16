import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "postgres" 
database = "vacancysanalize"
port = "5432"

def db_get_vacancy_id(name):
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    cur.execute('SELECT id FROM vacancies WHERE vacancy_name=%s', (name,))
    res = cur.fetchone()
    cur.close()
    con.close()
    return res

def db_get_vacancy_info(id):
    con = psycopg2.connect(host=host, user=user, password=password, database=database,port=port)
    cur = con.cursor()
    cur.execute('SELECT * FROM vacancy_info WHERE fk_vacancy=%s', (id,))
    res = cur.fetchone()
    cur.close()
    con.close()
    return res



