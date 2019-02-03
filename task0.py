from celery import Celery
import os
from pprint import pprint
app = Celery('a_Task', broker='amqp://devcrack:mientras123@192.168.100.12:5672')

@app.task
def add(x,y):
    dirlist = os.listdir("/home")
    pprint(dirlist)
    return dirlist
