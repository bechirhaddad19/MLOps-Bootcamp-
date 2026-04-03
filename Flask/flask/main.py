#Here we understand how does flask works and how to create a simple flask application 
#This specific file is combinin flask with html, we will add more features in the next files
from flask import Flask, render_template 
''' It creates an instance of the Flask class, 
Which will be your WSGI application
'''
### WSGI Application
app=Flask( __name__) 

@app.route("/") 
def welcome(): 
    return "<html><H1>Welcome to this Flask best course with HTML </H1></html>"

@app.route("/index") 
def index(): 
    return render_template("index.html")

@app.route("/about") 
def about(): 
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True) #the debug=True will allow us to see the changes we make 
