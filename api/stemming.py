import os, nltk, os.path, re, string, sys, getopt, Sastrawi, glob2

from nltk.stem.porter import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from pathlib import Path

def hanya_huruf( input ):
   r = re.match('^[a-zA-Z]+$', input)
   if (r == None):
      return False
   else:
      return True

def stemming_file():
    global list_output

    path = Path(__file__).parent / './uploaded_files/'
    list_dir = [name for name in glob2.glob(os.path.join(path, '*.txt'))]

    list_input = []
    for i in range (len(list_dir)):
        list_input.append(os.path.basename(list_dir[i]))

    list_output = [[0 for x in range(0)] for x in range(len(list_input))]

    for x in range(len(list_dir)):
        f = open(os.path.join(os.getcwd(), list_dir[x]),"r")
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
                    list_output[x].append(word)
            else:
                pass

def stemming_query():
    global hasil_query

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    query = '...'
    lines = query.split()
    hasil_query = []
    for word in lines:
        word = word.strip(string.punctuation).lower()
        word = stemmer.stem(word)
        if (word not in nltk.corpus.stopwords.words('indonesian')):
            hasil_query.append(word)