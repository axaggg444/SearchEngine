from flask import Flask, render_template, request, url_for, flash, redirect
import subprocess
from Search import Search
import sqlite3

app = Flask(__name__, template_folder="template/", static_folder="static/")
app.config["SECRET_KEY"] = "Your Secret Key"

SearchQuery = []

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    if request.method == 'POST':
        search = request.form["search"]

        results = Search(search)
        lenres = len(results)

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        
        resultscomp = []
        for i in results:
            sql = f"""SELECT url, title, description FROM TBL_Search WHERE ID = {i}"""
            cursor.execute(sql)
            for dsatz in cursor:
                if dsatz[1].lower() != "none":
                    resultscomp.append({"url": dsatz[0], "title": dsatz[1]})
                else:
                    resultscomp.append({"url": dsatz[0], "title": dsatz[2]})

        if len(resultscomp) == 0:
            return render_template("index.html")
        else:
            return render_template("index.html", lenres=lenres, resultscomp=resultscomp)

@app.route("/about/")
def about():
    return render_template("About.html")

@app.errorhandler(404)
def NotFound(error):
    return render_template("404.html")

app.run("0.0.0.0", debug=True)
