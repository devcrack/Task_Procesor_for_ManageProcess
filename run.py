from main.main import flask_app



#print(celery.conf)
print(flask_app.config)

if __name__ == '__main__':    
    flask_app.run()