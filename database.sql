DO $$ DECLARE
r RECORD;
BEGIN
-- if the schema you operate on is not "public", you must change "public" to your schema name
FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
EXECUTE 'DROP TABLE IF EXISTS public.' || quote_ident(r.tablename) || ' CASCADE';
END LOOP;
END $$;

CREATE table schedule(
    id serial4 NOT NULL PRIMARY KEY,
    schedule_name varchar(50)
);

CREATE table vacancy_name(
    id serial4 NOT NULL PRIMARY KEY,
    vacancy_name varchar
);

CREATE table vacancies(
    id bigserial NOT NULL PRIMARY KEY,
    fk_vacancy_name serial4,
    vacancy_date date, 
    vacancy_country varchar(30),
    vacancy_city varchar(100),
    vacancy_salary_from int,
    vacancy_salary_to int,
    vacancy_currency varchar(5),
    vacancy_gross boolean,
    fk_vacancy_schedule serial4,
    FOREIGN KEY (fk_vacancy_schedule) REFERENCES schedule (id),
    FOREIGN KEY (fk_vacancy_name) REFERENCES vacancy_name (id)
);

CREATE table skills(
    id serial4 NOT NULL PRIMARY KEY,
    skill_name varchar(100)
);

CREATE table vacancy_skills(
    id serial4 NOT NULL PRIMARY KEY,
    fk_vacancy serial4,
    fk_skills serial4,
    FOREIGN KEY (fk_vacancy) REFERENCES vacancies (id),
    FOREIGN KEY (fk_skills) REFERENCES skills (id)
);
