import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Tool(Cog_Extension):

    @commands.command()
    async def cal(self, ctx, formula):
        ans = eval(formula)
        embed=discord.Embed(title="The answer is", description = f':small_orange_diamond: **{ans}**',color=0xffe26f)
        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Tool(bot))