from flask import Flask, request, jsonify, render_template, send_file
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def csv_upload():
    target = os.path.join(APP_ROOT, 'static/')
    for upload in request.files.getlist("file"):
        destination = "/".join([target, upload.filename])
        upload.save(destination)
    return render_template("result.html", filename=upload.filename)

if __name__ == '__main__':
    app.run(debug=True)
