import os
from parsefile import parsedoc
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploaded_files"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Main page backend
@app.route('/')
def main_page():
    return {
        "message": "Hi"
    }

# Upload File
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files["file"]
        
        filename = secure_filename(file.filename)
        
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)

        file.save(os.path.join(app.config["UPLOAD_FOLDER"],filename))
        return jsonify(completed= True, name= filename)


# Menerima query dan mengembalikan response berupa array of objects
@app.route('/query', methods=['POST'])
def query():
    if request.method == 'POST':
        query = request.form["query"]
        return query


# Akses Konten Dokumen yang dipilih
@app.route('/doc/<filename>')
def fetchdoc(filename):
    content = parsedoc(filename)
    name = (os.path.splitext(filename)[0]).title().replace("_"," ") #Hilangkan extension, kapitalisasi huruf pertama, dan mengganti _ menjadi spasi
    
    return jsonify(name = name, content = content)