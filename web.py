from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return render_template('entry_menu.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
