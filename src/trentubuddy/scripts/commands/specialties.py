#Commands for contact and children

import discord
from discord.ext import commands
import json
import helper.cross_platform as cp

class Specialties(commands.Cog):

    def __init__(self, bot):
        self.bot = bot   
    
    @commands.command(case_insensitive=True)
    async def specialties(self, ctx):
        file = open(cp.os_path_helper(".\\data\\specialties.json"))
        content = json.load(file)
        file.close()
        for specialty_key, specialty_value in content.items():
            embed=discord.Embed(title=specialty_key, color=0x3a8d34)
            embed.add_field(name="Requirements", value=specialty_value, inline=False)
            await ctx.send(embed=embed)      

#Required to add the functions
async def setup(bot):
    await bot.add_cog(Specialties(bot))