import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix= 'cat!')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run(jdata["TOKEN"])