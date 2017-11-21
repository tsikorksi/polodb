from flask import Flask, render_template, request, jsonify
from forms import Stats
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
# app.secret_key = "development-key"


@app.route("/", methods=["GET", "POST"])
def hello():
    """
    Takes data input to entry_menu.html and adds it to the DB
    also logs visitors to site
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
        # adds . for separation
        for i in range(0, len(entry_data)):
            for j in range(0, len(entry_data[i])):
                temp.append(entry_data[i][j])
            temp.append('.')
        # temp.append('.')
        input_data = ''.join(temp)
        # validation
        valid = Validation.validate(input_data)
        error = valid
        if valid:
            coredb.write(input_data + '\n')
        return render_template('entry_menu.html', error=error), 200
    elif request.method == "GET":
        # logging
        with open("data"+"/visitors.txt", "a") as file:
            file.write('ip: ' + request.environ['REMOTE_ADDR'] + " " + str(jsonify({'ip': request.remote_addr})) + "\n")
        return render_template('entry_menu.html')
    return render_template('entry_menu.html', error=True)


@app.errorhandler(404)
def page_not_found(error):
    """
    handles 404 errors, returning page_not_found.html
    :param error:
    :return:
    """
    # logs error
    with open("data" + "/visitors.txt", "a") as file:
        file.write('ip: ' + request.environ['REMOTE_ADDR'] + " " +
                   str(jsonify({'ip': request.remote_addr})) + "\n" + error)
    return render_template('page_not_found.html'), 404


@app.route("/stats", methods=["POST", "GET"])
def stats():
    """
    handles data_menu.html
    takes form input on page and gets data from the DB
    :return:
    """
    if request.method == "POST":
        # globals
        global template3
        template3 = None
        global player_name
        global player_name2
        global enter3
        enter3 = False
        if 'search' in request.form:
            # if first part of check, where only one box is visible
            player_name = request.form['player_name']
            mean, median, max_val, min_val, dev, error = Stats.single_variable_stats(player_name, 0)
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
            # if second name has been entered this handles the second search
            player_name2 = request.form['player_name2']
            mean, median, max_val, min_val, dev, error = Stats.single_variable_stats(player_name2, 0)
            if error:
                return render_template('page_not_found.html'), 404
            else:
                global template2
                template2 = [mean, median, max_val, min_val, dev, player_name2]
                global enter2
                enter2 = True
        elif 'query' in request.form:
            # if second variable comparison has been chosen, this processes handles the POST
            option = request.form['options']
            # chooses flag
            if option == 'pony':
                flag = 2
            elif option == 'venue':
                flag = 1
            elif option == 'conditions':
                flag = 4
            else:
                return render_template('page_not_found.html'), 404
            query = request.form['query']
            # handles weather conditions
            if 'rain' in query:
                query = '1'
            elif 'snow' in query:
                query = '2'
            elif 'hot' in query:
                query = '3'
            elif 'clear' in query:
                query = '0'
            # calculates stats
            mean, median, max_val, min_val, dev, error = Stats.double_variable_stats(player_name, query, flag)
            if error:
                return render_template('page_not_found.html'), 404
            else:
                query = request.form['query']
                template3 = [mean, median, max_val, min_val, dev, query]
            if enter2:
                global template4
                if 'rain' in query:
                    query = '1'
                elif 'snow' in query:
                    query = '2'
                elif 'hot' in query:
                    query = '3'
                elif 'clear' in query:
                    query = '0'
                mean, median, max_val, min_val, dev, error = Stats.double_variable_stats(player_name2, query, flag)
            if flag == 4:
                query = request.form['query']
            template4 = [mean, median, max_val, min_val, dev, query]
            enter3 = True
        # final part 3 variables sent to HTML
        return render_template('data_menu.html', template=template, template2=template2, template3=template3,
                               template4=template4, enter=enter, enter2=enter2, enter3=enter3)
    else:
        # if request was a GET, sends basic HTML to client
        return render_template('data_menu.html', enter=False, enter2=False)


@app.route("/robots.txt")
def robots():
    """
    handles robots.txt
    :return:
    """
    return render_template('robots.txt')


class Validation:

    @staticmethod
    def validate(data_set):
        """
        data validation for input, checks if all fields are filled
        :param data_set:
        :return:
        """
        valid = True
        # checks for missing data
        for i in range(0, len(data_set)):
            # returns False if 2 . next to each other, indicating a data point has not been entered
            if data_set[i] == "." and data_set[i-1] == ".":
                valid = False
        return valid


if __name__ == "__main__":
    app.run(debug=True)
