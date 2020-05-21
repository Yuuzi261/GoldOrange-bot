import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json


with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Arcaea(Cog_Extension):

    @commands.command()
    async def arc9p(self, ctx):
        random_song = random.choice(jdata["arc9+songs"])
        await ctx.send(f'選擇困難症喵?讓本喵來幫你喵:\n{random_song}') 

    @commands.command()
    async def arc10(self, ctx):
        random_song = random.choice(jdata["arc10songs"])
        await ctx.send(f'選擇困難症喵?讓本喵來幫你喵:\n{random_song}')  


def setup(bot):
    bot.add_cog(Arcaea(bot))