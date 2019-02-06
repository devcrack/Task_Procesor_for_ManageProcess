from celery import Celery
import os

from pprint import pprint
app = Celery('a_Task', broker='amqp://devcrack:mientras123@192.168.100.5:5672', backend ='mongodb://user:mientras123@ds157574.mlab.com:57574/connect_to_mongo')

@app.task
def add(x,y):
    dirlist = os.listdir("/home")
    pprint(dirlist)
    return dirlist
