#Here we understand how does flask works and how to create a simple flask application 
#This specific file aims to show jinja template in flask 
# 
### Jinja Template in Flask
''' 
 {{  }} : Expression to print to the template output
    {%  %} : conditions, for loops
    {#  #} : Comments
''' 

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



## Variable Rules : new part 
@app.route("/success2/<int:score>", methods=['GET','POST'])
def success2(score):
   res=""
   if score>=50:
      res="Passed"
   else:
      res="Failed"
    
   return render_template("result.html", results=res)



@app.route("/successres/<int:score>")
def successres(score):
   res=""
   if score>=50:
      res="Passed"
   else:
      res="Failed"

   exp={"score":score, "res":res}
   return render_template("result1.html", results=exp)

## if condition 
@app.route("/successif/<int:score>")
def successif(score):
   return render_template("result.html", results=score)

@app.route("/success/<int:score>", methods=['GET','POST'])
def success(score):
   return "The score is "+ str(score)









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
