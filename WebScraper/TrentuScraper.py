import requests
from bs4 import BeautifulSoup

#The URL we are looking to scrap
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

#required by the library 
soup = BeautifulSoup(page.content, "html.parser")

#searching only the main container on the website
results = soup.find(id="ResultsContainer")

#get all the div tags labeled card-content
job_elements = results.find_all("div", class_="card-content")

#Iterate over all the results and extract just the title location and company
#Then only output the text, and strip the whitespace
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
    
    