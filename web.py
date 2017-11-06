from flask import Flask, render_template, request, jsonify
import forms as forms
app = Flask(__name__)
app.secret_key = "development-key"


@app.route("/", methods=["GET", "POST"])
def hello():
    """
    Basic web service for data entry
    all data is added to coredb.txt (i know)
    there is no db library because this has to be
    'computationally complex' cuz fuck not reinventing the wheel
    this will not scale lol
    :return:
    """
    if request.method == "POST":
        entry_data = []
        # data entry
        coredb = open("data"+"/coredb.txt", "a")
        entry_data.append(request.form["venue"])
        entry_data.append(".")
        entry_data.append(request.form["pony"])
        entry_data.append(".")
        entry_data.append(request.form["player"])
        entry_data.append(".")
        entry_data.append(request.form["result"])
        entry_data.append(".")
        entry_data.append(request.form["conditions"])
        input_data = ''.join(entry_data)
        valid = validate(input_data)
        error = valid
        if valid:
            coredb.write(input_data + '\n')
        return render_template('entry_menu.html', error=error), 200
    elif request.method == "GET":
        with open("data"+"/visitors.txt", "a") as file:
            file.write('ip: ' + request.environ['REMOTE_ADDR'] + " " + str(jsonify({'ip': request.remote_addr})) + "\n")
        return render_template('entry_menu.html')
    return render_template('entry_menu.html', error=True)


@app.errorhandler(404)
def page_not_found(error):
    """
    404
    :param error:
    :return:
    """
    return render_template('page_not_found.html'), 404


@app.route("/search")
def search():
    """
    probably wont be used
    :return:
    """
    return render_template('page_not_found.html'), 404


@app.route("/stats", methods=["POST", "GET"])
def stats():
    if request.method == "POST":
        x = forms.base()
        print(x)
    return render_template('data_menu.html')


@app.route("/robots.txt")
def robots():
    return render_template('robots.txt')


def validate(data_set):
    """
    data validation for input
    :param data_set:
    :return:
    """
    valid = True
    for i in range(0, len(data_set)):
        if data_set[i] == "." and data_set[i-1] == ".":
            valid = False
    return valid


if __name__ == "__main__":
    app.run(debug=True)
