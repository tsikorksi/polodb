from flask import Flask, render_template, request, jsonify
import forms
import encrypt
template = None
template2 = None
entered = None
entered2 = None
app = Flask(__name__)
app.secret_key = "development-key"
# TODO:secondary data comparison, css, unit tests, docs


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
        # data entry, encrypted with whift of 5, chosen by fair dice roll, guaranteed random
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


@app.route("/stats", methods=["POST", "GET"])
def stats():
    if request.method == "POST":
        if 'search' in request.form:
            player_name = request.form['player_name']
            mean, median, max_val, min_val, dev, error = forms.player_stats(player_name)
            if error:
                return render_template('page_not_found.html'), 404
            else:
                global template
                template = [mean, median, max_val, min_val, dev, player_name]
                global entered
                entered = True
                return render_template('data_menu.html', template=[mean, median, max_val, min_val, dev, player_name],
                                       entered=True)
        else:
            player_name2 = request.form['player_name2']
            mean, median, max_val, min_val, dev, error = forms.player_stats(player_name2)
            if error:
                return render_template('page_not_found.html'), 404
            else:
                global template2
                template2 = [mean, median, max_val, min_val, dev, player_name2]
                global entered2
                entered2 = True
                # resp = render_template('data_menu.html', template2=[mean, median, max_val, min_val, dev, player_name2]
                #                     , entered2=True)
        return render_template('data_menu.html', template=template, template2=template2, entered=entered, entered2=entered2)
    else:
        return render_template('data_menu.html', entered=False, entered2=False)


@app.route("/compare", methods=["POST", "GET"])
def compare():
    pass


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
