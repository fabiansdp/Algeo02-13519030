import os, nltk, re, string

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def hanya_huruf( input ):
   r = re.match('^[a-zA-Z]+$', input)
   if (r == None):
      return False
   else:
      return True

def stemming_file(filename):
    hasil_stemming = []

    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        fcontent = f.read()
        lines = fcontent.split()
        f.close()

        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        for word in lines:
            if (hanya_huruf(word) and len(word)>1) :
                word = word.strip(string.punctuation).lower()
                word = stemmer.stem(word)
                if (word not in nltk.corpus.stopwords.words('indonesian')):
                    hasil_stemming.append(word)
            else:
                pass
    
    return hasil_stemming

def stemming_query(query):
    global hasil_query

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    lines = query.split()
    hasil_query = []
    for word in lines:
        word = word.strip(string.punctuation).lower()
        word = stemmer.stem(word)
        if (word not in nltk.corpus.stopwords.words('indonesian')):
            hasil_query.append(word)