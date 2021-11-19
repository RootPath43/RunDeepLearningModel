import redis
from flask import Flask
from flask import request
from rq import Queue
import multiprocessing
from CmdRunner import getQueueFromDB
app=Flask(__name__)
r=redis.Redis()
q=Queue(connection=r)
@app.route('/model_run',methods=['GET','POST'])
def model_run():
    if request.args.get('value'):
        #don not forget to add method
        job = q.enqueue(getQueueFromDB, request.args.get("value"))
        q_len = len(q)

        return f"Task{job.id} added to queue at {job.enqueued_at}.{q_len} tasks in the queue"
    return "succeeded"

if __name__=="__main__":
    app.run()