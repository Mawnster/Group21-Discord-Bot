#Commands for contact and children

import discord
from discord.ext import commands
import json
import scripts.helpers as helper
import scripts.cs_specialty_scraper as cs_specialties
import scripts.ac_link_scraiper as academic_calendar
import os

path_to_data = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../../data")
class Specialties(commands.Cog):

    def __init__(self, bot):
        self.bot = bot   
    
    @commands.command()
    async def testt(self, ctx):
        await ctx.send("HEH TESTED...")

    @commands.command(case_insensitive=True, aliases=["sp"])
    async def specialties(self, ctx):  
           
        if(helper.SinceLastModified(path_to_data + "/specialties.json") > 1):
            await ctx.send("Let me get that information for you...")
            if cs_specialties.update_specialties() != 0:
                await ctx.send("Error fetching information...")
                return
        file = open(helper.os_path_helper(path_to_data + "/specialties.json"))
        content = json.load(file)
        file.close()
        for specialty_key, specialty_value in content.items():
            embed=discord.Embed(title=specialty_key, color=0x3a8d34)            
            embed.add_field(name="Requirements:", value="\n\n".join(specialty_value), inline=False)
            await ctx.send(embed=embed)     

    @commands.command(case_insensitive=True, aliases=["academiccalendar", "academic_calendar", "a_c"])
    async def ac(self, ctx):
        delete_timer = 30.0        
        if(helper.SinceLastModified(path_to_data + "/ac_link.json") > 1):
            await ctx.send("Let me get that information for you...", delete_after=delete_timer)
            if academic_calendar.get_ac_link() != 0:
                await ctx.send("Error fetching information...", delete_after=delete_timer)
                return
        file = open(helper.os_path_helper(path_to_data + "/ac_link.json"))
        content = json.load(file)
        file.close()
        for specialty_key, specialty_value in content.items():
            embed=discord.Embed(title=specialty_key, color=0x3a8d34, url=specialty_value)            
            await ctx.send(embed=embed, delete_after=delete_timer) 
            #only one item in the dict
            return   

#Required to add the functions
async def setup(bot):
    await bot.add_cog(Specialties(bot))