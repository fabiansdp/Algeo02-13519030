import numpy as np

class Document(object):
    def __init__(self, judul, kata):
        self.judul = judul
        self.jml_kata = 0
        self.kata = kata
        self.vect = []
        self.similarity = 0
        self.dict = {}
        #self.dict = self.createDict()

    def createDict(self):
        for kata in database:
            self.dict[kata] = self.kata.count(kata)
    
    def createVector(self):
        for jml in self.dict.values():
            self.vect.append(jml)
        self.vect = np.array(self.vect)
        #self.vect = csr_matrix(self.vect)

    def createJmlKata(self):
        for jml in self.dict.values():
            self.jml_kata += jml 

    def createSimilarity(self):
        self.similarity = np.dot(self.vect, vecQuery)

    def getDict(self):
        return self.dict

    def getJudul(self):
        return self.judul
    
    def getKata(self):
        return self.kata

    def getVector(self):
        return self.vect
    
    def getJmlKata(self):
        return self.jml_kata

def addToDatabase(input, database):
    for kata in input:
        if kata not in database:
            database.append(kata)
def createDictQuery(dictQuery):
    pass
def createVecQuery(query, database):
    pass

database = []

testfile = ["ini", "itu", "dia", "ini"]
testfile2 = ["test", "uhuy", "dia", "hehe"]

addToDatabase(testfile,database)
addToDatabase(testfile2,database)
print(database)

file1 = Document("Artikel Sampah", testfile)
file2 = Document("Artikel Bagus", testfile2)

file1.createDict()
file2.createDict()
dict1 = print(file1.getDict())
dict2 = print(file2.getDict())

file1.createVector()
file2.createVector()
vec1 = file1.getVector()
vec2 = file2.getVector()
print(file1.getVector())
print(file2.getVector())

dot = np.dot(vec1, vec2)
print(dot)

file1.createJmlKata()
print(file1.getJmlKata())
