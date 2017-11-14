from flask import Flask, render_template, request, jsonify
import forms
import encrypt
app = Flask(__name__)
app.secret_key = "development-key"
# TODO: random test data generation, comparison between players, secondary data comparison, css


@app.route("/", methods=["GET", "POST"])
def hello():
    """
    Basic web service for data entry
    all data is added to coredb.txt
    there is no db library because this has to be
    'computationally complex' cuz fuck not reinventing the wheel
    this will not scale lol
    :return:
    """
    if request.method == "POST":
        entry_data = []
        temp = []
        # data entry
        coredb = open("data"+"/coredb.txt", "a")
        entry_data.append(encrypt.shift_encode(request.form["player"], 5))
        entry_data.append(encrypt.shift_encode(request.form["venue"], 5))
        entry_data.append(encrypt.shift_encode(request.form["pony"], 5))
        entry_data.append(encrypt.shift_encode(request.form["result"], 5))
        entry_data.append(encrypt.shift_encode(request.form["conditions"], 5))
        for i in range(0, len(entry_data)):
            for j in range(0, len(entry_data[i])):
                temp.append(entry_data[i][j])
            temp.append('.')
        # temp.append('.')
        input_data = ''.join(temp)
        # print(input_data)
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
        player_name = request.form['player_name']
        mean, median, max_val, min_val, dev = forms.player_stats(player_name)
        return render_template('data_menu.html', template=[mean, median, max_val, min_val, dev, player_name]
                               , entered=True)
    return render_template('data_menu.html', entered=False)


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
    # checks for missing data
    for i in range(0, len(data_set)):
        if data_set[i] == "." and data_set[i-1] == ".":
            valid = False
    return valid


if __name__ == "__main__":
    app.run(debug=True)
