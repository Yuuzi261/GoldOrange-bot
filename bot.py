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
    print(">> Bot is online <<")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(509693136247848961)
    await channel.send(f"**{member}**歡迎喵~")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(509693136247848961)
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
async def help(ctx):
    embed=discord.Embed(title="桔喵小助手", description="指令查詢", color=0xffe26f)
    embed.set_thumbnail(url="https://i.imgur.com/pms8YGV.png")
    embed.add_field(name="Arcaea", value="arc | arcbomb", inline=False)
    embed.add_field(name="Common", value="member | mj | ping | say", inline=False)
    embed.add_field(name="Random", value="choose | mora | rs", inline=False)
    embed.set_footer(text="使用.cmd來查詢你想了解的指令")
    await ctx.send(embed=embed)


for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}') 

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])