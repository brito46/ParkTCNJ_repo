from flask import Flask, render_template, url_for, request, redirect
import pyodbc

#setting up our application
app = Flask(__name__)


server = 'lot-tcnj.database.windows.net'
database = 'lot'
username = 'mckinnc4'
password = 'Ellectric6000'   
driver= '{ODBC Driver 17 for SQL Server}'
#conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)


#creating an starting route for the start of the application
@app.route('/') 

# creating a function for the start route
def home():
	return render_template('home.html')



@app.route('/five') 
def lot5():
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor() 
        cursor.execute("SELECT spaces from lot_four")
        row = cursor.fetchall()
        #value = str(row[0][0])
        value = row[0][0]
        return render_template('five.html',value=value)
    except:
        return render_template('five.html', value=100)


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
        temp = counter.split('q')
        count = int(temp[0]) #the number before the q signifies 
        tran_id = temp[1]

        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id from transactions where id = '{tran_id}'")
        row = cursor.fetchall()

        #the transaction id was already recorded
        if len(row) > 0:
            return "Valid"
        
        #this means the transaction id doesn't exist, so new information being sent to dB 
        cursor.execute("SELECT spaces from lot_four")
        row = cursor.fetchall()
        val = row[0][0] + count
        if val < 0:
            if row[0][0] != 0:
                cursor.execute("update lot_four set spaces = 0")
                cursor.commit()
        elif val > 234:
            if row[0][0] != 234:
                cursor.execute("update lot_four set spaces = 234")
                cursor.commit()
        else:
            cursor.execute(f"update lot_four set spaces = {val}")
            cursor.commit()

        #start of new day transaction ids so remove the previous transaction ids from dB
        if tran_id == "0":
            cursor.execute(f"delete from transactions")
            cursor.commit()

        #store current day transaction ids
        else:
            cursor.execute(f"insert into transactions values('{tran_id}')")
            cursor.commit()
        return "Valid"
    except:
        return "Invalid"
    


@app.route('/testdb')
def tester():
    try:
        conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = conn.cursor() 
        cursor.execute("SELECT spaces from lot_four")
        row = cursor.fetchall()
        return str(row[0][0])
    except:
        return "100"



if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
