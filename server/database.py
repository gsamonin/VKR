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

def dbGetAvgSallaryAndVac():
    con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    cur = con.cursor()
    cur.execute('''select v.vacancy_name, count(vi.fk_vacancy), round(avg(vi.vacancy_salary_from), 0) from vacancies v 
                    join vacancy_info vi on v.id = vi.fk_vacancy 
                    where vi.vacancy_salary_from  in (select vacancy_salary_from from vacancy_info vi2 where vacancy_salary_from > 1000 and vacancy_currency = 'RUR' )
                    group by v.vacancy_name, vi.fk_vacancy ''')
    res = cur.fetchall()
    cur.close()
    con.close()
    avgSallaryVac = []
    for r in res:
        avgSallaryVac.append(list(r))
    return avgSallaryVac


def dbGetSkillsByVac(id):
    con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    cur = con.cursor()
    cur.execute('''select count(s.skill_name) kolvo, s.skill_name  from vacancy_info vi 
                    join vacancy_skills vs on vs.fk_vacancy = vi.id
                    join skills s on s.id = vs.fk_skills 
                    join vacancies v on v.id = vi.fk_vacancy 
                    where vi.fk_vacancy = %s
                    group by s.skill_name, v.vacancy_name
                    order by kolvo desc 
                    limit 10''', (id,))
    res = cur.fetchall()
    cur.close()
    con.close()
    skillsByVac = []
    for r in res:
        skillsByVac.append(list(r))
    return skillsByVac

def dbGetSallaryInDiagVac(id):
    con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    cur = con.cursor()
    cur.execute('''select round(min(vi.vacancy_salary_from), 0) as ot, round(max(vi.vacancy_salary_to), 0) as doo, avg(vacancy_salary_to - vi.vacancy_salary_from) as sred from vacancy_info vi  
                where vi.fk_vacancy = %s and vacancy_currency = 'RUR' and vacancy_salary_from > 100 and vacancy_salary_to > 100
                group by fk_vacancy''', (id,))
    res = cur.fetchall()
    cur.close()
    con.close()
    sallByVac = []
    for r in res:
        sallByVac.append(list(r))
    return sallByVac 

def dbGetCourses(id):
    con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    cur = con.cursor()
    cur.execute('''select c.course_name, c.course_org, c.course_price, c.course_rating  from courses c 
                where fk_vacancy = %s''', (id,))
    res = cur.fetchall()
    cur.close()
    con.close()
    coursesByVac = []
    for r in res:
        coursesByVac.append(list(r))
    return coursesByVac 

def dbGetCitiesByVac(id):
    con = psycopg2.connect(host=host, user=user, password=password, database=database, port=port)
    cur = con.cursor()
    cur.execute('''select vi.fk_vacancy, count(vi.fk_vacancy_city), c.city_name  from vacancy_info vi 
                    join cities c on vi.fk_vacancy_city = c.id 
                    where fk_vacancy = %s
                    group by vi.fk_vacancy, c.city_name 
                    order by vi.fk_vacancy ''', (id,))
    res = cur.fetchall()
    cur.close()
    con.close()
    citiesByVac = []
    for r in res:
        citiesByVac.append(list(r))
    return citiesByVac 