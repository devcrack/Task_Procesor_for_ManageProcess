from celery import Celery 


""" Creating the Celery instance """
def make_celery(app):
    celery = Celery(app)
    celery.conf.update(app.config)
    Task_Base = celery.Task
        
    class Context_Task(Task_Base):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return Task_Base.__call__(self, *args, *kwargs)
    celery.Task=Context_Task
    return celery 
