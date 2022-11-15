Project created and maintained by Zachary B and Kenzie A

##Description##

This discord bot utilizes popular frameworks such as discord.py, cogs, selenium and beautiful soup. The goal is to create a faster and more convenient way to navigate and retrieve informationf from "trentu.ca". 

Using senenium and beautiful soup 4 we can parse HTML from the website and retrieve information. The information retrieved is dynamic so it will grab any information updated by JS. It saves this file as a dictionary and dumps it into a .json file for the bot to grab later

The bot file will call multiple script files for listeners, commands and if needed to run the script to update the .json files as need. It will then display the information in a readable embed for the user.

We chose discord as it is a popular platform use by many people, but also cuts out the idea of remaking a website or creating a new front end. 

This is a proof of concept.



##Setup##

Highly recomended to use a virutal enviornment for python to install packages on. We used venv.

Must get a bot set up throguh discord and save the token in a file called .env and it env foler

Must install dependencies which are included in the package we created using PIP
pip install trentubuddy

Currently deployable on both windows and linux systems (tested on linux mint)




