from flask import Flask, render_template, request
import requests

# make Flask application with home, contact, and search brewery
# if user wants to search for brewery, they can input text.
# if search response has some object, then take the user,
# to different sub-site with information about brewery
# if you will be able to do that, make another sub-site to which
# user can append breweries from search-brewery sub-site that they like


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(template_name_or_list="index.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        brewery_search = request.form["message"]
        breweries = requests.get(url=f"https://api.openbrewerydb.org/v1/breweries/search?query={brewery_search}")
        print(breweries.json())
        return render_template(template_name_or_list="search.html")
    else:
        return render_template(template_name_or_list="search.html")


if __name__ == '__main__':
    app.run(debug=True)

