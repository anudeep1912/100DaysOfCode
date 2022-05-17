from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/<myname>')
def home(myname):
    parameters = {"name": myname}
    age_response = requests.get("https://api.agify.io", params=parameters)
    gender_response = requests.get("https://api.genderize.io", params=parameters)
    return render_template("index.html", name=myname, age=age_response.json()["age"], gender=gender_response.json()["gender"] )


if __name__ == "__main__":
    app.run(debug=True)


