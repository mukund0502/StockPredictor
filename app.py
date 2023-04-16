from flask import Flask, render_template, request ,redirect, url_for
from flask_mysqldb import MySQL
import yaml
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.plot([1,2,3,4,5])

app = Flask(__name__)


with open("db.yaml") as f:
    db = yaml.full_load(f) 
app.config['MYSQL_HOST'] = db['mqsql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

db = MySQL(app)

#db schema 
#user[uname, fname, lname, email, password]
#favstock[uname, stockname]



@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method=='POST':
        uname = request.form.get('uname')
        password = request.form.get('password')
        cur = db.connection.cursor()
        ret = cur.execute("select * from user where uname = %s", (uname,))
       
        if(uname =='' or len(password)<8):
            info = "*every space is required and password length should greater than 7."
            return render_template('home.html', info = info)
        elif ret>0:
            # print(cur.fetchall()) if this code is live then this will fail because after first time fetching details then another time not work 
            infor = cur.fetchall()
            print(infor[0])
            print(1)
            if(infor[0][4]==password):
                return redirect(url_for('content', uname = uname))
            else:
                info = "*incorrect password, Try again!"
                return render_template('home.html', info = info)
        else:
            info = "*Account not exist!, Please sign up"
            return render_template('home.html', info = info)

    return render_template('home.html')


@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    if request.method == 'POST' :
        email = request.form.get('email')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        uname = request.form.get('uname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if(email=='' or fname=='' or lname =='' or uname =='' or len(password1)<8):
            info = "*every space is required and password length should greater than 7."
            return render_template('signup.html', info = info)
        elif(password1!=password2):
            info = "*password doesn't match!"
            return render_template('signup.html', info = info)
        
        cur = db.connection.cursor()
        ret = cur.execute("select * from user where email=%s or uname = %s", (email, uname))
        if(ret>0):
            info = "*Account already exist!"
            return render_template('signup.html', info = info)


        cur = db.connection.cursor()
        # print(uname, fname, lname, email, password1)
        cur.execute("INSERT INTO USER values (%s, %s, %s, %s, %s)", (uname, fname, lname, email, password1))
        db.connection.commit()

        return redirect(url_for('content', uname = uname))
    return render_template('signup.html')



@app.route('/profile/<uname>', methods = ['GET', 'POST'])
def profile(uname):
    if request.method == 'POST':
        print(321)
        return redirect(f'/content/{uname}')
    return redirect(f'/content/{uname}')



@app.route('/content/<uname>', methods = ['POST', 'GET'])
def content(uname):
    fav = fetchfavstocks(uname)
    fname,lname, uname, email, password = fetchdetails(uname)
    person = [uname,fname,lname,email, fav, password]
    symbol, nifty100 = fetchnifty100(fav)

    if request.method =='POST':
        updateDB(uname,symbol)

    fav = fetchfavstocks(uname)
    fname,lname, uname, email, password = fetchdetails(uname)
    person = [uname,fname,lname,email, fav, password]
    symbol, nifty100 = fetchnifty100(fav)
    return render_template('content.html', person = person, nifty100 = nifty100)





def updateDB(uname,symbol):
    cur = db.connection.cursor()
    cur.execute("delete from favstock where uname = %s", (uname,))
    db.connection.commit()
    for i in symbol:
        if request.form.get(i)=='on':
            cur.execute("insert into favstock values(%s, %s)", (uname,i))
            db.connection.commit()
        
    db.connection.commit()
    return



def fetchdetails(uname):
    cur = db.connection.cursor()
    abc = "select * from user where uname = %s"
    rr = cur.execute(abc, (uname,))
    detail = cur.fetchall()
    cur.close()
    return detail[0][1],detail[0][2],detail[0][0],detail[0][3],detail[0][4]

def fetchfavstocks(uname):
    cur = db.connection.cursor()
    xyz = cur.execute("select stockname from favstock where uname = %s", (uname,))
    favstocks = cur.fetchall()
    fav = []
    for i in favstocks:
        fav.append(i[0])
    return fav

def fetchnifty100(fav):
    df = pd.read_csv('nifty100.csv')
    name = df['Company Name']
    symbols = df['Symbol']
    industry = df['Industry']
    favo = []
    for x in symbols:
        if x in fav:
            favo.append(1)
        else:
            favo.append(0)

    detail = [name.tolist(), symbols.tolist(), industry.tolist(), favo]
    detail = np.array(detail)
    detail = detail.T
    detail = detail.tolist()
    return symbols,detail


if __name__ == '__main__':
    app.run(debug=True)