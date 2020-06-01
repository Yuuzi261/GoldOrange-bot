import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Common(Cog_Extension):

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'本喵現在的反應延遲是 **{round(self.bot.latency*1000)}** 毫秒，至少比你的頭腦還要快上 **{round(250/(self.bot.latency*1000),3)}** 倍喵(・∀・)')

    @commands.command()
    async def mora(self, ctx):
        random_result = random.choice(jdata["mora"])
        await ctx.send(f'本喵贏定了喵~\n{random_result}') 

    @commands.command()
    async def choice(self, ctx, *, songs):
        result = random.choice(songs)
        await ctx.send(f'本喵決定選 **{result}** 喵~')


def setup(bot):
    bot.add_cog(Common(bot))