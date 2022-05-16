from flask import Flask
import random
app = Flask(__name__)
random_number = random.randint(1, 9)
print(random_number)


@app.route('/')
def hello_world():
    return "<h1>Guess a number between 1 and 9!</h1>" \
           "<img src='https://media.giphy.com/media/l378khQxt68syiWJy/giphy-downsized-large.gif'></img>"


@app.route("/<int:number>")
def check(number):
    if number > random_number:
        return "<h1 style='color:red;'>The number is high!</h1>" \
           "<img src='https://media.giphy.com/media/MXi8nBJjIBgKbyA1MM/giphy.gif'></img>"
    elif number < random_number:
        return "<h1 style='color:blue;'>The number is low!</h1>" \
           "<img src='https://media.giphy.com/media/XJLEXP9xEJRevqXxnR/giphy.gif'></img>"
    elif number == random_number:
        return "<h1 style='color:green;'>You guessed it correctly!</h1>" \
           "<img src='https://media.giphy.com/media/qMi9FmYD8zXH15Fcw3/giphy.gif'></img>"


if __name__ == "__main__":
    app.run(debug=True)
