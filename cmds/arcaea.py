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
        if "all" in difficulty or "ALL" in difficulty:
            allist = ["7", "8", "9", "9+", "10", "10+", "11"]
            resultdiff = random.choice(allist)
        else:
            resultdiff = random.choice(difficulty)
            
        keyword = "arc" + resultdiff + "songs"
        random_song = random.choice(jdata[keyword])
        await ctx.send(f'選擇困難症喵?讓本喵來幫你喵:\n{random_song}')

    @commands.command()
    async def arcbomb(self, ctx, amount, *difficulty):
        amount = int(amount)
        if 1 < amount <= 5:
            songs = []

            if "all" in difficulty or "ALL" in difficulty:
                allist = ["7", "8", "9", "9+", "10", "10+", "11"]
                nowdiff = random.choice(allist)
            else:
                nowdiff = random.choice(difficulty)

            nowkeyword = "arc" + nowdiff + "songs"
            now = random.choice(jdata[nowkeyword])
            songs.append(now)
            i = 0
            while i < (amount - 1):
                if "all" in difficulty or "ALL" in difficulty:
                    allist = ["7", "8", "9", "9+", "10", "10+", "11"]
                    nowdiff = random.choice(allist)
                else:
                    nowdiff = random.choice(difficulty)
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