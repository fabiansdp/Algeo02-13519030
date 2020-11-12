import re

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def parsedoc(filename):
    f = open("uploaded_files//"+filename, "r")
    content = f.readlines()
    for i in range (len(content)):
        content[i] = remove_html_tags(content[i])

    f.close()
    return content