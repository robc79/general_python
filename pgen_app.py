# Flask app for password generation api.

from flask import Flask, jsonify
import pgen


app = Flask(__name__)
pgen.load_word_list("common_words.txt")


@app.route("/api/password")
def password():
    return jsonify({"password": pgen.password()})
