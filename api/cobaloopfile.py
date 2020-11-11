from pathlib import Path
import glob
import os

path = Path(__file__).parent / "./testrelativepath/"
for filename in glob.glob(os.path.join(path, '*.html')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        namafileasli = os.path.basename(filename)
        print(namafileasli)
        contents = f.read()
        print(contents)