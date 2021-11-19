import os.path
import sys
sys.path.append(os.path.join(os.path.dirname('filedb.py')))
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
from rq import Queue, Connection, Worker
import time
from filedb import getfiles
import multiprocessing


app = Flask(__name__)
r=redis.Redis()
q=Queue(connection=r)
@app.route('/pass_val',methods=['GET','POST'])
def pass_val():

    #name=request.args.get('value')
    if request.args.get('value') :
        job=q.enqueue(getfiles, request.args.get("value"))
        q_len=len(q)


        return f"Task{job.id} added to queue at {job.enqueued_at}.{q_len } tasks in the queue"
    print('name',request.args.get('value'))
    return "no value for n"



if __name__=="__main__":
    app.run()