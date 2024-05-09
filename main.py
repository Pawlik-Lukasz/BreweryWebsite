from flask import Flask, render_template, request
from flask_bootstrap5 import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import requests
import random
import ast


# make Flask application with home, contact, and search brewery
# if user wants to search for brewery, they can input text.
# if search response has some object, then take the user,
# to different sub-site with information about brewery
# if you will be able to do that, make another sub-site to which
# user can append breweries from search-brewery sub-site that they like


app = Flask(__name__)


# class FavForm(FlaskForm):
#     brewery = StringField('Brewery Rating', validators=[DataRequired()])
#     submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template(template_name_or_list="index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    # form = FavForm(request.form)
    if request.method == "POST":
        brewery_search = request.form["message"]
        breweries = requests.get(url=f"https://api.openbrewerydb.org/v1/breweries/search?query={brewery_search}")
        breweries_json = breweries.json()
        try:
            random_breweries = random.sample(breweries_json, 5)
            return render_template(template_name_or_list="results.html", breweries=random_breweries)
        except ValueError:
            return render_template(template_name_or_list="index.html")
    else:
        return render_template(template_name_or_list="search.html")


@app.route("/favourites", methods=["GET", "POST"])
def favourites():
    if request.method == "GET":
        with open('fav_brew.txt', 'r', encoding='utf-8') as f:
            read = f.read()
            brew_dict = eval(read)
            brew_name = brew_dict["name"]
            brew_addr = brew_dict["address_1"]
            brew_country = brew_dict["country"]
            brew_url = brew_dict["website_url"]
        return render_template(template_name_or_list="favourites.html",
                               brew_name=brew_name, brew_addr=brew_addr, brew_country=brew_country, brew_url=brew_url)
    else:
        with open('fav_brew.txt', 'w', encoding='utf-8') as f:
            f.write(request.form["chosen-brewery"])
        return render_template(template_name_or_list="index.html")


if __name__ == '__main__':
    app.run(debug=True)
