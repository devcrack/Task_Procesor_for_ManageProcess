from celery import Celery

app = Celery('task ', broker='amqp=192.168.100.12')

@app.task
def reverse(string):
    return string[::-1]