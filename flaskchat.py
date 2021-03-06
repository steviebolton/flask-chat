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
    l = []
    for message in messages:
        if "@" not in message:
            l.append(message)
        if "<username>" in message:
            l.append(message)

    return render_template("chat.html", messages=l, username=username)

@app.route("/chat/<username>/tags/<hashtag>")
def show_tags(username, hashtag):
    fm = []
    for message in messages:
        if "#" + hashtag.lower() in message.lower():
            fm.append(message)
            
    return render_template("chat.html", messages=fm, username=username)

@app.route("/new", methods=['POST'])
def add_new_message():
    message = request.form['message']
    username = request.form['username']
    messages.append(username + ": " + message)
    return redirect("/chat/" + username)





if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)