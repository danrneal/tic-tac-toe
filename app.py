from flask import Flask, render_template, session, redirect, url_for
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

MOVES = []


@app.route("/")
def index():

    if "board" not in session:
        new_board()

    return render_template(
        "index.html",
        winner=session["winner"],
        game=session["board"],
        turn=session["turn"],
    )


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["turn"]

    if (
        all(move == session["turn"] for move in session["board"][row]) or
        all(move[col] == session["turn"] for move in session["board"]) or
        (
            row == col and
            all(session["board"][i][i] == session["turn"] for i in range(3))
        ) or 
        (
            row + col == 2 and
            all(session["board"][i][2-i] == session["turn"] for i in range(3))
        )
    ):
        session["winner"] = session["turn"]

    switch_player()
    MOVES.append((row, col))

    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    new_board()
    return redirect(url_for("index"))


@app.route("/undo")
def undo():
    if len(MOVES) > 0:
        (row, col) = MOVES.pop()
        session["winner"] = None
        session["board"][row][col] = None
        switch_player()

    return redirect(url_for("index"))


def new_board():
    session["winner"] = None
    session["board"] = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    session["turn"] = "X"


def switch_player():
    if session["turn"] == "X":
        session["turn"] = "0"
    else:
        session["turn"] = "X"
