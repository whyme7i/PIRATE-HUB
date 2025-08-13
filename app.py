from flask import Flask, render_template, abort
import json, os

app = Flask(__name__)

# Load games from JSON
with open("games.json", "r", encoding="utf-8") as f:
    games = json.load(f)

@app.route("/")
def home():
    return render_template("index.html", games=games)

@app.route("/game/<int:game_id>")
def game_page(game_id):
    game = next((g for g in games if g["id"] == game_id), None)
    if not game:
        abort(404)
    return render_template("game.html", game=game)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
