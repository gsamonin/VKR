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

def db_get_vacancy_skills_top10():
    con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    cur = con.cursor()
    cur.execute('''select s.skill_name, vs.fk_skills, count(vs.fk_skills) kolvo  
                    from vacancy_skills vs 
                    join skills s 
	                on s.id = vs.fk_skills  
                    group by vs.fk_skills, s.skill_name 
                    order by count(vs.fk_skills) desc
                    limit 10 ''')
    res = cur.fetchall()
    cur.close()
    con.close()
    vacancySkills = []
    for r in res:
        vacancySkills.append(list(r))
    return vacancySkills

def db_get_vacancy_top5(id):
    con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    cur = con.cursor()
    cur.execute('''select vi.fk_vacancy, v.vacancy_name, count(vi.fk_vacancy) kolvo 
                    from vacancy_info vi 
                    join vacancies v 
	                    on v.id = vi.fk_vacancy 
                    group by vi.fk_vacancy, v.vacancy_name 
                    order by kolvo DESC
                    limit 5 ''')
    res = cur.fetchall()
    cur.close()
    con.close()
    vacancies = []
    for r in res:
        vacancies.append(list(r))
    return vacancies
