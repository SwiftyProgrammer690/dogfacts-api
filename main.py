from wisdom import *
from flask import *
from random import *
from facts import *
from reasons import *
import os
import json

app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='images/favicon.png')


@app.route('/', methods=['GET'])
def facts():
    fact = dog_facts[randint(0, 100)]
    json_dump = json.dumps(fact)

    return "{data: " + json_dump + "}"


@app.route('/reasons', methods=['GET'])
def reasons():
    reason = dog_reasons[randint(0, 14)]
    json_dump = json.dumps(reason)

    return "{data: " + json_dump + "}"


@app.route('/fun/coinflip', methods=['GET'])
def coinflip():
    values = ["Heads", "Tails"]
    result = values[randint(0, 1)]

    if result == 0:
        json_dump = json.dumps(result)
        return "{data: {flip: " + json_dump + "}}"
    else:
        json_dump = json.dumps(result)
        return "{data: {flip: " + json_dump + "}}"


@app.route('/fun/rolldice', methods=['GET'])
def rolldice():
    values = [1, 2, 3, 4, 5, 6]
    result = values[randint(0, 5)]

    if result == 0:
        json_dump = json.dumps(result)
        return "{data: {roll: " + json_dump + "}}"
    elif result == 1:
        json_dump = json.dumps(result)
        return "{data: {roll: " + json_dump + "}}"
    elif result == 2:
        json_dump = json.dumps(result)
        return "{data: {roll: " + json_dump + "}}"
    elif result == 3:
        json_dump = json.dumps(result)
        return "{data: {roll: " + json_dump + "}}"
    elif result == 4:
        json_dump = json.dumps(result)
        return "{data: {roll: " + json_dump + "}}"
    else:
        json_dump = json.dumps(result)
        return "{data: {roll: " + json_dump + "}}"


@app.route('/dog_zen', methods=['GET'])
def give_quote():
    quote = wisdom[randint(0, 34)]
    json_dump = json.dumps(quote)

    return "{data: Parker Says:{" + json_dump + "}}"


@app.route('/emoji', methods=['GET'])
def get_emoji():
    emojis = ["🐕", "🐶", "🐩"]
    result = emojis[randint(0, 2)]

    return "{data: " + result + "}"


@app.route('/search_emoji/', methods=['GET'])
def request_emoji():
    user_query = str(request.args.get('emoji'))
    if user_query == 'DogFace':
        return "🐶"
    elif user_query == 'Dog':
        return "🐕"
    elif user_query == 'PoodleDog':
        return "🐩"
    else:
        return "<h1>Error 404</h1><br>" + "Emoji Not Found ¯\_(ツ)_/¯"


if __name__ == '__main__':
    app.run(port=7777)
