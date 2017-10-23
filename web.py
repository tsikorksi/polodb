from flask import Flask, render_template, request
from forms import InputForm
app = Flask(__name__)
app.secret_key = "development-key"


@app.route("/", methods=["GET", "POST"])
def hello():
    form = InputForm()
    if request.method == "POST":
        if form.validate() is False:
            return render_template('entry_menu.html', form=form), 412
        else:
            pony_name = request.form["pony"]

            return "yay"
    elif request.method == "GET":
        return render_template('entry_menu.html', form=form), 404
    return render_template('entry_menu.html', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
