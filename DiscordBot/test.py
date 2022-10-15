import os
import discord
TOKEN = '77KaI7erB_JqWGwqLqJCbADuWze5XHMX'
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)