import discord
from discord.ext import commands
import json
import random
import os

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= '.')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('.help → 獲得幫助'))
    print(">> Bot is online <<")
    
@bot.event
async def on_member_join(member: discord.Member):
    if member.guild.id == jdata["sever_ID"]:
        channel = bot.get_channel(jdata["welcome_channel"])
        await channel.send(f"**{member}**歡迎喵~")

@bot.event
async def on_member_remove(member: discord.Member):
    if member.guild.id == jdata["sever_ID"]:
        channel = bot.get_channel(jdata["welcome_channel"])
        await channel.send(f"抓到了喵!!**{member}**在偷尻喵~")

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'學習了 **{extension}** 指令包!!奇怪的知識增加了喵~')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'少了 **{extension}** 指令包，本喵現在覺得一身輕喵~')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Re - Loaded {extension} done.')

bot.remove_command('help')
@bot.command()
async def help(ctx, *comad):
    if comad:
        embed=discord.Embed(title="指令查詢", color=0xffe26f)
        if comad[0] == 'arc':
            embed.add_field(name="Arcaea", value=".arc <amount> 抽取隨機Arcaea歌曲", inline=False)
        elif comad[0] == 'arcbomb':
            embed.add_field(name="Arcaea", value=".arcbomb <amount> [difficulty...] 連續抽取2~5首Arcaea歌曲", inline=False)
        elif comad[0] == 'member':
            embed.add_field(name="Common", value=".member 顯示當前群組人數", inline=False)
        elif comad[0] == 'mj':
            embed.add_field(name="Common", value=".mj <name> 查詢成員進入伺服器時間", inline=False)
        elif comad[0] == 'ping':
            embed.add_field(name="Common", value=".ping 查詢現在bot的延遲", inline=False)
        elif comad[0] == 'say':
            embed.add_field(name="Common", value=".say <msg> 讓bot重複訊息", inline=False)
        elif comad[0] == 'choose':
            embed.add_field(name="Random", value=".choose [anything...]隨機選擇輸入的文字", inline=False)
        elif comad[0] == 'mora':
            embed.add_field(name="Random", value=".mora 猜拳", inline=False)
        elif comad[0] == 'rs':
            embed.add_field(name="Random", value=".rs <num_of_people> <group_amount> <role> 隨機分隊", inline=False)
        elif comad[0] == 'rn':
            embed.add_field(name="Random", value=".rn <amount> <low> <top> 指定區間內隨機數字抽取", inline=False)
        else:
            embed.add_field(name="Not Found", value="查無此指令", inline=False)
    
        await ctx.send(embed=embed)    
        
    else:   
        embed=discord.Embed(title="桔喵小助手", description="指令查詢", color=0xffe26f)
        embed.set_thumbnail(url="https://i.imgur.com/pms8YGV.png")
        embed.add_field(name="Arcaea", value="arc | arcbomb", inline=False)
        embed.add_field(name="Common", value="member | mj | ping | say", inline=False)
        embed.add_field(name="Random", value="choose | mora | rs | rn", inline=False)
        embed.set_footer(text="使用.help <cmd>來查詢你想了解的指令")
        await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    embed=discord.Embed(title="ERROR", color=0xffe26f)

    if isinstance(error, commands.errors.CommandNotFound):
        return
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        embed.add_field(name="缺少必要參數", value="你什麼都不說是要本喵怎麼辦喵?", inline=False)
    elif isinstance(error, commands.errors.BadArgument):
        embed.add_field(name="型態錯誤或不明的參數", value="找遍了本喵的資料庫也幫不了你了喵~", inline=False)
    elif isinstance(error, commands.errors.CommandInvokeError):
        embed.add_field(name="呼叫指令時出現例外狀況", value="你...你...你...罰你去看.help喵!!", inline=False)
    else:
        embed.add_field(name="發生錯誤", value="本喵什麼都不知道喵~", inline=False)
        embed.add_field(name="錯誤訊息", value=error, inline=False)

    embed.set_footer(text="使用.help <cmd>來查詢你想了解的指令")
    await ctx.send(embed=embed)

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}') 

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])