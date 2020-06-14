import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Arcaea(Cog_Extension):


    @commands.command()
    async def arc(self, ctx, *difficulty):
        allist = ["7", "8", "9", "9+", "10", "10+", "11"]
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
            embed.add_field(name=".arc", value="請輸入合理的難度喵~(7 ~ 11)", inline=False)
            await ctx.send(embed=embed)
            return

        if "all" in difficulty or "ALL" in difficulty:
            resultdiff = random.choice(allist)
            boo = False
        else:
            resultdiff = random.choice(diffs)
        
        if boo:
            embed=discord.Embed(title="錯誤警告", color=0xffe26f)
            embed.add_field(name=".arc", value="出現了無法識別的難度喵~已自動排除了喵~\n你再亂打啊喵~本喵沒在理你的喵!!", inline=False)
            await ctx.send(embed=embed)
            
        keyword = "arc" + resultdiff + "songs"
        random_song = random.choice(jdata[keyword])
        await ctx.send(f'選擇困難症喵?讓本喵來幫你喵:\n{random_song}')

    @commands.command()
    async def arcbomb(self, ctx, amount, *difficulty):
        try:
            amount = int(amount)
        except:
            embed=discord.Embed(title="錯誤排除", color=0xffe26f)
            embed.add_field(name=".arcbomb", value="請輸入合理的數量喵~(2 ~ 5)", inline=False)
            await ctx.send(embed=embed)
            return

        if 1 < amount <= 5:

            allist = ["7", "8", "9", "9+", "10", "10+", "11"]
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
                embed.add_field(name=".arcbomb", value="請輸入合理的難度喵~(7 ~ 11)", inline=False)
                await ctx.send(embed=embed)
                return

            if (amount == 5) and (len(diffs) == 1) and (diffs[0] == "11"):
                await ctx.send("11級只有4首喵~\n")
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
                embed.add_field(name=".arcbomb", value="出現了無法識別的難度喵~已自動排除了喵~\n你再亂打啊喵~本喵沒在理你的喵!!", inline=False)
                await ctx.send(embed=embed)

            nowkeyword = "arc" + nowdiff + "songs"
            now = random.choice(jdata[nowkeyword])
            songs.append(now)
            i = 0
            while i < (amount - 1):
                if "all" in difficulty or "ALL" in difficulty:
                    allist = ["7", "8", "9", "9+", "10", "10+", "11"]
                    nowdiff = random.choice(allist)
                else:
                    nowdiff = random.choice(diffs)
                nowkeyword = "arc" + nowdiff + "songs"
                now = random.choice(jdata[nowkeyword])
                if now in songs:
                    continue
                else:
                    songs.append(now)
                    i+=1

            i = 0
            await ctx.send("選擇困難症喵?讓本喵來幫你喵:\n")
            for i in range(amount):
                await ctx.send(f'{songs[i]}')

        else:
            await ctx.send("請輸入2 ~ 5的整數喵~")


def setup(bot):
    bot.add_cog(Arcaea(bot))