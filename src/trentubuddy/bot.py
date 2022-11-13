# bot.py
# Skeleton code obtained from realpython.com - see sources
# added in extra lines from discord.ext import commands

#Custom scripts to allow linux support
import helper.cross_platform as cp
import discord
import os
import random
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
from discord.ui import Select

#prefix
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents = discord.Intents.all(), command_prefix = '!', help_command=None, case_insensitive=True)

#Gets the project root and uses the helper function(if linux) to find the .env file and save
load_dotenv(os.getcwd() + cp.os_path_helper("\\env\\.env"))

#token defined in .env
TOKEN = os.getenv('DISCORD_TOKEN')

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
            print(f'{folder_path}.{filename[:-3]}')
            await bot.load_extension(f'{folder_path}.{filename[:-3]}')
            
        
    



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


#making sure that it works with a simple hello - WORKING 11/
@bot.command()
async def hello(ctx):
    await ctx.send("Hi there!")

#will a goodbye work?
@bot.command()
async def goodbye(ctx):
    await ctx.send("pls come back")

#roles, opens up new channels 

#help command // what are all the available functions?

@bot.group(name="help", invoke_without_command=True)
async def help(ctx):
    await ctx.send("Here are the available commands:\n`Hello`: Say hello to the bot \
        \n`Goodbye`: Say goodbye to the bot\n`Contact`: Contact information for COIS faculty members\n`Resources`: Links to different\
 Trent resources\n")

#this is an example of different sub categories that can be in the
#overall bot group. Will use this function for specific faculty members.
@help.command()
async def booking(ctx):
    await ctx.send("Here are the available commands:\n`advising`: Book with Trent's Academic Advising\n\
`skills`: Book with Academic Skills\n`healthinmotion`: Book with Trent Health in Motion\n\
`room`: Book a room at Trent's Peterborough campus\n`travel`: Book with Trent International\n\
`career`: Book with Careerspace\n`peers`: Book with Peer Support\n`coop`: Book with Co-Op")


#Course specializations // hardcoded for now

#program requirements // description of classes // 

#course reccommendations?

#


#logging and storing information // tech with tim on youtube

async def main():
    async with bot:
        await load_extensions(cp.os_path_helper(".\\src\\trentubuddy\\scripts"))
        await bot.start(TOKEN)
#bot.run(TOKEN)

asyncio.run(main())     
