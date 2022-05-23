from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

post_url = "https://api.npoint.io/ee3e3912e83d723277f5"
post_response = requests.get(post_url).json()
posts_list = []
for post in post_response:
    posts_list.append(Post(post["id"], post["title"], post["subtitle"], post["body"]))

@app.route('/')
def home():
    return render_template("index.html", all_posts=posts_list)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts_list:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
