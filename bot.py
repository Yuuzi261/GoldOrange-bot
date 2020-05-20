import discord
from discord.ext import commands
import json
import random

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= 'c!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.command()
async def arc9p(ctx):
    random_song = random.choice(jdata["arc9+songs"])
    await ctx.send(f'選擇困難症喵?讓本喵來幫你喵:\n{random_song}喵!!') 

@bot.command()
async def arc10(ctx):
    random_song = random.choice(jdata["arc10songs"])
    await ctx.send(f'選擇困難症喵?讓本喵來幫你喵:\n{random_song}喵!!')  

bot.run(jdata["TOKEN"])