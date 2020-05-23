import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Common(Cog_Extension):


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'本喵現在的反應延遲是 **{round(self.bot.latency*1000)}** 毫秒，至少比你的頭腦還要快上 **{round(250/(self.bot.latency*1000),3)}** 倍喵(・∀・)')


def setup(bot):
    bot.add_cog(Common(bot))