import os, glob

from pathlib import Path
from collections import Counter

from flask.helpers import send_from_directory
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

    listOfDocuments = []
    '''ambil file yang telah di upload dan proses'''
    path = Path(__file__).parent / './uploaded_files/'
    for filename in glob.glob(os.path.join(path, '*.txt')): #iterasi tiap file yang ada dengan extension .txt
      namafileasli = Path(filename).stem #ambil nama file untuk jadi nama variable Document()
      urlfile = os.path.basename(filename)
      outputstemming = stemming_file(filename) #stemming file
      kalimat1 = extractFirstLine(filename) #ambil kalimat pertama
      addToDatabase(outputstemming, database) #tambah kata yang ada dalam file ke database
      jmlkata = calculateJmlKata(filename) #hitung jumlah kata dokumen asli
      #if namafileasli not in listOfDocuments:
      namafileasli = Document(namafileasli, urlfile, outputstemming, jmlkata, kalimat1) #buat Document baru
      listOfDocuments.append(namafileasli) #buat list of Documents
    
    addToDatabase(hasil_query, database) #tambah kata yang ada di query ke database

    ''' buat dictionary dan vector dari query '''
    iniVectQuery = []
    iniDictQuery = {}
    iniDictQuery = createDictQuery(hasil_query)
    iniVectQuery = createVecQuery(hasil_query, iniDictQuery, database)
    
    ''' buat dictionary dan vector setiap Document dan hitung similarity'''
    for doc in range(len(listOfDocuments)):
      if not(listOfDocuments[doc].initVector):
        listOfDocuments[doc].createDict()
        listOfDocuments[doc].createVector()
        listOfDocuments[doc].createSimilarity(iniVectQuery)
        
    '''sort dokumen berdasarkan similarity'''
    sortSimilarity(listOfDocuments)

    listofDict = []
    for doc in range(len(listOfDocuments)): #Membuat list of objects
      listofDict.append(
        {
          'judul': listOfDocuments[doc].getJudul(),
          'url' : listOfDocuments[doc].getURL(),
          'jumlah': listOfDocuments[doc].getJmlKata(),
          'similarity' : listOfDocuments[doc].getSimilarity(),
          'first_sentence' : listOfDocuments[doc].getFirstLine()
        }
      )
    
    
    jmlh_query = Counter(hasil_query) #Hitung jumlah tiap kata query yang muncul

    listofQuery = [{
        'dokumen' : 'query',
        'jumlah' : jmlh_query
        }]

    for doc in range(len(listOfDocuments)): #Membuat list of objects
      listofQuery.append(
        {
          'dokumen': listOfDocuments[doc].getJudul(),
          'jumlah' : listOfDocuments[doc].getDict()
        }
      )

    del iniVectQuery
    del iniDictQuery
    del listOfDocuments
    
    return jsonify(query=sorted(hasil_query), hasil=listofDict, dataTabel=listofQuery)


# Akses Konten Dokumen yang dipilih
@app.route('/doc/<filename>')
def fetchdoc(filename):
  content = parsedoc(filename)
  name = (os.path.splitext(filename)[0]).title().replace("_"," ") #Hilangkan extension, kapitalisasi huruf pertama, dan mengganti _ menjadi spasi
  
  return jsonify(name = name, content = content)

# Download dokumen
@app.route('/download/<filename>')
def getfile(filename):
  return send_from_directory(app.config["UPLOAD_FOLDER"],filename,as_attachment=True)


