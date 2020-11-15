import os, nltk, re, string

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Untuk menghilangkan karakter atau simbol, jadi akan mengembalikan hanya hufuf baik kapital maupun biasa
def hanya_huruf( input ):
   r = re.match('^[a-zA-Z0-9]+$', input)
   if (r == None):
      return False
   else:
      return True

# Untuk stemming dan stopword dokumen
def stemming_file(filename, path):
    hasil_stemming = []

    with open(os.path.join(path, filename), 'r') as f:  # Membuka dokumen
        fcontent = f.read()
        lines = fcontent.split()
        f.close()

        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        for word in lines:
            if (hanya_huruf(word) and len(word)>1) :    # Jika kata tersebut terdiri hanya huruf (tidak terdapat simbol) dan panjangnya lebih dari 1
                word = word.strip(string.punctuation).lower()   # Membuat semua huruf kapital menjadi huruf biasa
                word = stemmer.stem(word)
                if (word not in nltk.corpus.stopwords.words('indonesian')): # Stopword atau menghilangkan kata yang tidak bermakna atau kata umum
                    hasil_stemming.append(word) # Menambah kata ke dalam array hasil stemming dokumen/file
            else:
                pass
    
    return hasil_stemming

# Untuk stemming dan stopword query
def stemming_query(query):
    global hasil_query

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    lines = query.split()
    hasil_query = []
    for word in lines:
        word = word.strip(string.punctuation).lower()   # Membuat semua huruf kapital menjadi huruf biasa
        word = stemmer.stem(word)
        if (word not in nltk.corpus.stopwords.words('indonesian')): # Stopword atau menghilangkan kata yang tidak bermakna atau kata umum
            hasil_query.append(word)    # Menambah kata ke dalam array hasil stemming query