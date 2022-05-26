from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def send_mail():
    username = request.form['username']
    password = request.form['password']
    return password + username


if __name__ == "__main__":
    app.run(debug=True)
