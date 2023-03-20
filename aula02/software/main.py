# coding: utf-8
# CREATE DATABASE apresentacao CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
import sys
import mysql.connector
import requests

# create table ceps (id int auto_increment primary key, cep varchar(255) not null, logradouro varchar(255) not null, complemento varchar(255), bairro varchar(255), localidade varchar(255), uf varchar(255));
cnx = mysql.connector.connect(user='root', password='12345',
                              host='127.0.0.1',
                              database='apresentacao')

cursor = cnx.cursor()

cep_user = input("Insira o cep para busca: ")

url = "https://viacep.com.br/ws/" + cep_user + "/json/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

response_api_cep = response.json()

sql = "insert into ceps (`cep`, `logradouro`, `complemento`, `bairro`, `localidade`, `uf`) values (%s, %s, %s, %s, %s, %s);"

data_insert = (
    response_api_cep['cep'],
    response_api_cep['logradouro'],
    response_api_cep['complemento'],
    response_api_cep['bairro'],
    response_api_cep['localidade'],
    response_api_cep['uf']
    )

cursor.execute(sql, data_insert)

cnx.commit()
cursor.close()
cnx.close()
