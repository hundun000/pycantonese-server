import pycantonese
from flask import Flask, jsonify, request
from pycantonese.word_segmentation import Segmenter

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
    disallow = set(body['disallow']) if ('disallow' in body and body['disallow'] is not None) else set()
    my_segmenter = Segmenter(disallow=disallow)
    jyutpings = pycantonese.characters_to_jyutping(text, my_segmenter)
    yales = []
    for it in jyutpings:
        jyutping = it[1]
        yale = " ".join(pycantonese.jyutping_to_yale(jyutping))
        print("jyutping = " + (jyutping or 'None') + ", yale = " + (yale or 'None'))
        yales.append([
            it[0],
            yale
        ])
    return jsonify({
        'yale': yales
    })


if __name__ == '__main__':
    # corpus = pycantonese.read_chat("data/CHCC.zip")
    # print("read_chat corpus len = " + str(len(corpus.words())))
    app.run(debug=False, port=8002)
