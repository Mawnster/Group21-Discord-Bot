#To pause for testing
import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Gets cwd so that on any machine it will download the file directly to 
download_dir = os.getcwd() + "\\TrentUAC"

#changing the options to allow for chrome to download the file to the CWD instead of opening it
#adapted from https://stackoverflow.com/questions/53998690/downloading-a-pdf-using-selenium-chrome-and-python
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('prefs', {"plugins.always_open_pdf_externally": True,
                                                "download.default_directory": download_dir,
                                                "download.prompt_for_download": False,
                                                "download.directory_upgrade": True,})

#Instead of having a full chrome install we can use this to launch come
#append the defined options to chrome when opening
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)

#Static URL of the web page we are scraping, This shouldn't ever change
url = 'https://www.trentu.ca/registrar/academic-calendar/undergraduate-calendar'

#Launches the url and gives a few seconds to process. 
driver.get(url)
time.sleep(3)
#using the xpath even when the PDF gets updated the button will still lead to the new one every time
driver.find_element('xpath', '//*[@id="block-system-main"]/div/div/div/div/p[1]/a').click()
time.sleep(6)


#this will delete the old instance of the file and rename the new one appropriately
PDF_Directory = os.getcwd() + "\\TrentUAC"

for file in os.listdir(PDF_Directory):
    if "UpdatedUAC.pdf" in file:
        os.remove(PDF_Directory + "\\" + file)

for file in os.listdir(PDF_Directory):
    if "Undergrad" in file:
        os.rename(PDF_Directory + "\\" + file, PDF_Directory + "\\" + "TrentUAC.pdf")
            