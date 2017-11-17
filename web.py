from flask import Flask, render_template, request, jsonify
import forms
import encrypt
player_name = None
player_name2 = None
template = None
template2 = None
template3 = None
template4 = None
enter = None
enter2 = None
enter3 = False
app = Flask(__name__)
app.secret_key = "development-key"
# TODO: css, docs


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
        # data entry, encrypted with shift of 5, chosen by fair dice roll, guaranteed random
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
    print(error)
    return render_template('page_not_found.html'), 404


@app.route("/stats", methods=["POST", "GET"])
def stats():
    if request.method == "POST":
        # print(request.values)
        global template3
        template3 = None
        global player_name
        global player_name2
        global enter3
        enter3 = False
        if 'search' in request.form:
            # global player_name
            player_name = request.form['player_name']
            mean, median, max_val, min_val, dev, error = forms.single_variable_stats(player_name, 0)
            if error:
                return render_template('page_not_found.html'), 404
            else:
                global template
                template = [mean, median, max_val, min_val, dev, player_name]
                global enter
                enter = True
                return render_template('data_menu.html', template=template, template3=template3,
                                       enter=True, enter3=enter3)
        elif 'compare' in request.form:
            # global player_name2
            player_name2 = request.form['player_name2']
            mean, median, max_val, min_val, dev, error = forms.single_variable_stats(player_name2, 0)
            if error:
                return render_template('page_not_found.html'), 404
            else:
                global template2
                template2 = [mean, median, max_val, min_val, dev, player_name2]
                global enter2
                enter2 = True
        elif 'query' in request.form:
            option = request.form['options']
            if option == 'pony':
                flag = 2
            elif option == 'venue':
                flag = 1
            elif option == 'conditions':
                flag = 4
            else:
                return render_template('page_not_found.html'), 404
            query = request.form['query']
            if 'rain' in query:
                query = '1'
            elif 'snow' in query:
                query = '2'
            elif 'hot' in query:
                query = '3'
            elif 'clear' in query:
                query = '0'
            mean, median, max_val, min_val, dev, error = forms.double_variable_stats(player_name, query, flag)
            if error:
                return render_template('page_not_found.html'), 404
            else:
                template3 = [mean, median, max_val, min_val, dev, query]
            if enter2:
                global template4
                mean, median, max_val, min_val, dev, error = forms.double_variable_stats(player_name2, query, flag)
                template4 = [mean, median, max_val, min_val, dev, query]
            enter3 = True
        return render_template('data_menu.html', template=template, template2=template2, template3=template3,
                               template4=template4, enter=enter, enter2=enter2, enter3=enter3)
    else:
        return render_template('data_menu.html', enter=False, enter2=False)


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
