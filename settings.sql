DROP DATABASE IF EXISTS tripme;
DROP USER IF EXISTS tripmeuser; 


CREATE DATABASE tripme;
CREATE USER tripmeuser WITH PASSWORD 'tripme';
GRANT ALL PRIVILEGES ON DATABASE tripme TO tripmeuser;