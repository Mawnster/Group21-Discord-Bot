from asyncore import write
from cgitb import text
import PyPDF2
import re
import os
import sys

original_stdout = sys.stdout

# Open the pdf file
object = PyPDF2.PdfFileReader(os.getcwd() + '\\TrentUAC\\TrentUAC.pdf')

# Get number of pages
NumPages = object.getNumPages()

# Enter code here
String = "Bachelor of Science Program in Computer Science"
String2 = "The single-major Honours program."



# Extract text and do the search
for i in range(0, NumPages):
    PageObj = object.getPage(i)
    Text = PageObj.extractText()
    if re.search(String,Text):
        if re.search(String2, Text):
            print("Pattern Found on Page: " + str(i))
            append_Text = open(os.getcwd() + "\\TrentUAC\\UAC_CS.txt", "w")
            print(Text.encode("utf-8"), file=append_Text)
            append_Text.close()
            

print("b'TRENT UNIVERSITY  2022\xe2\x80\x932023 Undergraduate Calendar | August Edition 134\nComputer Science & Physics  \xe2\x96\xa0Computer Science & Physics\nProgram Coordinators\nChair of the Department of Computer Science\nR.\xc2\xa0T.\xc2\xa0Hurley , BSc (New Brunswick), PhD (Waterloo)\nChair of the Department of Physics & Astronomy\nA.\xc2\xa0D.\xc2\xa0Slepkov , BSc (Brock), MSc, PhD (Alberta) \nProfessors\nSee faculty listings in Computer Science, Mathematics, and Physics & Astronomy\nThis program is designed to meet the needs of students interested in electronic, hardware, and \ninterfacing aspects of computers, which are based on fundamental principles of physics and \nmathematics.\nBachelor of Science Program in Computer Science & Physics\n\xe2\x80\xa2 The Honours program in Computer Science & Physics is a sequence of courses that compose an \nintegrated whole and are offered by the Departments of Computer Science, Mathematics, and \nPhysics & Astronomy. For more information on individual courses, see Calendar entries for these \ndepartments.\n\xe2\x80\xa2 60% or higher in MATH 1120H is required for upper-level Physics courses; MATH 1350H is a \nprerequisite for upper-level Mathematics courses.\nThe single-major Honours program. 20.0 credits including the following 15.0 credits:\n\xe2\x80\x93 3.5 COIS credits consisting of COIS 1010H, 1020H, 2020H, 2300H, 2320H, 3320H, and 3380H\n\xe2\x80\x93 4.5 PHYS credits consisting of PHYS 1001H, 1002H, 2130H, 2250H, 2610H, 3200Y, 3610H, and \n4610H\n\xe2\x80\x93 4.5 MATH credits consisting of MATH 1110H, 1120H, 1350H, 1550H, 2110H, 2120H, 2150H, \n2600H, and 3150H \n\xe2\x80\x93 0.5 COIS credit from COIS 3400H or 4470H \n\xe2\x80\x93 1.0 COIS credit from COIS 4310H, 4350H, 4370H, or 4400H \n\xe2\x80\x93 1.0 PHYS credit from PHYS 4050H, 4220H, 4240H, 4310H, 4520H, or 4700H\n\xe2\x80\x93 In addition to the program requirements listed above, students must satisfy the University degree \nrequirements (see p. 15), including 0.5 credit from the Approved Indigenous Course List (see \np. 18)'")