# bot.py
# Skeleton code obtained from realpython.com - see sources
# added in extra lines from discord.ext import commands
import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

#prefix
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents = discord.Intents.all(), command_prefix = '!', help_command=None)


#allowing for the bot to read events from messages and guilds(servers)
#do not disbale these for now
@bot.event
async def on_guild_join(guild):
    if guild.system_channel:
        await guild.system_channel.send("Test")

load_dotenv(os.getcwd() + "\\env\\.env")

#token is not avialable in GIT
TOKEN = os.getenv('DISCORD_TOKEN')

#not seen by users, displays in terminal if the bot loaded
@bot.event
async def on_ready():
    print(f'{bot.user} TrentU Buddy... ONLINE !!!')


#When someone joins the server they get a direct message  
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, I am your student helper bot \nStarter Commands Here'
    )

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

#making sure that it works with a simple hello - WORKING 11/
@bot.command()
async def hello(ctx):
    await ctx.send("Hi there!")

#will a goodbye work?
@bot.command()
async def goodbye(ctx):
    await ctx.send("pls come back")

#roles, opens up new channels 

#contacting faulty members // hardcoded

#I NEED HELP


    

bot.run(TOKEN)