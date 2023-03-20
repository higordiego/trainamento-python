# docker run -d -p 3306:3306 --name mysql --platform linux/x86_64 --env MYSQL_ROOT_PASSWORD=12345 mysql:5.7

# create database apresentacao

# create table users (id int auto_increment primary key, name varchar(255) not null, email varchar(255) not null, idade int not null);

import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345',
                              host='127.0.0.1',
                              database='apresentacao')

cursor = cnx.cursor()

sql = "insert into users (`name`, `email`, `idade`) values (%s, %s, %s);"

data_insert = ("Higor Diego", "higordiegoti@gmail.com", 20)

cursor.execute(sql, data_insert)

cnx.commit()
cursor.close()
cnx.close()
