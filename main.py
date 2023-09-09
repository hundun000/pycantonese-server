import pycantonese
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/characters_to_jyutping", methods=['POST'])
def characters_to_jyutping():
    body = request.get_json()
    text = body['text']
    jyutping = pycantonese.characters_to_jyutping(text)
    return jsonify({
        'jyutping': jyutping
    })


@app.route("/jyutping_to_yale", methods=['POST'])
def jyutping_to_yale():
    body = request.get_json()
    text = body['text']
    jyutping = pycantonese.characters_to_jyutping(text)
    yale = []
    for it in jyutping:
        yale.append([
            it[0],
            " ".join(pycantonese.jyutping_to_yale(it[1]))
        ])
    return jsonify({
        'yale': yale
    })
