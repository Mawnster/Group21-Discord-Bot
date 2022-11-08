# bot.py
# Skeleton code obtained from realpython.com - see sources
# added in extra lines from discord.ext import commands
import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
from discord.ui import Select

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
async def game(ctx):
    await ctx.send("These are the game commands `rps`")

#ok lets get the party started // contacting faculty

@bot.group(name="contact", invoke_without_command=True)
async def contact(ctx):
    await ctx.send("**COIS Faculty Members\nList Updated: November 08/22\n\
**To access information, please type prefix '!' followed by contact and the LAST name of the\
 faculty member you wish to reach\n`Available Options:`\n\
Richard HURLEY\nWenying FENG\nBrian PATRICK\nSabine McCONNELL\nOmar ALAM\n\
Fadi ALZHOURI\nBrian SRIVASTAVA\nSofie ANDREOU\nJacques BELAND\nBrian HIRCOCK\n\
Jamie MITCHELL\nPeter NORTHROP\nStephen REGOCZEI\nNancy SMITH\nGraeme YOUNG\nElissa ONIELL\nOther")

# works but needs to not be case sensitive
# creds to patrick haugh on stackoverflow
@contact.command()
async def Hurley(ctx):
    embed=discord.Embed(title="Richard Hurley", description="Department Chair and Full-Time Professor", color=0x3a8d34)
    embed.add_field(name="Office Location", value="OC 102.3", inline=True)
    embed.add_field(name="Phone Number", value="(705) 748 1011 ext. 7542", inline=True)
    embed.add_field(name="Email", value="rhurley@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Feng(ctx):
    embed=discord.Embed(title="Wenying Feng", description="Professor", color=0x3a8d34)
    embed.add_field(name="Office Location", value="OC 102.9", inline=True)
    embed.add_field(name="Phone Number", value="(705) 748 1011 ext. 7249", inline=True)
    embed.add_field(name="Email", value="wfeng@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Patrick(ctx):
    embed=discord.Embed(title="Brian Patrick", description="Associate Professor", color=0x3a8d34)
    embed.add_field(name="Office Location", value="OC 102.8", inline=True)
    embed.add_field(name="Phone Number", value="(705) 748 1011 ext. 7804", inline=True)
    embed.add_field(name="Email", value="bpatrick@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def McConnell(ctx):
    embed=discord.Embed(title="Sabine McConnell", description="Associate Professor", color=0x3a8d34)
    embed.add_field(name="Office Location", value="OC 102.7", inline=True)
    embed.add_field(name="Phone Number", value="(705) 748 1011 ext. 7803", inline=True)
    embed.add_field(name="Email", value="sabinemcconnell@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Alam(ctx):
    embed=discord.Embed(title="Omar Alam", description="Assistant Professor", color=0x3a8d34)
    embed.add_field(name="Phone Number", value="(705) 748 1011 ext. 7347", inline=True)
    embed.add_field(name="Email", value="omaralam@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Alzhouri(ctx):
    embed=discord.Embed(title="Fadi Alzhouri", description="Assistant Professor", color=0x3a8d34)
    embed.add_field(name="Phone Number", value="(705) 748 1011 ext. 7750", inline=True)
    embed.add_field(name="Email", value="fadialzhouri@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Sri(ctx):
    embed=discord.Embed(title="Brian Srivastava", description="Lecturer", color=0x3a8d34)
    embed.add_field(name="Office Location", value="OC 102.6", inline=True)
    embed.add_field(name="Phone Number", value="(705) 748 1011", inline=True)
    embed.add_field(name="Email", value="bsrivastava@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Andreou(ctx):
    embed=discord.Embed(title="Sofie Andreou", color=0x3a8d34)
    embed.add_field(name="Email", value="sofieandreou@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Beland(ctx):
    embed=discord.Embed(title="Jacques Beland", color=0x3a8d34)
    embed.add_field(name="Email", value="jacquesbeland@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Hircock(ctx):
    embed=discord.Embed(title="Brian Hircock", color=0x3a8d34)
    embed.add_field(name="Email", value="bhircock@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Mitchell(ctx):
    embed=discord.Embed(title="Jamie Mitchell", color=0x3a8d34)
    embed.add_field(name="Email", value="jamiemitchell@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Northrop(ctx):
    embed=discord.Embed(title="Peter Northrop", color=0x3a8d34)
    embed.add_field(name="Email", value="pnorthrop@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Regoczei(ctx):
    embed=discord.Embed(title="Stephen Regoczei", color=0x3a8d34)
    embed.add_field(name="Email", value="sregoczei@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Smith(ctx):
    embed=discord.Embed(title="Nancy Smith", color=0x3a8d34)
    embed.add_field(name="Email", value="nmsmith@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Young(ctx):
    embed=discord.Embed(title="Graeme Young", color=0x3a8d34)
    embed.add_field(name="Email", value="gyoung@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def ONeill(ctx):
    embed=discord.Embed(title="Elissa O'Neill", description="Academic Administrative Assistant", color=0x3a8d34)
    embed.add_field(name="Office Location", value="OC 102.6", inline=True)
    embed.add_field(name="Phone Number", value="(705) 748 1011 ext. 7802", inline=True)
    embed.add_field(name="Email", value="cois@trentu.ca", inline=False)
    await ctx.send(embed=embed)

@contact.command()
async def Other(ctx):
    embed=discord.Embed(title="Other Contacts", color=0x3a8d34)
    embed.add_field(name="COIS General Inquiries Email", value="cois@trentu.ca", inline=False)
    embed.add_field(name="COIS Jobs", value="coisjobs@trentu.ca", inline=False)
    await ctx.send(embed=embed)


bot.run(TOKEN)