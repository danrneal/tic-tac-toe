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
        return redirect(url_for("reset"))

    return render_template(
        "index.html",
        winner=session["winner"],
        tie=session["tie"],
        board=session["board"],
        player=session["player"],
        new_game=session["new_game"]
    )


@app.route("/play/<int:row>/<int:col>")
def play(row, col):
    session["board"][row][col] = session["player"]
    session["winner"] = is_winner(
        session["board"],
        session["player"],
        (row, col)
    )
    session["tie"] = is_tie(session["board"])
    session["player"] = switch_player(session["player"])
    session["new_game"] = False
    MOVES.append((row, col))

    return redirect(url_for("index"))


@app.route("/computer_move")
def computer_move():
    row, col = minimax(session["board"], switch_player(session["player"]))[0]
    return redirect(url_for("play", row=row, col=col))


@app.route("/undo")
def undo():

    if len(MOVES) > 0:
        (row, col) = MOVES.pop()
        session["winner"] = None
        session["tie"] = False
        session["board"][row][col] = None
        session["player"] = switch_player(session["player"])

    if len(MOVES) == 0:
        session["new_game"] = True

    return redirect(url_for("index"))


@app.route("/reset")
def reset():
    session["winner"] = None
    session["tie"] = False
    session["board"] = [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]
    session["player"] = "X"
    session["new_game"] = True

    return redirect(url_for("index"))


def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"


def is_winner(board, player, move):
    row, col = move
    if (
        all(square == player for square in board[row]) or
        all(row[col] == player for row in board) or
        (row == col and all(board[i][i] == player for i in range(3))) or
        (row + col == 2 and all(board[i][2-i] == player for i in range(3)))
    ):
        return player


def is_tie(board):

    for row in board:
        if None in row:
            return False

    return True


def minimax(board, player, move=None, depth=0):

    if move is not None and is_winner(board, player, move) == "O":
        return (move, 1 / depth)

    if move is not None and is_winner(board, player, move) == "X":
        return (move, -1 / depth)

    if is_tie(board):
        return (move, 0)

    player = switch_player(player)

    if player == "O":
        value = -1
    else:
        value = 1

    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                new_board = [row.copy() for row in board]
                new_board[row][col] = player
                new_value = minimax(new_board, player, (row, col), depth+1)[1]

                if player == "O" and new_value >= value:
                    value = new_value
                    move = (row, col)
                elif player == "X" and new_value <= value:
                    value = new_value
                    move = (row, col)

    return (move, value)
