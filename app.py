

from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

#setting up our application
# __name__ is a way to get the import name of the place the app is defined(alternative to hardcode the name of the package)
app = Flask(__name__)


'''
Routing maps to URLs to actions
Routes define the way our users will access data
'''

# @app is a Python Decorator that is a line above the function they are modifying

#creating an starting route for the start of the application
@app.route('/') 

# creating a function for the start route
def home():
	return render_template('home.html')



@app.route('/five') 
def lot5():
	return render_template('five.html')


@app.route('/seventeen') 
def lot17():
	return render_template('seventeen.html')

@app.route('/sixteen')
def lot16():
	return render_template('sixteen.html')


@app.route('/map')
def map():
	return render_template('map.html')


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
