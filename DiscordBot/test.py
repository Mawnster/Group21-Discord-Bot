import os
import discord
TOKEN = 'MTAzMDU0OTk5Nzk2OTczOTc4Ng.G_Cz6P.EQeQvpxO_58GhBG8WaSZPDUbhp_W1KxNYqp29A'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)