import os, nltk, os.path, re, string, sys, getopt, Sastrawi, glob2

from parsefile import parsedoc
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from stemming import *
from prosesquery import *

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

        stemming_query(query) #stemming query
        from stemming import hasil_query # import hasil stemming query

        '''ambil file yang telah di upload dan proses'''
        path = Path(__file__).parent / './uploaded_files/'
        for filename in glob.glob(os.path.join(path, '*.txt')): #iterasi tiap file yang ada dengan extension .txt
            namafileasli = Path(filename).stem #ambil nama file untuk jadi nama variable Document()
            outputstemming = stemming_file(filename) #stemming file
            kalimat1 = extractFirstLine(filename)
            addToDatabase(outputstemming, database) #tambah kata yang ada dalam file ke database
            jmlkata = calculateJmlKata(filename)
            namafileasli = Document(namafileasli, outputstemming, jmlkata, kalimat1) #buat Document baru
            listOfDocuments.append(namafileasli) #buat list of Documents

        addToDatabase(hasil_query, database) #tambah kata yang ada di query ke database

        ''' buat dictionary dan vector dari query '''
        createDictQuery(hasil_query, dictQuery)
        createVecQuery(hasil_query, vectQuery, database)
        
        ''' buat dictionary dan vector setiap Document dan hitung similarity'''
        for doc in range(len(listOfDocuments)):
            listOfDocuments[doc].createDict()
            listOfDocuments[doc].createVector()
            listOfDocuments[doc].createSimilarity()

        sortSimilarity(listOfDocuments)
        print(database)
        for doc in range(len(listOfDocuments)):
            print(listOfDocuments[doc].getJudul())
            print(listOfDocuments[doc].getJmlKata())
            print(listOfDocuments[doc].getSimilarity())
            print(listOfDocuments[doc].getFirstLine())
        pass


# Akses Konten Dokumen yang dipilih
@app.route('/doc/<filename>')
def fetchdoc(filename):
    content = parsedoc(filename)
    name = (os.path.splitext(filename)[0]).title().replace("_"," ") #Hilangkan extension, kapitalisasi huruf pertama, dan mengganti _ menjadi spasi
    
    return jsonify(name = name, content = content)


