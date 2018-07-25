from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

messages = [
    "Richard: Hi everyone",
    "Everyone: Hi Richard",
    "Tom: Hello there",
    ]

@app.route("/")
def show_join():
    return render_template("join.html")

@app.route("/join")
def do_join():
    username = request.args['username']
    return redirect("/chat/" + username)

@app.route("/chat/<username>")
def show_chat(username):
    return render_template("chat.html", messages=messages, username=username)


@app.route("/new", methods=['POST'])
def add_new_message():
    message = request.form['message']
    username = request.form['username']
    messages.append(username + ": " + message)
    return redirect("/chat/" + username)



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)