from flask import Flask, render_template
import random, datetime
app = Flask(__name__)

year= datetime.datetime.today().year

@app.route('/')
def home():
    a = datetime.datetime.today().year
    random_number = random.randint(1, 10)
    return render_template("index.html", num=random_number, year=a)


if __name__ == "__main__":
    app.run(debug=True)


