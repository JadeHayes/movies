from os import getenv
import json

import requests
from flask import Flask, jsonify, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS

def pretty_json(value):
    return json.dumps(value, sort_keys=True, indent=4, separators=(',', ': '))


app = Flask(__name__)
cors = CORS(app)
app.secret_key = getenv('SECRET_KEY', "bleh")
app.jinja_env.filters['pretty_json'] = pretty_json


@app.route("/")
def show_movies():
    query = request.args.get("query", "Monty python")
    headers = {"x-rapidapi-key": "52e1fd5f72mshd42007aabdf908fp183231jsn25f1dacdda82",
	"x-rapidapi-host": "imdb-internet-movie-database-unofficial.p.rapidapi.com"}
    res = requests.get(f"https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/{query}",
                       headers=headers)
    titles = res.json().get("titles", [])
    return jsonify(titles)

@app.route("/<movie_id>", methods=["POST"])
def add_reaction(movie_id):
    # Look up movie_id in reaction DB.
    # Add like or dislike count to the DB.
    return

@app.route("/<movie_id>")
def show_movie_info(movie_id):
    # Make a get request using IMBD's get film API
    # "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/{movie_id}"
    # Display movie information.
    return

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug

    # connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')