#Commands for contact and children

import discord
from discord.ext import commands
import json
import scripts.helpers as helper
import scripts.cs_specialty_scraper as cs_specialties
import scripts.ac_link_scraiper as academic_calendar

class Specialties(commands.Cog):

    def __init__(self, bot):
        self.bot = bot   
    
    @commands.command(case_insensitive=True)
    async def specialties(self, ctx):
        await ctx.send("Let me get that information for you...")
        if(helper.SinceLastModified(".\\data\\specialties.json") > 1):
            if cs_specialties.update_specialties() != 0:
                await ctx.send("Error fetching information...")
                return
        file = open(helper.os_path_helper(".\\data\\specialties.json"))
        content = json.load(file)
        file.close()
        for specialty_key, specialty_value in content.items():
            embed=discord.Embed(title=specialty_key, color=0x3a8d34)            
            embed.add_field(name="Requirements:", value="\n\n".join(specialty_value), inline=False)
            await ctx.send(embed=embed)     

    @commands.command(case_insensitive=True, aliases=["academiccalendar", "academic_calendar", "a_c"])
    async def ac(self, ctx):
        await ctx.send("Let me get that information for you...")
        if(helper.SinceLastModified(".\\data\\ac_link.json") > 1):
            if academic_calendar.get_ac_link() != 0:
                await ctx.send("Error fetching information...")
                return
        file = open(helper.os_path_helper(".\\data\\ac_link.json"))
        content = json.load(file)
        file.close()
        for specialty_key, specialty_value in content.items():
            embed=discord.Embed(title=specialty_key, color=0x3a8d34)            
            embed.add_field(name="Link:", value=specialty_value, inline=False)
            await ctx.send(embed=embed) 
            return   

#Required to add the functions
async def setup(bot):
    await bot.add_cog(Specialties(bot))