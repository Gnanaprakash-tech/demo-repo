from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    return jsonify({"message": "Login successful"})

@app.route("/documents", methods=["GET"])
def get_documents():
    return jsonify({"documents": []})

app.run(debug=True)