DO $$ DECLARE
r RECORD;
BEGIN
-- if the schema you operate on is not "public", you must change "public" to your schema name
FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
EXECUTE 'DROP TABLE IF EXISTS public.' || quote_ident(r.tablename) || ' CASCADE';
END LOOP;
END $$;


CREATE table cities(
    id serial4 NOT NULL PRIMARY KEY,
    city_name varchar
);

CREATE table vacancies(
    id serial4 NOT NULL PRIMARY KEY,
    vacancy_name varchar
);

CREATE table vacancy_info(
    id bigserial NOT NULL PRIMARY KEY,
    fk_vacancy serial4,
    vacancy_date date, 
    vacancy_country varchar(30),
    fk_vacancy_city serial4,
    vacancy_salary_from int,
    vacancy_salary_to int,
    vacancy_currency varchar(5),
    vacancy_gross boolean,
    FOREIGN KEY (fk_vacancy_city) REFERENCES cities (id),
    FOREIGN KEY (fk_vacancy) REFERENCES vacancies (id)
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

-----------------------------------------------------

INSERT INTO public.cities
(id, city_name)
VALUES(1, 'Москва');

INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(1, 'Python');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(2, 'Python Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(3, 'Python Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(4, 'Python Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(5, 'Java ');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(6, 'Java Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(7, 'Java Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(8, 'Java Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(9, 'C++');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(10, 'C++ Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(11, 'C++ Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(12, 'C++ Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(13, 'Golang');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(14, 'Golang Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(15, 'Golang Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(16, 'Golang Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(17, '1C ');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(18, '1C Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(19, '1C Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(20, '1C Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(21, 'Ruby');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(22, 'Ruby Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(23, 'Ruby Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(24, 'Ruby Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(25, 'C#');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(45, 'C# Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(46, 'C# Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(47, 'C# Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(48, 'Swift');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(49, 'Swift Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(50, 'Swift Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(51, 'Swift Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(52, 'PHP');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(53, 'PHP Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(54, 'PHP Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(55, 'PHP Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(56, 'Android');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(57, 'Android Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(58, 'Android Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(59, 'Android Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(60, 'Frontend');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(61, 'Frontend Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(62, 'Frontend Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(63, 'Frontend Senior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(64, 'Backend');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(65, 'Backend Junior');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(66, 'Backend Middle');
INSERT INTO public.vacancies
(id, vacancy_name)
VALUES(67, 'Backend Senior');

INSERT INTO public.skills
(id, skill_name)
VALUES(5267, '1С');
INSERT INTO public.skills
(id, skill_name)
VALUES(5432, 'A/B тесты');
INSERT INTO public.skills
(id, skill_name)
VALUES(4828, 'API');
INSERT INTO public.skills
(id, skill_name)
VALUES(4860, 'AWS');
INSERT INTO public.skills
(id, skill_name)
VALUES(5430, 'Active Directory');
INSERT INTO public.skills
(id, skill_name)
VALUES(4850, 'ActiveAdmin');
INSERT INTO public.skills
(id, skill_name)
VALUES(5490, 'Ad Hoc Analysis');
INSERT INTO public.skills
(id, skill_name)
VALUES(5463, 'Agile Project Management');
INSERT INTO public.skills
(id, skill_name)
VALUES(5499, 'Airflow');
INSERT INTO public.skills
(id, skill_name)
VALUES(4886, 'Ajax');
INSERT INTO public.skills
(id, skill_name)
VALUES(5523, 'Allure');
INSERT INTO public.skills
(id, skill_name)
VALUES(5448, 'Android');
INSERT INTO public.skills
(id, skill_name)
VALUES(5447, 'Android Studio');
INSERT INTO public.skills
(id, skill_name)
VALUES(5385, 'Angular');
INSERT INTO public.skills
(id, skill_name)
VALUES(5414, 'Ansible');
INSERT INTO public.skills
(id, skill_name)
VALUES(5561, 'Apache HTTP Server');
INSERT INTO public.skills
(id, skill_name)
VALUES(5489, 'Apache Superset');
INSERT INTO public.skills
(id, skill_name)
VALUES(5459, 'Atlassian Confluence');
INSERT INTO public.skills
(id, skill_name)
VALUES(5458, 'Atlassian Jira');
INSERT INTO public.skills
(id, skill_name)
VALUES(4883, 'Automation QA');
INSERT INTO public.skills
(id, skill_name)
VALUES(5426, 'BI');
INSERT INTO public.skills
(id, skill_name)
VALUES(5406, 'Backend');
INSERT INTO public.skills
(id, skill_name)
VALUES(4842, 'Bash');
INSERT INTO public.skills
(id, skill_name)
VALUES(5509, 'Big Data');
INSERT INTO public.skills
(id, skill_name)
VALUES(5556, 'Bugzilla');
INSERT INTO public.skills
(id, skill_name)
VALUES(5422, 'Business Intelligence Systems');
INSERT INTO public.skills
(id, skill_name)
VALUES(5609, 'C');
INSERT INTO public.skills
(id, skill_name)
VALUES(5428, 'C#');
INSERT INTO public.skills
(id, skill_name)
VALUES(5382, 'C++');
INSERT INTO public.skills
(id, skill_name)
VALUES(5542, 'CAD');
INSERT INTO public.skills
(id, skill_name)
VALUES(5543, 'CAE');
INSERT INTO public.skills
(id, skill_name)
VALUES(4832, 'CI/CD');
INSERT INTO public.skills
(id, skill_name)
VALUES(5581, 'CMS Bitrix');
INSERT INTO public.skills
(id, skill_name)
VALUES(4829, 'CSS');
INSERT INTO public.skills
(id, skill_name)
VALUES(5273, 'Celery');
INSERT INTO public.skills
(id, skill_name)
VALUES(5417, 'CentOS');
INSERT INTO public.skills
(id, skill_name)
VALUES(5416, 'Ceph');
INSERT INTO public.skills
(id, skill_name)
VALUES(5445, 'Charles');
INSERT INTO public.skills
(id, skill_name)
VALUES(5519, 'Chef');
INSERT INTO public.skills
(id, skill_name)
VALUES(5606, 'ClearML');
INSERT INTO public.skills
(id, skill_name)
VALUES(4879, 'ClickHouse');
INSERT INTO public.skills
(id, skill_name)
VALUES(5544, 'Computational Geometry');
INSERT INTO public.skills
(id, skill_name)
VALUES(5420, 'Continuous Integration');
INSERT INTO public.skills
(id, skill_name)
VALUES(5514, 'DBT');
INSERT INTO public.skills
(id, skill_name)
VALUES(5582, 'DBus');
INSERT INTO public.skills
(id, skill_name)
VALUES(5560, 'DHCP');
INSERT INTO public.skills
(id, skill_name)
VALUES(5546, 'DRC');
INSERT INTO public.skills
(id, skill_name)
VALUES(5511, 'DWH');
INSERT INTO public.skills
(id, skill_name)
VALUES(5341, 'Data Analysis');
INSERT INTO public.skills
(id, skill_name)
VALUES(5608, 'Data Science');
INSERT INTO public.skills
(id, skill_name)
VALUES(5522, 'Debezium');
INSERT INTO public.skills
(id, skill_name)
VALUES(5418, 'Debian');
INSERT INTO public.skills
(id, skill_name)
VALUES(5329, 'DevOps');
INSERT INTO public.skills
(id, skill_name)
VALUES(5460, 'DevTools');
INSERT INTO public.skills
(id, skill_name)
VALUES(5533, 'Django');
INSERT INTO public.skills
(id, skill_name)
VALUES(5269, 'Django Framework');
INSERT INTO public.skills
(id, skill_name)
VALUES(4848, 'Docker');
INSERT INTO public.skills
(id, skill_name)
VALUES(5469, 'Docker-swarm');
INSERT INTO public.skills
(id, skill_name)
VALUES(5541, 'EDA');
INSERT INTO public.skills
(id, skill_name)
VALUES(5424, 'ETL');
INSERT INTO public.skills
(id, skill_name)
VALUES(5274, 'Elastic search');
INSERT INTO public.skills
(id, skill_name)
VALUES(5309, 'FastApi');
INSERT INTO public.skills
(id, skill_name)
VALUES(5446, 'Fiddler');
INSERT INTO public.skills
(id, skill_name)
VALUES(5415, 'Foreman');
INSERT INTO public.skills
(id, skill_name)
VALUES(5393, 'GRC');
INSERT INTO public.skills
(id, skill_name)
VALUES(4830, 'Git');
INSERT INTO public.skills
(id, skill_name)
VALUES(4836, 'Gitlab');
INSERT INTO public.skills
(id, skill_name)
VALUES(4837, 'Golang');
INSERT INTO public.skills
(id, skill_name)
VALUES(5503, 'Google Analytics');
INSERT INTO public.skills
(id, skill_name)
VALUES(4862, 'Google Cloud');
INSERT INTO public.skills
(id, skill_name)
VALUES(5332, 'Grafana');
INSERT INTO public.skills
(id, skill_name)
VALUES(5494, 'Grails');
INSERT INTO public.skills
(id, skill_name)
VALUES(4846, 'Grape');
INSERT INTO public.skills
(id, skill_name)
VALUES(5515, 'GreenPlum');
INSERT INTO public.skills
(id, skill_name)
VALUES(4833, 'HTML');
INSERT INTO public.skills
(id, skill_name)
VALUES(5500, 'Hadoop');
INSERT INTO public.skills
(id, skill_name)
VALUES(4845, 'Hanami');
INSERT INTO public.skills
(id, skill_name)
VALUES(5564, 'Helpdesk');
INSERT INTO public.skills
(id, skill_name)
VALUES(5573, 'Hyper-V');
INSERT INTO public.skills
(id, skill_name)
VALUES(5596, 'IBM Cognos Analytics');
INSERT INTO public.skills
(id, skill_name)
VALUES(5597, 'IBM Cognos BI');
INSERT INTO public.skills
(id, skill_name)
VALUES(5595, 'IBM Cognos TM1');
INSERT INTO public.skills
(id, skill_name)
VALUES(5513, 'IBM DataStage');
INSERT INTO public.skills
(id, skill_name)
VALUES(5594, 'IBM Planning Analytics');
INSERT INTO public.skills
(id, skill_name)
VALUES(5508, 'IDE Visual Studio');
INSERT INTO public.skills
(id, skill_name)
VALUES(5391, 'IRP');
INSERT INTO public.skills
(id, skill_name)
VALUES(5485, 'IT Recruitment');
INSERT INTO public.skills
(id, skill_name)
VALUES(5376, 'Information Security');
INSERT INTO public.skills
(id, skill_name)
VALUES(5452, 'Insomnia');
INSERT INTO public.skills
(id, skill_name)
VALUES(4887, 'JSON');
INSERT INTO public.skills
(id, skill_name)
VALUES(5456, 'Java');
INSERT INTO public.skills
(id, skill_name)
VALUES(4826, 'JavaScript');
INSERT INTO public.skills
(id, skill_name)
VALUES(5429, 'Jira');
INSERT INTO public.skills
(id, skill_name)
VALUES(5517, 'Jmeter');
INSERT INTO public.skills
(id, skill_name)
VALUES(5412, 'KVM');
INSERT INTO public.skills
(id, skill_name)
VALUES(5512, 'Kafka');
INSERT INTO public.skills
(id, skill_name)
VALUES(4864, 'Keycloak');
INSERT INTO public.skills
(id, skill_name)
VALUES(5307, 'Kibana');
INSERT INTO public.skills
(id, skill_name)
VALUES(4865, 'Kong API Gateway');
INSERT INTO public.skills
(id, skill_name)
VALUES(4857, 'Kubernetes');
INSERT INTO public.skills
(id, skill_name)
VALUES(5363, 'LAN');
INSERT INTO public.skills
(id, skill_name)
VALUES(5547, 'LVS');
INSERT INTO public.skills
(id, skill_name)
VALUES(5577, 'Laravel');
INSERT INTO public.skills
(id, skill_name)
VALUES(4843, 'Linux');
INSERT INTO public.skills
(id, skill_name)
VALUES(5501, 'MATLAB');
INSERT INTO public.skills
(id, skill_name)
VALUES(5592, 'MDX');
INSERT INTO public.skills
(id, skill_name)
VALUES(5311, 'ML');
INSERT INTO public.skills
(id, skill_name)
VALUES(5607, 'MLOps');
INSERT INTO public.skills
(id, skill_name)
VALUES(5605, 'MLflow');
INSERT INTO public.skills
(id, skill_name)
VALUES(5535, 'MS Access');
INSERT INTO public.skills
(id, skill_name)
VALUES(5326, 'MS Excel');
INSERT INTO public.skills
(id, skill_name)
VALUES(5574, 'MS Exchange');
INSERT INTO public.skills
(id, skill_name)
VALUES(5536, 'MS Outlook');
INSERT INTO public.skills
(id, skill_name)
VALUES(5325, 'MS Power BI');
INSERT INTO public.skills
(id, skill_name)
VALUES(5346, 'MS PowerPoint');
INSERT INTO public.skills
(id, skill_name)
VALUES(5335, 'MS SQL');
INSERT INTO public.skills
(id, skill_name)
VALUES(5537, 'MS SQL Server');
INSERT INTO public.skills
(id, skill_name)
VALUES(5297, 'MS Visio');
INSERT INTO public.skills
(id, skill_name)
VALUES(5352, 'MS Visual Studio');
INSERT INTO public.skills
(id, skill_name)
VALUES(5601, 'MS Word');
INSERT INTO public.skills
(id, skill_name)
VALUES(5402, 'MSSQL');
INSERT INTO public.skills
(id, skill_name)
VALUES(5312, 'Machine Learning');
INSERT INTO public.skills
(id, skill_name)
VALUES(5468, 'Manticore Search');
INSERT INTO public.skills
(id, skill_name)
VALUES(4884, 'Manual QA');
INSERT INTO public.skills
(id, skill_name)
VALUES(5451, 'Manual testing');
INSERT INTO public.skills
(id, skill_name)
VALUES(5467, 'MariaDB');
INSERT INTO public.skills
(id, skill_name)
VALUES(5529, 'Mathematical Statistics');
INSERT INTO public.skills
(id, skill_name)
VALUES(5481, 'Media Planning');
INSERT INTO public.skills
(id, skill_name)
VALUES(5403, 'Memcached');
INSERT INTO public.skills
(id, skill_name)
VALUES(5386, 'Microsoft .NET');
INSERT INTO public.skills
(id, skill_name)
VALUES(4827, 'MongoDB');
INSERT INTO public.skills
(id, skill_name)
VALUES(4870, 'MySQL');
INSERT INTO public.skills
(id, skill_name)
VALUES(5333, 'Nginx');
INSERT INTO public.skills
(id, skill_name)
VALUES(5405, 'NoSQL');
INSERT INTO public.skills
(id, skill_name)
VALUES(5578, 'Node.js');
INSERT INTO public.skills
(id, skill_name)
VALUES(5317, 'Numpy');
INSERT INTO public.skills
(id, skill_name)
VALUES(5593, 'OLAP');
INSERT INTO public.skills
(id, skill_name)
VALUES(5549, 'ORACLE');
INSERT INTO public.skills
(id, skill_name)
VALUES(5534, 'Oracle Pl/SQL');
INSERT INTO public.skills
(id, skill_name)
VALUES(5351, 'PHP');
INSERT INTO public.skills
(id, skill_name)
VALUES(5384, 'PPC');
INSERT INTO public.skills
(id, skill_name)
VALUES(5413, 'PXE');
INSERT INTO public.skills
(id, skill_name)
VALUES(5318, 'Pandas');
INSERT INTO public.skills
(id, skill_name)
VALUES(5400, 'Perl');
INSERT INTO public.skills
(id, skill_name)
VALUES(5470, 'Portainer');
INSERT INTO public.skills
(id, skill_name)
VALUES(4825, 'PostgreSQL');
INSERT INTO public.skills
(id, skill_name)
VALUES(5302, 'Postman');
INSERT INTO public.skills
(id, skill_name)
VALUES(5334, 'Power BI');
INSERT INTO public.skills
(id, skill_name)
VALUES(5338, 'Power Pivot');
INSERT INTO public.skills
(id, skill_name)
VALUES(5337, 'Power Query');
INSERT INTO public.skills
(id, skill_name)
VALUES(5350, 'PowerBI');
INSERT INTO public.skills
(id, skill_name)
VALUES(5361, 'PowerShell');
INSERT INTO public.skills
(id, skill_name)
VALUES(4881, 'Prometheus');
INSERT INTO public.skills
(id, skill_name)
VALUES(5527, 'Pytest');
INSERT INTO public.skills
(id, skill_name)
VALUES(4838, 'Python');
INSERT INTO public.skills
(id, skill_name)
VALUES(5444, 'QA');
INSERT INTO public.skills
(id, skill_name)
VALUES(5518, 'Qt');
INSERT INTO public.skills
(id, skill_name)
VALUES(5538, 'R');
INSERT INTO public.skills
(id, skill_name)
VALUES(5580, 'REST');
INSERT INTO public.skills
(id, skill_name)
VALUES(5484, 'RESTful API');
INSERT INTO public.skills
(id, skill_name)
VALUES(4831, 'RSpec');
INSERT INTO public.skills
(id, skill_name)
VALUES(4849, 'RabbitMQ');
INSERT INTO public.skills
(id, skill_name)
VALUES(5321, 'React');
INSERT INTO public.skills
(id, skill_name)
VALUES(5493, 'ReactJS');
INSERT INTO public.skills
(id, skill_name)
VALUES(5486, 'Recruitment');
INSERT INTO public.skills
(id, skill_name)
VALUES(5524, 'RedOs');
INSERT INTO public.skills
(id, skill_name)
VALUES(4835, 'Redis');
INSERT INTO public.skills
(id, skill_name)
VALUES(5322, 'Redux');
INSERT INTO public.skills
(id, skill_name)
VALUES(4875, 'Rubocop');
INSERT INTO public.skills
(id, skill_name)
VALUES(4822, 'Ruby');
INSERT INTO public.skills
(id, skill_name)
VALUES(5383, 'SEO');
INSERT INTO public.skills
(id, skill_name)
VALUES(5389, 'SIEM');
INSERT INTO public.skills
(id, skill_name)
VALUES(5367, 'SIEm');
INSERT INTO public.skills
(id, skill_name)
VALUES(5392, 'SOAR');
INSERT INTO public.skills
(id, skill_name)
VALUES(5375, 'SOC');
INSERT INTO public.skills
(id, skill_name)
VALUES(5497, 'SOLID');
INSERT INTO public.skills
(id, skill_name)
VALUES(4852, 'SQL');
INSERT INTO public.skills
(id, skill_name)
VALUES(5443, 'SQLite');
INSERT INTO public.skills
(id, skill_name)
VALUES(5354, 'STL');
INSERT INTO public.skills
(id, skill_name)
VALUES(4878, 'SaaS');
INSERT INTO public.skills
(id, skill_name)
VALUES(5559, 'Samba');
INSERT INTO public.skills
(id, skill_name)
VALUES(5320, 'Scikit-learn');
INSERT INTO public.skills
(id, skill_name)
VALUES(5449, 'Scrum');
INSERT INTO public.skills
(id, skill_name)
VALUES(5388, 'SecurityVision');
INSERT INTO public.skills
(id, skill_name)
VALUES(5550, 'Selenium IDE');
INSERT INTO public.skills
(id, skill_name)
VALUES(5399, 'Shell');
INSERT INTO public.skills
(id, skill_name)
VALUES(4834, 'Sidekiq');
INSERT INTO public.skills
(id, skill_name)
VALUES(4844, 'Sinatra');
INSERT INTO public.skills
(id, skill_name)
VALUES(4877, 'Solid Edge');
INSERT INTO public.skills
(id, skill_name)
VALUES(5488, 'Sourcing');
INSERT INTO public.skills
(id, skill_name)
VALUES(5510, 'Spark');
INSERT INTO public.skills
(id, skill_name)
VALUES(5408, 'Sphinx');
INSERT INTO public.skills
(id, skill_name)
VALUES(5398, 'Sybase');
INSERT INTO public.skills
(id, skill_name)
VALUES(5576, 'Symfony');
INSERT INTO public.skills
(id, skill_name)
VALUES(5565, 'TCP/IP');
INSERT INTO public.skills
(id, skill_name)
VALUES(5496, 'TDD');
INSERT INTO public.skills
(id, skill_name)
VALUES(5349, 'Tableau');
INSERT INTO public.skills
(id, skill_name)
VALUES(4859, 'Team City');
INSERT INTO public.skills
(id, skill_name)
VALUES(4869, 'Teamleading');
INSERT INTO public.skills
(id, skill_name)
VALUES(4868, 'TechLead');
INSERT INTO public.skills
(id, skill_name)
VALUES(5521, 'Terraform');
INSERT INTO public.skills
(id, skill_name)
VALUES(5304, 'Test case');
INSERT INTO public.skills
(id, skill_name)
VALUES(5551, 'TestComplete');
INSERT INTO public.skills
(id, skill_name)
VALUES(5340, 'Think-cell');
INSERT INTO public.skills
(id, skill_name)
VALUES(4863, 'Trailblazer');
INSERT INTO public.skills
(id, skill_name)
VALUES(5323, 'TypeScript');
INSERT INTO public.skills
(id, skill_name)
VALUES(5441, 'UI');
INSERT INTO public.skills
(id, skill_name)
VALUES(5313, 'UML');
INSERT INTO public.skills
(id, skill_name)
VALUES(5442, 'UX');
INSERT INTO public.skills
(id, skill_name)
VALUES(5331, 'Ubuntu');
INSERT INTO public.skills
(id, skill_name)
VALUES(5558, 'Ubuntu Server');
INSERT INTO public.skills
(id, skill_name)
VALUES(5268, 'Unit Testing');
INSERT INTO public.skills
(id, skill_name)
VALUES(5293, 'Unity');
INSERT INTO public.skills
(id, skill_name)
VALUES(4873, 'Unix');
INSERT INTO public.skills
(id, skill_name)
VALUES(5419, 'Unix Shell Scripts');
INSERT INTO public.skills
(id, skill_name)
VALUES(5336, 'VBA');
INSERT INTO public.skills
(id, skill_name)
VALUES(5294, 'Vue.js');
INSERT INTO public.skills
(id, skill_name)
VALUES(5380, 'Windows Forms');
INSERT INTO public.skills
(id, skill_name)
VALUES(5427, 'Windows Server');
INSERT INTO public.skills
(id, skill_name)
VALUES(5308, 'XML');
INSERT INTO public.skills
(id, skill_name)
VALUES(5401, 'XSLT');
INSERT INTO public.skills
(id, skill_name)
VALUES(5520, 'Zabbix');
INSERT INTO public.skills
(id, skill_name)
VALUES(5505, 'afl++');
INSERT INTO public.skills
(id, skill_name)
VALUES(5407, 'amoCRM');
INSERT INTO public.skills
(id, skill_name)
VALUES(4880, 'dry-rb');
INSERT INTO public.skills
(id, skill_name)
VALUES(5455, 'e2e тесты');
INSERT INTO public.skills
(id, skill_name)
VALUES(5532, 'fastapi');
INSERT INTO public.skills
(id, skill_name)
VALUES(5504, 'jsfuzz');
INSERT INTO public.skills
(id, skill_name)
VALUES(5507, 'libfuzzer');
INSERT INTO public.skills
(id, skill_name)
VALUES(5585, 'openssl');
INSERT INTO public.skills
(id, skill_name)
VALUES(5584, 'rpm');
INSERT INTO public.skills
(id, skill_name)
VALUES(5371, 'sgrc');
INSERT INTO public.skills
(id, skill_name)
VALUES(4882, 'sneakers');
INSERT INTO public.skills
(id, skill_name)
VALUES(5370, 'soar');
INSERT INTO public.skills
(id, skill_name)
VALUES(5366, 'soc');
INSERT INTO public.skills
(id, skill_name)
VALUES(5583, 'systemd');
INSERT INTO public.skills
(id, skill_name)
VALUES(5450, 'Автоматизированное тестирование');
INSERT INTO public.skills
(id, skill_name)
VALUES(5479, 'Администрирование сайтов');
INSERT INTO public.skills
(id, skill_name)
VALUES(5572, 'Администрирование серверов Windows');
INSERT INTO public.skills
(id, skill_name)
VALUES(5563, 'Алгоритмы');
INSERT INTO public.skills
(id, skill_name)
VALUES(5342, 'Анализ бизнес показателей');
INSERT INTO public.skills
(id, skill_name)
VALUES(5295, 'Анализ данных');
INSERT INTO public.skills
(id, skill_name)
VALUES(5553, 'Анализ макроэкономической среды');
INSERT INTO public.skills
(id, skill_name)
VALUES(5480, 'Анализ посещаемости сайтов');
INSERT INTO public.skills
(id, skill_name)
VALUES(5298, 'Аналитика');
INSERT INTO public.skills
(id, skill_name)
VALUES(5345, 'Аналитические исследования');
INSERT INTO public.skills
(id, skill_name)
VALUES(5275, 'Аналитическое мышление');
INSERT INTO public.skills
(id, skill_name)
VALUES(4847, 'Английский язык');
INSERT INTO public.skills
(id, skill_name)
VALUES(5548, 'Архитектура баз данных');
INSERT INTO public.skills
(id, skill_name)
VALUES(5378, 'Аудит безопасности');
INSERT INTO public.skills
(id, skill_name)
VALUES(5327, 'Веб-аналитика');
INSERT INTO public.skills
(id, skill_name)
VALUES(5478, 'Веб-дизайн');
INSERT INTO public.skills
(id, skill_name)
VALUES(5454, 'Интеграционное тестирование');
INSERT INTO public.skills
(id, skill_name)
VALUES(5425, 'Математический анализ');
INSERT INTO public.skills
(id, skill_name)
VALUES(5531, 'Машинное обучение');
INSERT INTO public.skills
(id, skill_name)
VALUES(5462, 'Нагрузочное тестирование');
INSERT INTO public.skills
(id, skill_name)
VALUES(4841, 'ООП');
INSERT INTO public.skills
(id, skill_name)
VALUES(5301, 'Описание бизнес-процессов');
INSERT INTO public.skills
(id, skill_name)
VALUES(5457, 'Проведение тестирований');
INSERT INTO public.skills
(id, skill_name)
VALUES(5423, 'Продуктовая аналитика');
INSERT INTO public.skills
(id, skill_name)
VALUES(5434, 'Разработка ПО');
INSERT INTO public.skills
(id, skill_name)
VALUES(5296, 'Разработка технических заданий');
INSERT INTO public.skills
(id, skill_name)
VALUES(5453, 'Регрессионное тестирование');
INSERT INTO public.skills
(id, skill_name)
VALUES(5487, 'Рекрутмент');
INSERT INTO public.skills
(id, skill_name)
VALUES(5316, 'Ручное тестирование');
INSERT INTO public.skills
(id, skill_name)
VALUES(5600, 'Сводные таблицы');
INSERT INTO public.skills
(id, skill_name)
VALUES(5300, 'Составление технических заданий');
INSERT INTO public.skills
(id, skill_name)
VALUES(5530, 'Статистика');
INSERT INTO public.skills
(id, skill_name)
VALUES(5516, 'Статистический анализ');
INSERT INTO public.skills
(id, skill_name)
VALUES(5285, 'Стремление к профессиональному росту');
INSERT INTO public.skills
(id, skill_name)
VALUES(5303, 'Тестирование');
INSERT INTO public.skills
(id, skill_name)
VALUES(5314, 'Функциональное тестирование');