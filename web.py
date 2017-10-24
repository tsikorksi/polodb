from flask import Flask, render_template, request
from forms import InputForm
app = Flask(__name__)
app.secret_key = "development-key"
ponies = open("data"+"/ponies.txt", "a")
venues = open("data"+"/venues.txt", "a")
players = open("data"+"/players.txt", "a")


@app.route("/", methods=["GET", "POST"])
def hello():
    error = None
    # form = InputForm()
    if request.method == "POST":
        pony_name = request.form["pony"]
        ponies.write(pony_name + '\n')
        venue = request.form["venue"]
        venues.write(venue + '\n')
        player = request.form["player"]
        players.write(player + '\n')
        players.write("test")
        return render_template('entry_menu.html'), 200
    elif request.method == "GET":
        return render_template('entry_menu.html', error=error), 404
    return render_template('entry_menu.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
