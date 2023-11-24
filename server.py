from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/admin", methods=["GET", "POST"])
def admin():
    return render_template("admin.html")


@app.route("/user", methods=["GET", "POST"])
def user():
    return render_template("user.html")


if __name__ == "__main__":
    app.run(debug=True)
