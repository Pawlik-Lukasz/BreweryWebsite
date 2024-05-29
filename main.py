from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap5 import Bootstrap
from forms import Registration, Login
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

bootstrap = Bootstrap(app)


@app.route("/")
def home():
    return render_template(template_name_or_list="index.html",
                           title="Home")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        brewery_search = request.form["message"]
        breweries = requests.get(url=f"https://api.openbrewerydb.org/v1/breweries/search?query={brewery_search}")
        breweries_json = breweries.json()
        try:
            random_breweries = random.sample(breweries_json, 5)
            return render_template(template_name_or_list="results.html",
                                   breweries=random_breweries,
                                   title="Results")
        except ValueError:
            flash("Sorry, there are no breweries that match Your search query")
            return render_template(template_name_or_list="index.html")
    else:
        return render_template(template_name_or_list="search.html",
                               title="Search")


@app.route("/favourites", methods=["GET", "POST"])
def favourites():
    if request.method == "GET":
        with open('fav_brew.txt', 'r', encoding='utf-8') as f:
            list_of_brews = []
            [list_of_brews.append(eval(line)) for line in f.readlines()]

        return render_template(template_name_or_list="favourites.html",
                               list_of_brews=list_of_brews,
                               title="Favourites")
    else:
        with open('fav_brew.txt', 'a', encoding='utf-8') as f:
            f.write(request.form["chosen-brewery"] + '\n')
        flash("Your brewery was added to Your favourites")
        return redirect(url_for('home'))


@app.route('/deleted', methods=["POST"])
def delete_fav():
    with open("fav_brew.txt", "r") as f:
        lines = f.readlines()
    with open('fav_brew.txt', 'w', encoding='utf-8') as f:
        for line in lines:
            if request.form["brewery-delete"] not in line:
                f.write(line)
    flash(f'Your favourite brewery {request.form["brewery-delete"]} was deleted :(')
    return redirect(url_for('home'))


@app.route('/register', methods=["GET", "POST"])
def register():
    form = Registration()
    if form.validate_on_submit():
        flash("Signed Up properly")
        return redirect(url_for('home'))
    return render_template(template_name_or_list="register.html",
                           form=form,
                           title="Sign Up")


@app.route('/login', methods=["GET", "POST"])
def login():
    form = Login()
    if form.validate_on_submit and request.method == "POST":
        flash("You are now logged in")
        return redirect(url_for('home'))
    return render_template(template_name_or_list="login.html",
                           form=form,
                           title="Sign Up")


if __name__ == '__main__':
    app.run(debug=True)
