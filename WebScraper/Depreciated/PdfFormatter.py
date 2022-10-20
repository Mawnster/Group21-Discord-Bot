#Zachary Bricknell
#PDFParse.py
#10/18/2022
#Test script for reading a pdf and writing out the important information to a txt document
#The script will seach the two defined strings against each page of the pdf. If it finds a match
#on the same page it will save the text of said page to another text document for a more
#compiled piece of data to use. 
#With further processing it removes the leading information before the desired keyword and
#appends a finalized text document without ascii characters and properly appending newlines 

#Changelog
#Changed to two strings as there were multiple pages that returned for either of the subtrings
#and now only returns two
#Created a new text document with further processing for a much more readable document.
#Moved to depreciated folder and copied the code over to the main script to invoke it all 
#instead of importing and calling the methods


#-----------------
#-Data dictionary-
#-----------------

# pdf_Original      using the PyPDF2 library this stores the pdf to a readable object
# numPages          Saves the total number of pagees from PEF_Original
# title_String      The first headline string we are searching for in the PDF
# narrow_String     a keyword used to find in tandem with the title_String. Also used for 
#                   a reference to remove data before this keyword
# head_Flag         a boolean used to denote when we found the keyword defined in narrow_String
#                   and return true once found
# pdf_Page_Object   store an instance of the page as an object
# pdf_Page_Text     Retrieve the actual text only from the pdf_Page_Object
# append_Text       the file that we are stroing the pdf_Page_Text to (After filtering for specific pages only)



#------
#-MAIN-
#------
import PyPDF2
import re
import os
import io

# Open the pdf file
pdf_Original = PyPDF2.PdfFileReader(os.getcwd() + '\\TrentUAC\\TrentUAC.pdf')

# Get number of pages to ensure we iterate the entire pdf (breaking after a few 100 pages otherwies)
numPages = pdf_Original.getNumPages()

#defined strings to search for both a string and keyword
title_String = "Bachelor of Science Program in Computer Science"
narrow_String = "single-major"
#flag used to cut the leading information before the desired content
head_Flag = False

#this loop will iterate over the maximum number of pages 
#looking for the a match of both the title_String and narrow_string. If successfull
#save that pages text to a file to narrow down the pdf size to only a few pages
#this loop also utilitizes the print function to print to a text file instead of write.(Educational)
def pdf_To_Text():
    for i in range(0, numPages):
        pdf_Page_Object = pdf_Original.getPage(i)
        pdf_Page_Text = pdf_Page_Object.extractText()
        #searching two strongs to try and narrow down the information
        if re.search(title_String,pdf_Page_Text):
            if re.search(narrow_String, pdf_Page_Text):
                append_Text = io.open(os.getcwd() + "\\TrentUAC\\UAC_CS.txt", "w")
                #Remove all ascii characters to only get text
                print(pdf_Page_Text.encode("ascii", "ignore"), file=append_Text)
                append_Text.close()


#This loop will further narrow down the input information removing all the un-nessisary data before
#the start of the keyword defined in narrow_String. Afterwords appending the words to the text file
#It will also check for \n character which denote a newline and remove them, but also adding the
#newline to the new file for readbility and further processing.            
def format_PDF():
    pdf_To_Text()
    with open(os.getcwd() + "\\TrentUAC\\UAC_CS.txt", "r") as input_File, open(os.getcwd() + "\\TrentUAC\\Formatted_UAC.txt", "w") as output_File:
        for line in input_File:
            for word in line.split():
                #create a flag to cut all the leading information off the text to further
                #narrow down the content
                if narrow_String in word:
                    head_Flag = True
                if head_Flag == True:
                    if "\\n" in word:
                        output_File.write("\n")
                    output_File.write(word.replace("\\n", "") + " ")
            
        