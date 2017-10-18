from flask import Flask, render_template
from forms import InputForm
app = Flask(__name__)
app.secret_key = "development-key"


@app.route("/", methods=["GET"])
def hello():
    form = InputForm
    return render_template('entry_menu.html', form = form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
