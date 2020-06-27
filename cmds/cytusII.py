import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class CytusII(Cog_Extension):


    @commands.command()
    async def c2(self, ctx, *difficulty):
        allist = ["8", "9", "10", "11", "12", "13", "14", "15"]
        diffs = []
        temp = []
        boo = False
        for x in difficulty:
            diffs.append(x)

        for x in diffs:
            if x not in allist:
                boo = True
                temp.append(x)

        diffs = list(set(diffs).difference(set(temp)))

        if diffs == [] and not("all" in difficulty or "ALL" in difficulty):
            embed=discord.Embed(title="錯誤排除", color=0xffe26f)
            embed.add_field(name=".c2", value="請輸入合理的難度喵~(8 ~ 15)", inline=False)
            await ctx.send(embed=embed)
            return

        if "all" in difficulty or "ALL" in difficulty:
            resultdiff = random.choice(allist)
            boo = False
        else:
            resultdiff = random.choice(diffs)
        
        if boo:
            embed=discord.Embed(title="錯誤警告", color=0xffe26f)
            embed.add_field(name=".c2", value="出現了無法識別的難度喵~已自動排除了喵~\n你再亂打啊喵~本喵沒在理你的喵!!", inline=False)
            await ctx.send(embed=embed)
            
        keyword = "c2lv" + resultdiff + "songs"
        random_song = random.choice(jdata[keyword])

        embed=discord.Embed(title="選擇困難症喵?", description="讓本喵來幫你喵:", color=0xffe26f)
        embed.set_image(url=(random_song))
        await ctx.send(embed=embed)

    @commands.command()
    async def c2bomb(self, ctx, amount, *difficulty):
        try:
            amount = int(amount)
        except:
            embed=discord.Embed(title="錯誤排除", color=0xffe26f)
            embed.add_field(name=".c2bomb", value="請輸入合理的數量喵~(2 ~ 5)", inline=False)
            await ctx.send(embed=embed)
            return

        if 1 < amount <= 5:

            allist = ["8", "9", "10", "11", "12", "13", "14", "15"]
            diffs = []
            temp = []
            boo = False
            for x in difficulty:
                diffs.append(x)

            for x in diffs:
                if x not in allist:
                    boo = True
                    temp.append(x)

            diffs = list(set(diffs).difference(set(temp)))

            if diffs == [] and not("all" in difficulty or "ALL" in difficulty):
                embed=discord.Embed(title="錯誤排除", color=0xffe26f)
                embed.add_field(name=".c2bomb", value="請輸入合理的難度喵~(8 ~ 15)", inline=False)
                await ctx.send(embed=embed)
                return

            if ((amount == 4) or (amount == 5)) and (len(diffs) == 1) and (diffs[0] == "8"):
                await ctx.send("8級只有3首喵~\n")
                await ctx.send("<:Gcat3:711805083695710228>")
                return
            
            songs = []

            if "all" in difficulty or "ALL" in difficulty:
                boo = False
                nowdiff = random.choice(allist)
            else:
                nowdiff = random.choice(diffs)

            if boo:
                embed=discord.Embed(title="錯誤警告", color=0xffe26f)
                embed.add_field(name=".c2bomb", value="出現了無法識別的難度喵~已自動排除了喵~\n你再亂打啊喵~本喵沒在理你的喵!!", inline=False)
                await ctx.send(embed=embed)

            nowkeyword = "c2lv" + nowdiff + "songs"
            now = random.choice(jdata[nowkeyword])
            songs.append(now)
            i = 0
            while i < (amount - 1):
                if "all" in difficulty or "ALL" in difficulty:
                    allist = ["8", "9", "10", "11", "12", "13", "14", "15"]
                    nowdiff = random.choice(allist)
                else:
                    nowdiff = random.choice(diffs)
                nowkeyword = "c2lv" + nowdiff + "songs"
                now = random.choice(jdata[nowkeyword])
                if now in songs:
                    continue
                else:
                    songs.append(now)
                    i+=1

            i = 0
            for i in range(amount):
                if i == 0:
                    embed=discord.Embed(title="選擇困難症喵?", description="讓本喵來幫你喵:", color=0xffe26f)
                else:
                    embed=discord.Embed(color=0xffe26f)
                random_song = songs[i]
                embed.set_image(url=(random_song + '.jpg'))
                await ctx.send(embed=embed)

        else:
            embed=discord.Embed(title="錯誤排除", color=0xffe26f)
            embed.add_field(name=".c2bomb", value="請輸入合理的數量喵~(2 ~ 5)", inline=False)
            await ctx.send(embed=embed)
            return


def setup(bot):
    bot.add_cog(CytusII(bot))