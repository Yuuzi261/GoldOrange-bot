import discord
from discord.ext import commands
from openpyxl import load_workbook
from core.classes import Cog_Extension
import random
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

def count(c):
    wb = load_workbook('cmdcount.xlsx')
    ws = wb.active
    if ws['A1'].value != None:
        a = int(ws['A1'].value)
        for i in range(a):
            if str(ws['B' + str(i+1)].value) == str(c.author.id):
                ws['C' + str(i+1)].value = int(ws['C' + str(i+1)].value) + 1
                break
            else:
                if i == (a-1):
                    ws['A1'].value = int(ws['A1'].value) + 1
                    ws['B' + str(i+2)].value = str(c.author.id)
                    ws['C' + str(i+2)].value = 1
    else:
        ws['A1'].value = 1
        ws['B1'].value = str(c.author.id)
        ws['C1'].value = 1

    wb.save('cmdcount.xlsx')
    wb.close()

class Tool(Cog_Extension):

    @commands.command()
    async def cal(self, ctx, formula):
        count(ctx)
        ans = eval(formula)
        embed=discord.Embed(title="The answer is", description = f':small_orange_diamond: **{ans}**',color=0xffe26f)
        await ctx.send(embed=embed)

    @commands.command()
    async def cnt(self, ctx, name: discord.Member):
        wb = load_workbook('cmdcount.xlsx')
        ws = wb.active
        if ws['A1'].value != None:
            a = int(ws['A1'].value)
            for i in range(a):
                if str(ws['B' + str(i+1)].value) == str(name.id):
                    if name.nick != None:
                        embed=discord.Embed(title="YO!!", description = f'{name.nick} have used commands **{ws["C" + str(i+1)].value}** times~',color=0xffe26f)
                    else:
                        embed=discord.Embed(title="YO!!", description = f'{name} have used commands **{ws["C" + str(i+1)].value}** times~',color=0xffe26f)
                    embed.set_footer(text="GOOD JOB MEOW!")
                    break
                else:
                    if i == (a-1):
                        if name.nick != None:
                            embed=discord.Embed(title="OH~", description = f'It seems that **{name.nick}** hasn\'t use commands yet meow!',color=0xffe26f)
                        else:
                            embed=discord.Embed(title="OH~", description = f'It seems that **{name}** hasn\'t use commands yet meow!',color=0xffe26f)
        else:
            embed=discord.Embed(title="Humm...", description = f'I can\'t find any user in my data meow',color=0xffe26f)

        await ctx.send(embed=embed)
        wb.close()



def setup(bot):
    bot.add_cog(Tool(bot))