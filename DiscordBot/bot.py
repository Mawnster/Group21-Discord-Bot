# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
#token is not avialable in GIT
TOKEN = os.getenv('DISCORD_TOKEN')

#intents is required for all discord versions past 1.7.3 left 
#default for now
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} Heh....It works...')

client.run(TOKEN)