from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/categories")
def categories():
    return render_template("categories.html")
@app.route("/movie")
def movie():
    return render_template("movie.html")
@app.route("/comedy")
def comedy():
    return render_template("comedy.html")
@app.route("/song")
def song():
    return render_template("song.html")
@app.route("/webseries")
def webseries():
    return render_template("webseries.html")
@app.route("/cartoon")
def cartoon():
    return render_template("cartoon.html")
@app.route("/sports")
def sports():
    return render_template("sports.html")

if __name__ == "__main__":
    app.run(debug=True)
