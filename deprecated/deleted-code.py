#Zach's dad jokes :'( 
# rip in peace, you will be missed
"""
@bot.event
async def on_message(message):
    #check if the message is fron a bot and if so return
    if message.author == bot.user:
        return
    dad_Jokes = [
        # from https://www.countryliving.com/life/a27452412/best-dad-jokes/
        'I\'m afraid for the calendar. Its days are numbered.',
        'My wife said I should do lunges to stay in shape. That would be a big step forward.',
        'Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!',
        'Singing in the shower is fun until you get soap in your mouth. Then it\'s a soap opera.',
        'What do a tick and the Eiffel Tower have in common?" "They\'re both Paris sites.',
        'What do you call a fish wearing a bowtie?" "Sofishticated."',
    ]
    
    if 'tell me a joke' in message.content.lower():
        response = random.choice(dad_Jokes)
        await message.channel.send(response)

"""

"""
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
#intents.message_content = True
intents.members = True

"""