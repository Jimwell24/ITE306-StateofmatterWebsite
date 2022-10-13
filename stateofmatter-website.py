from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/stateofmatter")
def stateofmatter():
    return render_template("stateofmatter.html")


@app.route("/solid")
def solid():
    return render_template("solid.html")


@app.route("/liquid")
def liquid():
    return render_template("liquid.html")


@app.route("/gas")
def gas():
    return render_template("gas.html")

@app.route("/plasma")
def plasma():
    return render_template("plasma.html")


if __name__ == "__main__":
    app.run()