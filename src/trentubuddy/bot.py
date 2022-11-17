# bot.py
# Authors: Zachary Bricknell, Kenzie A
# 
# Desc: This bot is created to utilize the discord.py plugin to assist students in
# finding general information. This is achieved by using web scrapers to compile data
# and display a formatted output of the results. Utilizing Cogs to get those scripts 
# and creating helper functions for both linux and unix systems to run the bot.

#Backlog:

#program requirements // description of classes // 

#course reccommendations?

#logging and storing information // tech with tim on youtube

#if user has an invalid command // shark on stack overflow // needs to be reworked
"""
invalid_command = #userinput
command_list = [#list of your commands]
fuzzy_ratios = []
for command in command_list:
   ratio = fuzzywuzzy.ratio(invalid_command, command)
   fuzzy_ratios.append(ratio)
max_ratio_index = fuzzy_ratios.index(max(fuzzy_ratios))
fuzzy_matched = command_list[max_ratio_index]
return f"did you mean {fuzzy_matched}?"
"""
#select menu for a role // Code with Swastik on YouTube

#roles, opens up new channels 


import scripts.cross_platform as cp
import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from discord.ui import Select

#changes \\ to / if linux system
cog_path = cp.os_path_helper(".\\src\\trentubuddy\\cogs")

#Bot options
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents = discord.Intents.all(), command_prefix = '!', help_command=None, case_insensitive=True)

#get the enviornment variable file
load_dotenv(os.getcwd() + cp.os_path_helper("\\env\\.env"))

TOKEN = os.getenv('DISCORD_TOKEN')

#not fully implemented 
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'commands.{extension}')

#recursively get every extension for every .py file in the path or subdirectories
async def load_extensions(extensions_path, folder_path = "" ):
    if(folder_path == ""):
        #folder path must start at the given rirectory is located so we take the last entry of the input
        folder_path = extensions_path.rsplit(cp.os_path_helper("\\"), 1)[-1]    
    for filename in os.listdir(extensions_path):
        if(os.path.isdir(os.path.join(extensions_path, filename))):
            #recursively load in the new path with a delimiter of "." to be used in load_extension
            await load_extensions(extensions_path + cp.os_path_helper("\\") + filename, folder_path + "." + filename)
        if filename.endswith('.py'):    
            #remove .py for each filename         
            await bot.load_extension(f'{folder_path}.{filename[:-3]}')        
            
#This is the new way to do bot.run(TOKEN) by loading the cogs first.
async def main():
    async with bot:
        await load_extensions(cog_path)
        await bot.start(TOKEN)
        
if __name__ == "__main__":
    asyncio.run(main())  