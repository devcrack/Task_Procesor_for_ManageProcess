from main.main import flask_app
from main.main import celery_instance


print(celery_instance.conf)
print(flask_app.config)

if __name__ == '__main__':    
    flask_app.run(host = '0.0.0.0')
