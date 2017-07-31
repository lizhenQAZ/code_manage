#!/usr/bin/python
from flask import Flask
from flask import render_template
#from flask import url_for
from flask import request
from flask import redirect
import wtforms
#incomplete

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        print username,password
        if username=="jikexueyuan"and password=="123456":
            return redirect("http://www.jikexueyuan.com")
        else:
            message="Login Failed"
            return render_template('logininterface.html',message=message)
    return render_template('logininterface.html')

if __name__=='__main__':
    app.run(port=8081,debug=True)