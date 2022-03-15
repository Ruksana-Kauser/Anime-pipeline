from flask import Flask, render_template, request
from model import checker, anime_rec, lister

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/anime" , methods = ["POST","GET"])
def anime():
    if request.method == "POST":
        a = request.form["anime"]

        if checker(a) == "1":
            n,g,r = anime_rec(a)
            boom = 100
            return render_template("anime.html", n=n,g=g,r=r,boom=boom)
        else:    
            boom = 420
            return render_template("anime.html", boom=boom)
    return render_template("anime.html")

@app.route("/list")
def list():
    n,g,r = lister()
    
    return render_template("list.html", n=n,g=g,r=r)


if __name__ == "__main__":
    app.run(debug=True)

