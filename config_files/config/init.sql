create database data_tracking;
create user data_tracking with encrypted password 'data_tracking';
grant all privileges on database data_tracking to data_tracking;
alter role data_tracking LOGIN;
