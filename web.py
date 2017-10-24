from flask import Flask, render_template, request
app = Flask(__name__)
app.secret_key = "development-key"


@app.route("/", methods=["GET", "POST"])
def hello():
    """
    Basic web service for data entry
    :return:
    """
    if request.method == "POST":
        ponies = open("data" + "/ponies.txt", "w")
        venues = open("data" + "/venues.txt", "w")
        players = open("data" + "/players.txt", "w")
        venue = request.form["venue"]
        venues.write(venue + '\n')
        pony_name = request.form["pony"]
        ponies.write(pony_name + '\n')
        player = request.form["player"]
        players.write(player + '\n')
        return render_template('entry_menu.html'), 200
    elif request.method == "GET":
        return render_template('entry_menu.html', error=True), 400
    return render_template('entry_menu.html', error=False)


@app.errorhandler(404)
def page_not_found(error):
    """
    404
    :param error:
    :return:
    """
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
