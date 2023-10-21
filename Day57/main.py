from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World!!"

@app.route('/<some_name>')
def agify(some_name):
    gender_api = requests.get(url=f"https://api.genderize.io?name={some_name}")
    gender = gender_api.json()["gender"]
    age_api = requests.get(url=f"https://api.agify.io?name={some_name}")
    age = age_api.json()["age"]
    return render_template("index.html", gender=gender, age=age, name=some_name)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_api = requests.get(url=blog_url)
    posts = blog_api.json()
    return render_template("blog.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)


