#Here we understand how does flask works and how to create a simple flask application 
#This specific file is the basic structure of a flask application, we will add more features in the next files
from flask import Flask 

''' It creates an instance of the Flask class, 
Which will be your WSGI application
'''
### WSGI Application
app=Flask( __name__) 

@app.route("/") 
def welcome(): 
    return "Welcome to this Flask best course"

@app.route("/index") 
def index(): 
    return "Welcome to the index page"

if __name__=="__main__":
    app.run(debug=True) #the debug=True will allow us to see the changes we make 
