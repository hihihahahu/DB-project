DROP USER IF EXISTS db_project;
CREATE USER db_project WITH PASSWORD 'db_project';

GRANT ALL PRIVILEGES ON DATABASE project_db TO db_project;
