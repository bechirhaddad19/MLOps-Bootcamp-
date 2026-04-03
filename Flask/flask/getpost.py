#Here we understand how does flask works and how to create a simple flask application 
#This specific file aims to show how to create a simple  flask application with get and post methods 
from flask import Flask, render_template, request 
''' It creates an instance of the Flask class, 
Which will be your WSGI application
'''
### WSGI Application
app=Flask( __name__) 

@app.route("/") 
def welcome(): 
    return "<html><H1>Welcome to this Flask best course with HTML </H1></html>"

@app.route("/index", methods=['GET']) 
def index(): 
    return render_template("index.html")

@app.route("/about") 
def about(): 
    return render_template("about.html")

@app.route("/form", methods=['GET','POST'])
def form():
    if request.method == 'POST':
        # Handle form submission
        pass
    return render_template("form.html")
@app.route("/submit", methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        # Handle form submission
        name = request.form['name']
        email = request.form['email']
        return f"Received: Name : {name}, Email : {email}"
        # Do something with the form data (e.g., save to database)  
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True) #the debug=True will allow us to see the changes we make 
