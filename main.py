from flask import Flask
import requests

# make Flask application with home, contact, and search brewery
# if user wants to search for brewery, they can input text.
# if search response has some object, then take the user,
# to different sub-site with information about brewery
# if you will be able to do that, make another sub-site to which
# user can append breweries from search-brewery sub-site that they like


search = "family"
breweries = requests.get(url=f"https://api.openbrewerydb.org/v1/breweries/search?query={search}")
print(breweries.json())


#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     app.run(debug=True)

