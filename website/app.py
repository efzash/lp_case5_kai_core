from flask import Flask, request, jsonify, render_template
import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def csv_upload():
    print(request.files.getlist("file"))
    return render_template("result.html")

if __name__ == '__main__':
    app.run(debug=True)
