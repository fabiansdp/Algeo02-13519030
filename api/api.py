import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "D:\\Projects\\tubes-algeo\\api\\uploaded_files"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        return jsonify(completed= True, name= filename)

@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        query = request.data
        return query