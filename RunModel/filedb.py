from flask import Flask
from flask import request, jsonify, Response
from flask_restful import Api, Resource
import requests
from werkzeug.utils import secure_filename
import json
import psycopg2
import glob
import os
import redis
from rq import Queue
import time
from multiprocessing import Process

def getfiles(variable):

    print("getfiles working")
    name = "C:\\Users\\Emirhan\\car-damage-detection-using-CNN-master\\custom\\train"
    titles = []
    print("first one")
    for i in glob.iglob(name + "\\*"):
        print("secondaone")
        titles.append((os.path.basename(i)))
    print(titles)
    print("task completed")
    return Process(target=saveDB,args=(titles,name,"validation")).start()
def saveDB(titles, name, table):
    connection = psycopg2.connect(user="deneme",
                                 password="1234",
                                 host="127.0.0.1",
                                 port="5432",
                                 database="deneme")
    cursor = connection.cursor()
    try:

        for z in range(len(titles)):
            postgres_insert_query = f'''INSERT INTO {table} (img_name, img_path) VALUES ('{(name)}' , '{name}')'''
            cursor.execute(postgres_insert_query)
            connection.commit()
            count = cursor.rowcount
            print(postgres_insert_query)
            print(count, "Record inserted successfully into  table")
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)

    finally:
        # closing database connection.
        if connection:
            connection.close()
            cursor.close()

        print("PostgreSQL connection is closed")


def trainModel(epoch):
    #model comes here
    print("hello")
