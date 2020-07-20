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

iwb = load_workbook('item.xlsx')
iws = iwb.active
k = -1

class Fun(Cog_Extension):
    global iwb, iws

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def pick(self, ctx):
        count(ctx)
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(ctx.author.id):
                    I = ['B', 'C', 'D', 'E', 'F', 'G']
                    it = random.choice(I)
                    iws[it + str(i+1)].value+=1
                    await ctx.send(f'You pick up a **{iws[it + "1"].value}**!')
                    break
                else:
                    if i == a:
                        iws['A1'].value = int(iws['A1'].value) + 1
                        iws.append([-1, 0, 0, 0 ,0 ,0 ,0])
                        iws['A' + str(i+2)].value = str(ctx.author.id)
                        I = ['B', 'C', 'D', 'E', 'F', 'G']
                        it = random.choice(I)
                        iws[it + str(i+2)].value+=1
                        await ctx.send(f'You pick up a **{iws[it + "1"].value}**!')
        else:
            iws['A1'].value = 1
            iws.append([-1, 0, 0, 0 ,0 ,0 ,0])
            iws['A2'].value = str(ctx.author.id)
            I = ['B', 'C', 'D', 'E', 'F', 'G']
            it = random.choice(I)
            iws[it + '2'].value+=1
            await ctx.send(f'You pick up a **{iws[it + "1"].value}**!')

        iwb.save('item.xlsx')
        iwb.close()

    @commands.group()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sell(self, ctx):
        global k
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(ctx.author.id):
                    k = i+1
                    break
                else:
                    await ctx.send('You don\'t have any property')
        else:
            await ctx.send('can\'t find any user')
        embed=discord.Embed(title="Sell", color=0xffe26f)

    @sell.command()
    async def Copper(self, ctx):
        iws['B' + str(k)].value += (iws['C' + str(k)].value)*2
        iws['C' + str(k)].value = 0
        iwb.save('item.xlsx')
        await ctx.send('Copper sell successfully!')

    @sell.command()
    async def Sliver(self, ctx):
        iws['B' + str(k)].value += (iws['D' + str(k)].value)*20
        iws['D' + str(k)].value = 0
        iwb.save('item.xlsx')
        await ctx.send('Sliver sell successfully!')

    @sell.command()
    async def Gold(self, ctx):
        iws['B' + str(k)].value += (iws['E' + str(k)].value)*200
        iws['E' + str(k)].value = 0
        iwb.save('item.xlsx')
        await ctx.send('Gold sell successfully!')

    @sell.command()
    async def Diamond(self, ctx):
        iws['B' + str(k)].value += (iws['F' + str(k)].value)*2000
        iws['F' + str(k)].value = 0
        iwb.save('item.xlsx')
        await ctx.send('Diamond sell successfully!')

    @sell.command()
    async def MG(self, ctx):
        iws['B' + str(k)].value += (iws['G' + str(k)].value)*20000
        iws['G' + str(k)].value = 0
        iwb.save('item.xlsx')
        await ctx.send('Miracle Gem sell successfully!')



def setup(bot):
    bot.add_cog(Fun(bot))