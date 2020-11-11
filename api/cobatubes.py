import numpy as np
import glob
import os

from pathlib import Path

class Document(object):
    def __init__(self, judul, kata):
        self.judul = judul
        self.jml_kata = 0
        self.kata = kata
        self.vect = []
        self.similarity = 0
        self.dict = {}

    def createDict(self):
        for kata in database:
            self.dict[kata] = self.kata.count(kata)
    
    def createVector(self):
        for jml in self.dict.values():
            self.vect.append(jml)
        self.vect = np.array(self.vect)

    def createJmlKata(self):
        for jml in self.dict.values():
            self.jml_kata += jml 

    def createSimilarity(self):
        dotopr = np.dot(self.vect, vectQuery)
        lengthopr = np.linalg.norm(self.vect) * np.linalg.norm(vectQuery)
        self.similarity = dotopr / lengthopr

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

    def getSimilarity(self):
        return self.similarity

def addToDatabase(input, database):
    for kata in input:
        if kata not in database:
            database.append(kata)

def createDictQuery(dictQuery):
    for kata in database:
            dictQuery[kata] = query.count(kata)
    pass

def createVecQuery(query, vectQuery, database):
    for jml in dictQuery.values():
        vectQuery.append(jml)
    vectQuery = np.array(vectQuery)
    pass

def sortSimilarity(listobjects):
    listobjects.sort(key = lambda x: x.similarity, reverse = True)

def calculateJmlKata(input):
    jmlkata = 0
    input = input.split()

    for kata in input:
        jmlkata += 1
    
    return jmlkata

database = []
query = ["ini", "dia", "uhuy"]
vectQuery = []
dictQuery = {}

testfile = ["ini", "itu", "dia", "ini"]
testfile2 = ["test", "uhuy", "dia", "hehe"]

addToDatabase(testfile,database)
addToDatabase(testfile2,database)
addToDatabase(query,database)

listobjects = []

file1 = Document("Artikel Sampah", testfile)
listobjects.append(file1)
file2 = Document("Artikel Bagus", testfile2)
listobjects.append(file2)

file1.createDict()
file2.createDict()
createDictQuery(dictQuery)

createVecQuery(query, vectQuery, dictQuery)
file1.createVector()
file2.createVector()

file1.createSimilarity()
file2.createSimilarity()

sim1 = file1.getSimilarity()
sim2 = file2.getSimilarity()

print(sim1, sim2)
for obj in listobjects:
    print(obj.similarity)
sortSimilarity(listobjects)
for obj in listobjects:
    print(obj.similarity)
