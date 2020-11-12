import numpy as np
import glob
import os

from pathlib import Path

'''class buat nyimpen dokumen yang diupload'''
class Document(object):
    '''konstruktor class'''
    def __init__(self, judul, kata, jml_kata, first_line):
        self.judul = judul
        self.jml_kata = jml_kata
        self.kata = kata
        self.firstline = first_line
        self.vect = []
        self.similarity = 0
        self.dict = {}

    '''fungsi konstruktor'''
    def createDict(self):
        for kata in database:
            self.dict[kata] = self.kata.count(kata)
    
    def createVector(self):
        for jml in self.dict.values():
            self.vect.append(jml)
        self.vect = np.array(self.vect)

    def createSimilarity(self):
        dotopr = np.dot(self.vect, vectQuery)
        lengthopr = np.linalg.norm(self.vect) * np.linalg.norm(vectQuery)
        self.similarity = dotopr / lengthopr

    '''getter variable'''
    def getDict(self):
        return self.dict

    def getJudul(self):
        return self.judul
    
    def getKata(self):
        return self.kata

    def getFirstLine(self):
        return self.firstline

    def getVector(self):
        return self.vect
    
    def getJmlKata(self):
        return self.jml_kata

    def getSimilarity(self):
        return self.similarity

'''fungsi buat nyimpen setiap kata ke database'''
def addToDatabase(input, database):
    for kata in input:
        if kata not in database:
            database.append(kata)

'''buat dictionary dari query'''
def createDictQuery(query, dictQuery):
    for kata in database:
            dictQuery[kata] = query.count(kata)
    pass

'''buat vector dari dictionary query'''
def createVecQuery(query, vectQuery, database):
    for jml in dictQuery.values():
        vectQuery.append(jml)
    vectQuery = np.array(vectQuery)
    pass

'''sort nilai similarity tiap dokumen'''
def sortSimilarity(listobjects):
    listobjects.sort(key = lambda x: x.similarity, reverse = True)

'''hitung jumlah kata dari dokumen asli'''
def calculateJmlKata(filename):
    jmlkata = 0
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        input = f.read()
        lines = input.split()
        f.close()

        for word in lines:
            jmlkata += 1

    return jmlkata

'''ngambil kalimat pertama dokumen'''
def extractFirstLine(filename):
    firstline = []
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        input = f.readline()
        firstline = input
        f.close()
    return firstline

'''kamus data lengkap'''
database = [] 

'''properti dari query'''
vectQuery = [] 
dictQuery = {}

'''list buat nyimpen Document'''
listOfDocuments = []