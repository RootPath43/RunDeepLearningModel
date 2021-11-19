import os

import psycopg2
import threading

def getQueueFromDB():
    connection = psycopg2.connect(user="Deneme",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    cursor = connection.cursor()
    try:
        postgres_insert_query_search = '''SELECT * FROM workqueue WHERE ongoing = False LIMIT 1  '''
        cursor.execute(postgres_insert_query_search)
        connection.commit()
        count = cursor.rowcount
        print(postgres_insert_query_search)
        print(count,'Başarı ile aranan bulundu.')
        #run cmdmodel
        threading.Thread(target=cmdRunCommand, args=count)
        postgres_insert_query_change='''UPDATE workqueue SET ongoing = True WHERE ongoing = False LIMIT 1  '''
        cursor.execute(postgres_insert_query_change)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)

    finally:
        if connection:
            connection.close()
            cursor.close()

        print("PostgreSQL connection is closed")


def cmdRunCommand(path):
    os.popen(f"python custom_1.py train --dataset={path} --weights=coco")