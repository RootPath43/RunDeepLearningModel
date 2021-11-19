import os
import threading

import psycopg2


def getQueueFromDB(text):
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="Deneme")
    cursor = connection.cursor()
    print("GetQueueFromDb",text)
    postgres_insert_query_search = '''SELECT train_img_file FROM workqueue WHERE ongoing = False LIMIT 1  '''
    try:
        for i in range():

            cursor.execute(postgres_insert_query_search)
            connection.commit()
            count = cursor.rowcount
            #get first row db
            postgres_insert_query_change = '''UPDATE workqueue SET ongoing = True ongoing=False order_by asclimit 1)  '''
            cursor.execute(postgres_insert_query_change)
            connection.commit()
            # run cmdmodel
            #threading.Thread(target=cmdRunCommand, args=count)
            cmdRunCommand(count)


    except (Exception, psycopg2.Error) as error:
        print("Failed to insert record into table", error)

    finally:
        # closing database connection.<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        if connection:
            connection.close()
            cursor.close()

        print("PostgreSQL connection is closed")
    print("hellö")

def cmdRunCommand(self,path):
    print("it is running")

    os.system(f"python RunModel.py train --dataset={path} --weights=coco")
    print("it is running")


