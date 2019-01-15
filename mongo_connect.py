from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

#Define the database Name 
app.config['MONGO_DBNAME'] = 'connect_to_mongo'
#Define the conection string in this way we can connect to our database
app.config['MONGO_URI'] = 'mongodb://user:mientras123@ds157574.mlab.com:57574/connect_to_mongo'

try:
    #Create a mongo object, by it we can work with the MOngo database and our backend flask app.
    mongo = PyMongo(app)
except:
    print('Error have been encountered')

'''
Create a route that calls to our function from this Flask app, this allow us create a data collectiion and add to our mongo DataBase.
'''
@app.route('/add')
def add():    
    user = mongo.db.users

    user.insert({'name' : 'Aurelio'})
    return 'A User have been Added'

if __name__ == "__main__":
    app.run(debug = True)      


'''
Notas:
        A collection is the analogous to tables in databases.
'''    