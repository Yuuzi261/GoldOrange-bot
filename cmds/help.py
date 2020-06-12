import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Help(Cog_Extension):

    @commands.command()
    async def cmd(self, ctx, comad):
        embed=discord.Embed(title="指令查詢", color=0xffe26f)
        if comad == 'arc':
            embed.add_field(name="Arcaea", value=".arc <amount> 抽取隨機Arcaea歌曲", inline=False)
        elif comad == 'arcbomb':
            embed.add_field(name="Arcaea", value=".arcbomb <amount> [difficulty...] 連續抽取2~5首Arcaea歌曲", inline=False)
        elif comad == 'member':
            embed.add_field(name="Common", value=".member 顯示當前群組人數", inline=False)
        elif comad == 'mj':
            embed.add_field(name="Common", value=".mj <name> 查詢成員進入伺服器時間", inline=False)
        elif comad == 'ping':
            embed.add_field(name="Common", value=".ping 查詢現在bot的延遲", inline=False)
        elif comad == 'say':
            embed.add_field(name="Common", value=".say <msg> 讓bot重複訊息", inline=False)
        elif comad == 'choose':
            embed.add_field(name="Random", value=".choose [anything...]隨機選擇輸入的文字", inline=False)
        elif comad == 'mora':
            embed.add_field(name="Random", value=".mora 猜拳", inline=False)
        elif comad == 'rs':
            embed.add_field(name="Random", value=".rs <num_of_people> <group_amount> <role> 隨機分隊", inline=False)
        else:
            embed.add_field(name="Not Found", value="查無此指令", inline=False)
            
        
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))