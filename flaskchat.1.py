from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

messages=[
    "Steve:Hi Everyone",
    "Steve:Hi Richard",
    "Tom:Hello there!"
    ]
    
@app.route("/")
def add():
    return render_template("chat.html", messages=messages)   
   
@app.route("/add", methods= ["POST"])
def add_message():
    message = request.form["message"]
    messages.append(message)
    return redirect("/")
    
    
    
      
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)