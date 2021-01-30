from flask import Flask, render_template, url_for, request, redirect
import pyodbc



#setting up our application
app = Flask(__name__)


server = 'lot-tcnj.database.windows.net'
database = 'lot'
username = 'mckinnc4'
password = 'Ellectric6000'   
driver= '{ODBC Driver 17 for SQL Server}'
conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)


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
    try:
        cursor = conn.cursor() 
        cursor.execute("SELECT spaces from lot_four")
        row = cursor.fetchall()
        #value = str(row[0][0])
        value = row[0][0]
	    return render_template('five.html',value=value)
    except:
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

@app.route('/data/<counter>')
def profile(counter):
    try:
        count = int(counter)
        cursor = conn.cursor() 
        cursor.execute("SELECT spaces from lot_four")
        row = cursor.fetchall()
        val = row[0][0] + count
        #cursor = conn.cursor() 
        cursor.execute(f"update lot_four set spaces = {val}")
        cursor.commit()
        return "Valid"
    except:
        return "Invalid"
    


@app.route('/testdb')
def tester():
    cursor = conn.cursor() 
    cursor.execute("SELECT spaces from lot_four")
    row = cursor.fetchall()
    return str(row[0][0])


'''
@app.route('/test')
def tester2():
    print(mysql.is_connected())
'''


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
