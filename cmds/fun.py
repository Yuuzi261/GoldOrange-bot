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

def pickcount(c):
    wb = load_workbook('item.xlsx')
    ws = wb.active
    if iws['A1'].value != None:
        a = int(iws['A1'].value)
        for i in range(1, a + 1):
            if str(iws['A' + str(i+1)].value) == str(c.author.id):
                iws['I' + str(i+1)].value += 1
                break

    iwb.save('item.xlsx')

def mine():
    r = random.randint(1, 100)
    num = 0
    I = ['B', 'C', 'D', 'E', 'F', 'G']
    if r < 25:
        it = random.choice(I[:3])
        if it == 'B':
            num = 100
        else:
            num = 5 * 10**(2 - (ord(it) - ord('B')))
    elif r < 45:
        it = random.choice(I[:4])
        if it == 'B':
            num = 200
        else:
            num = 1 * 10**(3 - (ord(it) - ord('B')))
    elif r < 60:
        it = random.choice(I[:3])
        if it == 'B':
            num = 500
        else:
            num = 25 * 10**(2 - (ord(it) - ord('B')))
    elif r < 72:
        it = random.choice(I[:4])
        if it == 'B':
            num = 1000
        else:
            num = 5 * 10**(3 - (ord(it) - ord('B')))
    elif r < 82:
        it = random.choice(I[:3])
        if it == 'B':
            num = 1500
        else:
            num = 75 * 10**(2 - (ord(it) - ord('B')))
    elif r < 89:
        it = random.choice(I[:5])
        if it == 'B':
            num = 2000
        else:
            num = 1 * 10**(4 - (ord(it) - ord('B')))
    elif r < 94:
        it = random.choice(I[:4])
        if it == 'B':
            num = 5000
        else:
            num = 25 * 10**(3 - (ord(it) - ord('B')))
    elif r < 97:
        it = random.choice(I[:5])
        if it == 'B':
            num = 10000
        else:
            num = 5 * 10**(4 - (ord(it) - ord('B')))
    elif r < 99:
        it = random.choice(I[:4])
        if it == 'B':
            num = 15000
        else:
            num = 75 * 10**(3 - (ord(it) - ord('B')))
    else:
        it = random.choice(I)
        if it == 'B':
            num = 20000
        else:
            num = 1 * 10**(5 - (ord(it) - ord('B')))

    return it, num

iwb = load_workbook('item.xlsx')
iws = iwb.active
k = -1

