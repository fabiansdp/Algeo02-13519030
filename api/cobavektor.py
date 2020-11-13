import numpy as np
import nltk
nltk.download('punkt')

def dotProduct(vector1, vector2):
    return sum(x*y for x,y in zip(vector1,vector2))
def lengthVector(vector):
    length = 0
    for elmt in range(len(vector)):
        length += vector[elmt]**2
    length = length**0.5

    return length
v1 = [0,0,0,0]
v2 = [1,2,3,4]

print(dotProduct(v1,v2))
print(np.dot(v1,v2))

print(np.linalg.norm(v1), np.linalg.norm(v2))
print(lengthVector(v1), lengthVector(v2))

with open("./uploaded_files/bali.txt", 'r') as f:
    input = f.readline()
    detector = nltk.data.load('tokenizers/punkt/english.pickle')
    firstline = detector.tokenize(input.strip())[0]
    f.close()
    print(firstline)