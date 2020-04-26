# Tic-Tac-Toe

This is a flask-based tic-tac-toe game. It features the ability to undo move and has a computer AI that plays a minimax strategy. An example is is deployed on [Heroku](https://tic-tac-toe-beyond.herokuapp.com/).

## Set-up

Set-up a virtual environment and activate it:

```bash
python3 -m venv env
source env/bin/activate
```

You should see (env) before your command prompt now. (You can type `deactivate` to exit the virtual environment any time.)

Install the requirements:

```bash
pip install -U pip
pip install -r requirements.txt
```

## Usage

You can run this app either locally or deploy it to Heroku.

### Local

Make sure you are in the virtual environment (you should see (env) before your command prompt). If not `source /env/bin/activate` to enter it.

```bash
Usage: flask run
```

### Heroku

Set up a Heroku account.

- Create new app
- Connect to GitHub under "Deployment Method"
- Enable automatic deploys under "Automatic Deploys"
- Deploy branch under "Manual Deploy"

## Screenshots

![Tic-Tac-Toe game in progress](https://i.imgur.com/spzLUPH.png)

![Tic-Tac-Toe end of game](https://i.imgur.com/rs3BOTY.png)

## Credit

[Harvard: CS50 Beyond](https://cs50.harvard.edu/beyond/)

## License

Tic-Tac-Toe is licensed under the [MIT license](https://github.com/danrneal/tic-tac-toe/blob/master/LICENSE).
