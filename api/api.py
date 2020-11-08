from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def main_page():
    return {
        "message": "Hi"
    }

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files["file"]
        filename = secure_filename(file.filename)
        return jsonify(completed= True, name= filename)
