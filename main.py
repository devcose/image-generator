import json, requests, uuid, csv
from flask import Flask, render_template, request, url_for, jsonify, flash, Response
from flask_bootstrap import Bootstrap5
from lopenai import generate_image
from forms import ImageProperties
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = "ikoosaeyah0Me3aphuu0"

bootstrap = Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new-image", methods=["POST", "GET"])
def new_image():
    form = ImageProperties()
    if request.method == "POST":
        if form.validate_on_submit():
            images = generate_image(prompt=form.prompt.data, size=form.size.data, number=form.number.data)
            return render_template("image-result.html", images=images)
    return render_template("new-image.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
