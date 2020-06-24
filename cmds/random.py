import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Random(Cog_Extension):

    @commands.command()
    async def mora(self, ctx):
        random_result = random.choice(jdata["mora"])
        embed=discord.Embed(title="本喵贏定了喵~", color=0xffe26f)
        embed.set_image(url=(random_result + '.jpg'))
        await ctx.send(embed=embed)

    @commands.command()
    async def choose(self, ctx, *songs):
        result = random.choice(songs)
        embed=discord.Embed(title="Result", description = f'本喵決定選 **{result}** 喵~', color=0xffe26f)
        await ctx.send(embed=embed)

    @commands.command()
    async def rs(self, ctx, num_of_people, group_amount, role: discord.Role):
        num = int(num_of_people)
        gamount = int(group_amount)
        if num % gamount == 0:
            people = []
            for member in ctx.guild.members:
                if role in member.roles:
                    people.append(member.name)
        
            selected_people = random.sample(people, k=num)

            embed=discord.Embed(title="隨機分隊", color=0xffe26f)
        
            for squad in range(gamount):
                a = random.sample(selected_people, k = (num//gamount))
                msg = " "
                for name in a:
                    msg = msg + name + ' , '
                embed.add_field(name=f'第**{squad+1}**小隊:', value=msg[:-3], inline=False)
                for name in a:
                    selected_people.remove(name)

            await ctx.send(embed=embed)
        else:
            await ctx.send("請輸入合理的分組喵~")


def setup(bot):
    bot.add_cog(Random(bot))