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
    async def choice(self, ctx, *songs):
        result = random.choice(songs)
        await ctx.send(f'本喵決定選 **{result}** 喵~')

    @commands.command()
    async def spthx(self, ctx):
        await ctx.send("```\n【特別感謝】\n本喵的主要開發者是 金桔 喵~\n目前沒有其它的共同開發者喵！\n特別感謝以下的人協助開發喵(ㆁωㆁ)\n•Proladon以及其他所有SHELTER ZONE的大佬\n    感謝協助Debug以及提供教學喵\n•小杰\n    感謝提供arcaea所有歌曲圖片喵\n•最後感謝所有群內幫助測試以及提供意見的人員喵\n```")

    @commands.command()
    async def say(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def rand_squad(self, ctx, num_of_people, group_amount, role: discord.Role):
        num = int(num_of_people)
        gamount = int(group_amount)
        if num % gamount == 0:
            people = []
            for member in ctx.guild.members:
                if role in member.roles:
                    people.append(member.name)
        
            selected_people = random.sample(people, k=num)

            for squad in range(gamount):
                a = random.sample(selected_people, k = (num//gamount))
                msg = " "
                for name in a:
                    msg = msg + name + ' , '
                await ctx.send(f'第**{squad+1}**小隊:' + msg[:-3])
                for name in a:
                    selected_people.remove(name)
        else:
            await ctx.send("請輸入合理的分組喵~")
                


def setup(bot):
    bot.add_cog(Common(bot))