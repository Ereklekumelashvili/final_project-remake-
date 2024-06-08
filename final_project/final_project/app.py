from flask import Flask,render_template,request,redirect,url_for
import sqlite3

app=Flask(__name__)

@app.route('/')
def website():
    return render_template('index.html')

@app.route('/login', methods= ['GET','POST'] )
def login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        with sqlite3.connect('tablee.db') as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO people(name,email,password) VALUES (?,?,?)',(name,email,password))
            conn.commit()

            return redirect(url_for('website'))

    return render_template('login.html')






if __name__ =='__main__':
    app.run(debug=True)
