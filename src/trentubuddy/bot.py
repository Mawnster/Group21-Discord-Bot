# bot.py
# Authors: Zachary Bricknell, Kenzie A
# 
# Desc: This bot is created to utilize the discord.py plugin to assist students in
# finding general information. This is achieved by using web scrapers to compile data
# and display a formatted output of the results. Utilizing Cogs to get those scripts 
# and creating helper functions for both linux and unix systems to run the bot.

from scripts import helpers as helper
import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

#changes \\ to / if linux system
cog_path = os.path.dirname(os.path.realpath(__file__)) + helper.os_path_helper("\\cogs")

#Bot options
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents = discord.Intents.all(), command_prefix = '!', help_command=None, case_insensitive=True)

#get the files path (bot.py) and append the env folder for portability
load_dotenv(os.path.dirname(os.path.realpath(__file__)) + helper.os_path_helper("\\env\\.env"))

TOKEN = os.getenv('DISCORD_TOKEN')

#not fully implemented 
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'commands.{extension}')

#recursively get every extension for every .py file in the path or subdirectories as well as 
#use the apporpriate structure for cogs with a "." to join the path
async def load_extensions(extensions_path, folder_path = "" ):
    if(folder_path == ""):
        #folder path must start at the given rirectory is located so we take the last entry of the input
        folder_path = extensions_path.rsplit(helper.os_path_helper("\\"), 1)[-1]    
    for filename in os.listdir(extensions_path):
        if(os.path.isdir(os.path.join(extensions_path, filename))):
            #recursively load in the new path with a delimiter of "." to be used in load_extension
            await load_extensions(extensions_path + helper.os_path_helper("\\") + filename, folder_path + "." + filename)
        if filename.endswith('.py'):    
            #remove .py for each filename         
            await bot.load_extension(f'{folder_path}.{filename[:-3]}')        
            
#This is the new way to do bot.run(TOKEN) by loading the cogs first.
async def main():
    await load_bot()

#To be called from __main__.py to execute this script.
async def load_bot():
    async with bot:
        await load_extensions(cog_path)
        await bot.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())  