import os, nltk, os.path, re, string, sys, getopt, Sastrawi

from nltk.stem.porter import PorterStemmer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def hanya_huruf( input ):
   r = re.match('^[a-zA-Z]+$', input)
   if (r == None):
      return False
   else:
      return True

def stemming_file():
    list_input = ['file1.txt', 
                    'file2.txt',
                    'file3.txt',
                    'file4.txt',
                    'file5.txt',
                    'file6.txt',
                    'file7.txt',
                    'file8.txt',
                    'file9.txt',
                    'file10.txt',
                    'file11.txt',
                    'file12.txt',
                    'file13.txt',
                    'file14.txt',
                    'file15.txt']

    hasil_file1 = []
    hasil_file2 = []
    hasil_file3 = []
    hasil_file4 = []
    hasil_file5 = []
    hasil_file6 = []
    hasil_file7 = []
    hasil_file8 = []
    hasil_file9 = []
    hasil_file10 = []
    hasil_file11 = []
    hasil_file12 = []
    hasil_file13 = []
    hasil_file14 = []
    hasil_file15 = []

    list_output = [hasil_file1,
                    hasil_file2,
                    hasil_file3,
                    hasil_file4,
                    hasil_file5,
                    hasil_file6,
                    hasil_file7,
                    hasil_file8,
                    hasil_file9,
                    hasil_file10,
                    hasil_file11,
                    hasil_file12,
                    hasil_file13,
                    hasil_file14,
                    hasil_file15]

    for x in range(15):
        f = open(list_input[x],"r")
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
    
    stemming_file.list_output = list_output
    stemming_file.hasil_file1 = hasil_file1
    stemming_file.hasil_file2 = hasil_file2
    stemming_file.hasil_file3 = hasil_file3
    stemming_file.hasil_file4 = hasil_file4
    stemming_file.hasil_file5 = hasil_file5
    stemming_file.hasil_file6 = hasil_file6
    stemming_file.hasil_file7 = hasil_file7
    stemming_file.hasil_file8 = hasil_file8
    stemming_file.hasil_file9 = hasil_file9
    stemming_file.hasil_file10 = hasil_file10
    stemming_file.hasil_file11 = hasil_file11
    stemming_file.hasil_file12 = hasil_file12
    stemming_file.hasil_file13 = hasil_file13
    stemming_file.hasil_file14 = hasil_file14
    stemming_file.hasil_file15 = hasil_file15

def stemming_query():
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    query = '....'
    lines = query.split()
    hasil_query = []
    for word in lines:
        word = word.strip(string.punctuation).lower()
        word = stemmer.stem(word)
        if (word not in nltk.corpus.stopwords.words('indonesian')):
            hasil_query.append(word)
    
    stemming_query.hasil_query = hasil_query