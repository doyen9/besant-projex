

from django.shortcuts import render
from flask import Flask, render_template, request, make_response, url_for, redirect
app = Flask(__name__)

firstname = 0 
lastname = 0
  
@app.route("/",methods = ['GET','POST'])
def start():
   global lastname
   global firstname
   if request.method == "POST":
      firstname = request.form['fname']
      lastname = request.form['lname']
      # print(firstname,lastname)

   return firstname,lastname,render_template('front.html')
   # return render_template("front.html") #, firstname,lastname

print(firstname,lastname,"helo")

@app.route('/index')
def index():
   return render_template('index.html')


if __name__ == '__main__':
   app.run(debug = True)


