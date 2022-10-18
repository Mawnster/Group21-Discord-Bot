# Incomplete, See test.py

import os
import fitz

# creating an object 
file_Path = os.getcwd() + '\\TrentUAC\\TrentUAC.pdf'


with fitz.open(filename = file_Path, filetype="pdf") as doc:
    text = ""
    temp = ""
    for page in doc:
        for line in page:
            temp = line.get_text()
            if temp.find("The single-major Honours program."):
                text += temp

print(text)



