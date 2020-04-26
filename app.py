from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():

    if "board" not in session:
        new_board()

    return render_template(
        "index.html", game=session["board"], turn=session["turn"]
    )


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]

    if session["turn"] == "X":
        session["turn"] = "0"
    else:
        session["turn"] = "X"

    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    new_board()
    return redirect(url_for("index"))


def new_board():
    session["board"] = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    session["turn"] = "X"
