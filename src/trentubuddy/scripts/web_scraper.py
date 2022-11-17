from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import re
import json

results_array = []

#convert the array to a dict once formatted with key value pairs to save to a JSON file
results_dict = {}

url = 'https://www.trentu.ca/cois/programs/degree-computer-science/specializations'
html_container = "div"
#The class tag to search (within the container html_container)
class_tag = "field-item even"

#HTML tags we want to keep
header_tags = {"h1", "h2", "h3", "h4", "h5", "h6"}
list_tags = {"li"}

#merge the dictionaries to start with a full list to search by first then sellect one or the other
all_tags = header_tags.copy()
all_tags.update(list_tags)

def Store_Data(dict_to_save):
    with open("./data/specialties.json", "w") as file:
        json.dump(dict_to_save, file, indent=4)

#initialize a driver with the destination url and headless option (No GUI)
def Setup_Driver(destinationUrl):
    options = Options()
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    driver.get(destinationUrl)
    return driver

#Initialize beautiful soup as an object of the drivers page source
def BeautifulSoupSetup(input_driver):
    return BeautifulSoup(input_driver.page_source, "html.parser")

soup = BeautifulSoupSetup(Setup_Driver(url))

div_container = soup.find(html_container, class_ = class_tag)

#initialize a driver with the destination url and headless option (No GUI)
def Setup_Driver(destinationUrl):
    options = Options()
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),options=options)
    driver.get(destinationUrl)
    return driver

def main():
    specialty_title = ""
    requirements_list = []

    for html_tag in div_container.find_all(all_tags):
        print(html_tag.contents[0])
        if html_tag.name in header_tags:
            #wait for one full iteration first
            if specialty_title != "":
                results_dict[specialty_title] = requirements_list 
            requirements_list = []                               
            specialty_title = html_tag.contents[0]
        #if end of loop do the last add last iteration
        elif html_tag == div_container.find_all(all_tags)[-1]:
            requirements_list.append(html_tag.contents[0].text)
            results_dict[specialty_title] = requirements_list
        else:            
            requirements_list.append(html_tag.contents[0].text)
        
    Store_Data(results_dict)
    
if __name__ == "__main__":
    main()
