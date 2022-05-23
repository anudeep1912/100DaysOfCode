from flask import Flask, render_template, request
import requests
from post import Post

app = Flask(__name__)

blog_endpoint = "https://api.npoint.io/ca49d8d4e49d3200a110"
post_response = requests.get(blog_endpoint).json()
post_list = []
for post in post_response:
    post_list.append(Post(post['id'], post['title'], post['subtitle'], post['body'], post["author"], post["date"], post["img-url"]))


@app.route("/")
def home_page():
    return render_template("index.html", all_posts=post_list)


@app.route("/index.html")
def home():
    return render_template("index.html", all_posts=post_list)


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", msg_sent=False)
    elif request.method == "POST":
        return render_template("contact.html", msg_sent=True)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_list:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
