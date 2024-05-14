from flask import Flask, json, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/say_name5', methods=['GET', 'POST'])
def say_name5():

    json = request.get_json()
    nome = json['txtNome']
    print(nome)
    return jsonify(first_name=nome)



if __name__ == "__main__":
    app.run(debug=True, port=5000)