class Fun(Cog_Extension):
    global iwb, iws

    @commands.command()
    @commands.is_owner()
    async def system_give(self, ctx, amount: int, typee, name: discord.Member = None):
        count(ctx)
        if name == None:
            if iws['A1'].value != None:
                a = int(iws['A1'].value)
                for i in range(1, a + 1):
                    iws[typee + str(i+1)].value += amount
            else:
                await ctx.send('can\'t find any user')

            await ctx.send(f'Give EVERYONE **{amount} {iws[typee + "1"].value}** meow!!')
        else:
            if iws['A1'].value != None:
                a = int(iws['A1'].value)
                for i in range(1, a + 1):
                    if str(iws['A' + str(i+1)].value) == str(name.id):
                        iws[typee + str(i+1)].value += amount
                        await ctx.send(f'Give **{name} {amount} {iws[typee + "1"].value}** meow!!')
                        break
                    else:
                        if i == a:
                            await ctx.send('Can\'t find the user meow')
                else:
                    await ctx.send('can\'t find any user')
            
        iwb.save('item.xlsx')

    @commands.command()
    @commands.is_owner()
    async def system_bag(self, ctx, name: discord.Member):
        count(ctx)
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(name.id):
                    I = ['B', 'C', 'D', 'E', 'F', 'G']
                    embed=discord.Embed(title=f'{name}\'s backpack',color=0xffe26f)

                    for it in I:
                        embed.add_field(name=f':small_orange_diamond: **{iws[it + "1"].value}**', value=f'{iws[it + str(i+1)].value}', inline=False)
                        
                    break
                else:
                    if i == a:
                        await ctx.send(f'{name.id} don\'t have any property')
        else:
            await ctx.send('can\'t find any user')

        await ctx.send(embed=embed)
        iwb.save('item.xlsx')

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def give(self, ctx, name: discord.Member, amount: int, typee):
        count(ctx)
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            isfind = False
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(ctx.author.id):
                    for j in range(1, a + 1):
                        if str(iws['A' + str(j+1)].value) == str(name.id):
                            T = {'Gcoin' : 'B', 'Copper' : 'C', 'Silver' : 'D', 'Gold' : 'E', 'Diamond' : 'F', 'MG' : 'G'}
                            goods = T[typee]
                            if iws['A' + str(i+1)].value == str(name.id):
                                await ctx.send(f':x: Don\'t try to give property to yourself meow!')
                                isfind = True
                                break
                            if iws[goods + str(i+1)].value >= amount:
                                iws[goods + str(i+1)].value -= amount
                                iws[goods + str(j+1)].value += amount
                            else:
                                await ctx.send(f':x: **{ctx.author}** don\'t have enough **{typee}** meow!')
                            await ctx.send(f':handshake:  **{ctx.author}** gave **{name}** **{amount} {typee}** meow!!')
                            isfind = True
                            break
                        else:
                            if j == a:
                                isfind = True
                                await ctx.send(f':x: **{name}** didn\'t have an account meow!')
                else:
                    if i == a and not(isfind):
                        await ctx.send(':x: You don\'t have an account(enter .pick first meow!)')
        else:
            await ctx.send('can\'t find any user')

        iwb.save('item.xlsx')

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def picktimes(self, ctx):
        count(ctx)
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(ctx.author.id):
                    await ctx.send(f':raised_back_of_hand: **{ctx.author}** has picked {iws["I" + str(i+1)].value} times meow!')
                    break
                else:
                    if i == a:
                        await ctx.send('You don\'t have an account(enter .pick first meow!)')
        else:
            await ctx.send('can\'t find any user')

        iwb.save('item.xlsx')


    @commands.command()
    @commands.cooldown(1, 80000, commands.BucketType.user)
    async def daily(self, ctx):
        count(ctx)
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(ctx.author.id):
                    iws['B' + str(i+1)].value += 500
                    await ctx.send(f':moneybag: **{ctx.author}** earned the daily reward meow!')
                    break
                else:
                    if i == a:
                        await ctx.send('You don\'t have an account(enter .pick first meow!)')
        else:
            await ctx.send('can\'t find any user')

        iwb.save('item.xlsx')

    @commands.command()
    @commands.cooldown(1, 40000, commands.BucketType.user)
    async def rob(self, ctx, name: discord.Member):
        count(ctx)
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            isfind = False
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(ctx.author.id):
                    for j in range(1, a + 1):
                        if str(iws['A' + str(j+1)].value) == str(name.id):
                            if iws['H' + str(i+1)].value < 40:
                                iws['H' + str(i+1)].value += 1
                                await ctx.send(f'<a:hand:732937258868539483> **{ctx.author}**\'s Robbery skills point + 1 ({iws["H" + str(i+1)].value}/40)')
                            r = random.randint(1, 100)
                            if r <= iws['H' + str(i+1)].value:
                                P = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
                                p = random.choice(P)
                                iws['B' + str(i+1)].value += p
                                iws['B' + str(j+1)].value -= p
                                await ctx.send(f':money_with_wings: **{ctx.author}** robbed the property form **{name}** meow!!({p} Gcoin)')
                                
                            else:
                                iws['B' + str(i+1)].value -= 200
                                await ctx.send(f'<a:money:730029539815850045> **{ctx.author}** failed to rob the property form **{name}**\n:police_car: The MeowPolice took your property away meow~(200 Gcoin)')
                            isfind = True
                            break
                        else:
                            if j == a:
                                isfind = True
                                await ctx.send(f':x: **{name}** didn\'t have an account meow!')
                else:
                    if i == a and not(isfind):
                        await ctx.send(':x: You don\'t have an account(enter .pick first meow!)')
        else:
            await ctx.send('can\'t find any user')

        iwb.save('item.xlsx')

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def bag(self, ctx):
        count(ctx)
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(ctx.author.id):
                    I = ['B', 'C', 'D', 'E', 'F', 'G']
                    embed=discord.Embed(title=f'{ctx.author}\'s backpack',color=0xffe26f)

                    for it in I:
                        embed.add_field(name=f':small_orange_diamond: **{iws[it + "1"].value}**', value=f'{iws[it + str(i+1)].value}', inline=False)
                        
                    break
                else:
                    if i == a:
                        await ctx.send('You don\'t have any property')
        else:
            await ctx.send('can\'t find any user')

        await ctx.send(embed=embed)
        iwb.save('item.xlsx')

    @commands.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def pick(self, ctx):
        count(ctx)
        if iws['A1'].value != None:
            a = int(iws['A1'].value)
            for i in range(1, a + 1):
                if str(iws['A' + str(i+1)].value) == str(ctx.author.id):
                    it, num = mine()
                    iws[it + str(i+1)].value += num
                    await ctx.send(f'You pick up **{num}** **{iws[it + "1"].value}**!')
                    break
                else:
                    if i == a:
                        iws['A1'].value = int(iws['A1'].value) + 1
                        iws.append([-1, 0, 0, 0, 0, 0, 0, 0, 0])
                        iws['A' + str(i+2)].value = str(ctx.author.id)
                        it, num = mine()
                        iws[it + str(i+2)].value += num
                        await ctx.send(f'You pick up **{num}** **{iws[it + "1"].value}**!')
        else:
            iws['A1'].value = 1
            iws.append([-1, 0, 0, 0, 0, 0, 0, 0, 0])
            iws['A2'].value = str(ctx.author.id)
            it, name = mine()
            iws[it + '2'].value += num
            await ctx.send(f'You pick up **{num}** **{iws[it + "1"].value}**!')

        pickcount(ctx)
        iwb.save('item.xlsx')

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
                    if i == a:
                        await ctx.send('You don\'t have any property')
        else:
            await ctx.send('can\'t find any user')
        embed=discord.Embed(title="Sell", color=0xffe26f)

    @sell.command()
    async def Copper(self, ctx, amount = None):
        if amount != None:
            amount = int(amount)
        else:
            amount = iws['C' + str(k)].value
        iws['B' + str(k)].value += amount*2
        iws['C' + str(k)].value -= amount
        await ctx.send(f'**{amount} Copper** sold successfully meow!')
        iwb.save('item.xlsx')

    @sell.command()
    async def Silver(self, ctx, amount = None):
        if amount != None:
            amount = int(amount)
        else:
            amount = iws['D' + str(k)].value
        iws['B' + str(k)].value += amount*20
        iws['D' + str(k)].value -= amount
        await ctx.send(f'**{amount} Silver** sold successfully meow!')
        iwb.save('item.xlsx')

    @sell.command()
    async def Gold(self, ctx, amount = None):
        if amount != None:
            amount = int(amount)
        else:
            amount = iws['E' + str(k)].value
        iws['B' + str(k)].value += amount*200
        iws['E' + str(k)].value -= amount
        await ctx.send(f'**{amount} Gold** sold successfully meow!')
        iwb.save('item.xlsx')

    @sell.command()
    async def Diamond(self, ctx, amount = None):
        if amount != None:
            amount = int(amount)
        else:
            amount = iws['F' + str(k)].value
        iws['B' + str(k)].value += amount*2000
        iws['F' + str(k)].value -= amount
        await ctx.send(f'**{amount} Diamond** sold successfully meow!')
        iwb.save('item.xlsx')

    @sell.command()
    async def MG(self, ctx, amount = None):
        if amount != None:
            amount = int(amount)
        else:
            amount = iws['G' + str(k)].value
        iws['B' + str(k)].value += amount*20000
        iws['G' + str(k)].value -= amount
        await ctx.send(f'**{amount} Miracle Gem** sold successfully meow!')
        iwb.save('item.xlsx')


def setup(bot):
    bot.add_cog(Fun(bot))