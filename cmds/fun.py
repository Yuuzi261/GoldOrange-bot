import discord
from discord.ext import commands
from openpyxl import load_workbook
from core.classes import Cog_Extension
import pygsheets
import datetime
import random
import json
import pymysql

pymysql . install_as_MySQLdb ()

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

def count(c):
    cwb = load_workbook('cmdcount.xlsx')
    cws = cwb.active
    if cws['A1'].value != None:
        a = int(cws['A1'].value)
        for i in range(a):
            if str(cws['B' + str(i+1)].value) == str(c.author.id):
                cws['C' + str(i+1)].value = int(cws['C' + str(i+1)].value) + 1
                break
            else:
                if i == (a-1):
                    cws['A1'].value = int(cws['A1'].value) + 1
                    cws['B' + str(i+2)].value = str(c.author.id)
                    cws['C' + str(i+2)].value = 1
    else:
        cws['A1'].value = 1
        cws['B1'].value = str(c.author.id)
        cws['C1'].value = 1

    cwb.save('cmdcount.xlsx')
    cwb.close()

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

gc = pygsheets.authorize(service_account_file=jdata["service_account_file"])
survey_url = jdata["item_gsheet"]
sh = gc.open_by_url(survey_url)
ws = sh.worksheet_by_title('sheet1')
ItDir = {'B' : 1, 'C' : 2, 'D' : 20, 'E' : 200, 'F' : 2000, 'G' : 20000}
Name_ItDir = {'B' : 'Gcoin', 'C' : 'Copper', 'D' : 'Silver', 'E' : 'Gold', 'F' : 'Diamond', 'G' : 'Miracle Gem'}
Index_ItDir = {'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6}
FieldL = ['ID', 'Gcoin', 'Copper', 'Silver', 'Gold', 'Diamond', 'MiracleGem', 'Robpoint', 'PickTimes', 'TNT', 'Dynamite', 'Knife', 'DesertEagle', 'Bullet', 'MP5', 'Magazine', 'Property']
k = -1

class Fun(Cog_Extension):
    global sh, ws, ItDir

    @commands.command()
    @commands.is_owner()
    async def sg(self, ctx, amount: int, typee, name: discord.Member = None):
        count(ctx)
        if name == None:
            if ws.get_value('A1') != '':
                a = int(ws.get_value('A1'))
                L = ws.get_col(1)[:a+1]
                i = 1
                await ctx.send(f':credit_card: Give EVERYONE **{amount} {ws.get_value(typee + "1")}** meow!!')
                for x in L[1:]:
                    i+=1
                    ws.update_value(typee + str(i), int(ws.get_value(typee + str(i))) + amount)
                    ws.update_value('Q' + str(i), int(ws.get_value('Q' + str(i))) + amount*ItDir[typee])
            else:
                await ctx.send(':x: can\'t find any user')

        else:
            if ws.get_value('A1') != None:
                a = int(ws.get_value('A1'))
                L = ws.get_col(1)[:a+1]
                i = 1
                for x in L[1:]:
                    i+=1
                    if str(ws.get_value('A' + str(i))) == str(name.id):
                        await ctx.send(f':credit_card: Give **{name} {amount} {ws.get_value(typee + "1")}** meow!!')
                        ws.update_value(typee + str(i), int(ws.get_value(typee + str(i))) + amount)
                        ws.update_value('Q' + str(i), int(ws.get_value('Q' + str(i))) + amount*ItDir[typee])
                        break
                    else:
                        if i == a+1:
                            await ctx.send(':x: Can\'t find the user meow')
            else:
                await ctx.send(':x: can\'t find any user')

    @commands.command()
    @commands.is_owner()
    async def sb(self, ctx, name: discord.Member):
        count(ctx)
        if ws.get_value('A1') != '':
            a = int(ws.get_value('A1'))
            L = ws.get_col(1)[:a+1]
            i = 1
            for x in L[1:]:
                i+=1
                if str(x) == str(name.id):
                    I = ['B', 'C', 'D', 'E', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
                    na = str(name)
                    embed=discord.Embed(title=f'{na[:-5]}\'s backpack',color=0xffe26f)

                    for it in I:
                        embed.add_field(name=f':small_orange_diamond: **{ws.get_value(it + "1")}**', value=f'{ws.get_value(it + str(i))}', inline=True)

                    break
                else:
                    if i == a+1:
                        await ctx.send(f':x: {name.id} don\'t have any property')
        else:
            await ctx.send(':x: can\'t find any user')

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def info(self, ctx, name: discord.Member = None):
        count(ctx)
        async with ctx.channel.typing():
            if ws.get_value('A1') != '':
                if name == None:
                    name = ctx.author
                a = int(ws.get_value('A1'))
                L = ws.get_col(1)[:a+1]
                i, j = 1, 1
                for x in L[1:]:
                    i+=1
                    if str(x) == str(name.id):
                        I = ['R', 'Q', 'H', 'I']
                        na = str(name)
                        embed=discord.Embed(title=f'{na[:-5]}\'s infomation',color=0xffe26f)

                        for it in I:
                            if it == 'Q':
                                embed.add_field(name=f':small_orange_diamond: **{ws.get_value(it + "1")}**', value=f'{ws.get_value(it + str(i))} <:Gcoin:736650744861556749>', inline=True)
                            elif it == 'R':
                                embed.add_field(name=f':small_orange_diamond: **{ws.get_value(it + "1")}**', value=f'#{ws.get_value(it + str(i))}', inline=True)
                            else:
                                embed.add_field(name=f':small_orange_diamond: **{ws.get_value(it + "1")}**', value=f'{ws.get_value(it + str(i))}', inline=True)

                        break
                    else:
                        if i == a+1:
                            await ctx.send(':x: You don\'t have an account(enter .pick first meow!)')
                            return
            else:
                await ctx.send(':x: can\'t find any user')
                return

            await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def buy(self, ctx, amount: int, obj):
        count(ctx)
        async with ctx.channel.typing():
            loc = 0
            if amount < 0:
                await ctx.send(':x: Don\'t try to enter a negative number meow~')
                return
            if ws.get_value('A1') != '':
                a = int(ws.get_value('A1'))
                L = ws.get_col(1)[:a+1]
                i = 1
                for x in L[1:]:
                    i+=1
                    if str(x) == str(ctx.author.id):
                        loc = i
                        if int(ws.get_value('B' + str(i))) < 0:
                            await ctx.send(f':x: You are in debt meow!')
                            return
                        break
                    else:
                        if i == a+1:
                            await ctx.send(':x: You don\'t have an account(enter .pick first meow!)')
            else:
                await ctx.send(':x: can\'t find any user')
            if obj == 'Copper':
                if int(ws.get_value('B' + str(loc))) - amount*3 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} Copper** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*3)
                    ws.update_value('C' + str(loc), int(ws.get_value('C' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'Silver':
                if int(ws.get_value('B' + str(loc))) - amount*30 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} Silver** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*30)
                    ws.update_value('D' + str(loc), int(ws.get_value('D' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount*10)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'Gold':
                if int(ws.get_value('B' + str(loc))) - amount*400 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} Gold** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*400)
                    ws.update_value('E' + str(loc), int(ws.get_value('E' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount*200)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'Diamond':
                if int(ws.get_value('B' + str(loc))) - amount*8000 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} Diamond** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*8000)
                    ws.update_value('F' + str(loc), int(ws.get_value('F' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount*6000)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'MG':
                if int(ws.get_value('B' + str(loc))) - amount*400000 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} Miracle Gem** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*400000)
                    ws.update_value('G' + str(loc), int(ws.get_value('G' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount*380000)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'TNT':
                if int(ws.get_value('B' + str(loc))) - amount*500 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} TNT** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*500)
                    ws.update_value('J' + str(loc), int(ws.get_value('J' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount*500)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif  obj == 'Dynamite':
                if int(ws.get_value('B' + str(loc))) - amount*1000 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} Dynamite** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*1000)
                    ws.update_value('K' + str(loc), int(ws.get_value('K' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount*1000)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'Knife':
                if int(ws.get_value('B' + str(loc))) - amount*5000 >= 0:
                    if int(ws.get_value('L' + str(loc))) == 0:
                        await ctx.send(f':white_check_mark: It\'s your **Knife** meow!Thank you for coming meow~')
                        ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - 5000)
                        ws.update_value('L' + str(loc), int(ws.get_value('L' + str(loc))) + 1)
                        ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - 5000)
                    else:
                        await ctx.send(f':x: You have owned a Knife meow!')
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'DE':
                if int(ws.get_value('B' + str(loc))) - amount*35000 >= 0:
                    if int(ws.get_value('M' + str(loc))) == 0:
                        await ctx.send(f':white_check_mark: It\'s your **Desert Eagle** meow!Thank you for coming meow~')
                        ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - 35000)
                        ws.update_value('M' + str(loc), int(ws.get_value('M' + str(loc))) + 1)
                        ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - 35000)
                    else:
                        await ctx.send(f':x: You have owned a Desert Eagle meow!')
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'MP5':
                if int(ws.get_value('B' + str(loc))) - amount*50000 >= 0:
                    if int(ws.get_value('N' + str(loc))) == 0:
                        await ctx.send(f':white_check_mark: It\'s your **MP5** meow!Thank you for coming meow~')
                        ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - 50000)
                        ws.update_value('N' + str(loc), int(ws.get_value('N' + str(loc))) + 1)
                        ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - 50000)
                    else:
                        await ctx.send(f':x: You have owned a MP5 meow!')
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'Bullet(DE)':
                if int(ws.get_value('B' + str(loc))) - amount*100 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} Bullet(DE)** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*100)
                    ws.update_value('O' + str(loc), int(ws.get_value('O' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount*100)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            elif obj == 'Magazine(MP5)':
                if int(ws.get_value('B' + str(loc))) - amount*200 >= 0:
                    await ctx.send(f':white_check_mark: It\'s your **{amount} Magazine(MP5)** meow!Thank you for coming meow~')
                    ws.update_value('B' + str(loc), int(ws.get_value('B' + str(loc))) - amount*200)
                    ws.update_value('P' + str(loc), int(ws.get_value('P' + str(loc))) + amount)
                    ws.update_value('Q' + str(loc), int(ws.get_value('Q' + str(loc))) - amount*200)
                else:
                    await ctx.send(f':x: You don\'t have enough money meow!')
            #Future Features
            # elif obj == 'PickCD':
            #     if iws['Q' + str(a)].value == 1800:
            #         await ctx.send(':x: The minimum for PickCD is 1800 sec meow!')
            #         return
            #     if iws['B' + str(a)].value - amount*20000 >= 0 and iws['Q' + str(a)].value - amount*100 >= 1800:
            #         iws['B' + str(a)].value -= amount*20000
            #         iws['Q' + str(a)].value -= amount*100
            #         await ctx.send(f':ballot_box_with_check: You cut down the **PickCD {amount} times ({amount*100}sec)** meow!Thank you for coming meow~')
            #     else:
            #         await ctx.send(f':x: You don\'t have enough money or over the purchase limit of PickCD meow!Try to type less amount meow!')
            # elif obj == 'RobCD':
            #     if iws['R' + str(a)].value == 10800:
            #         await ctx.send(':x: The minimum for RobCD is 10800 sec meow!')
            #         return
            #     if iws['B' + str(a)].value - amount*5000 >= 0 and iws['R' + str(a)].value - amount*100 >= 10800:
            #         iws['B' + str(a)].value -= amount*5000
            #         iws['R' + str(a)].value -= amount*100
            #         await ctx.send(f':ballot_box_with_check: You cut down the **RobCD {amount} times ({amount*100}sec)** meow!Thank you for coming meow~')
            #     else:
            #         await ctx.send(f':x: You don\'t have enough money or over the purchase limit of RobCD meow!Try to type less amount meow!')


    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def shop(self, ctx):
        embed=discord.Embed(title="桔喵Black Market", description="Product List", color=0xffe26f)
        embed.set_thumbnail(url="https://i.imgur.com/NOq5mPb.png")
        embed.add_field(name=":small_orange_diamond:Copper", value="<:Gcoin:736650744861556749> 3", inline=True)
        embed.add_field(name=":small_orange_diamond:Silver", value="<:Gcoin:736650744861556749> 30", inline=True)
        embed.add_field(name=":small_orange_diamond:Gold", value="<:Gcoin:736650744861556749> 400", inline=True)
        embed.add_field(name=":small_orange_diamond:Diamond", value="<:Gcoin:736650744861556749> 8000", inline=True)
        embed.add_field(name=":small_orange_diamond:Miracle Gem", value="<:Gcoin:736650744861556749> 400000", inline=True)
        embed.add_field(name=":small_orange_diamond:TNT", value="<:Gcoin:736650744861556749> 500", inline=True)
        embed.add_field(name=":small_orange_diamond:Dynamite", value="<:Gcoin:736650744861556749> 1000", inline=True)
        embed.add_field(name=":small_orange_diamond:Knife", value="<:Gcoin:736650744861556749> 5000", inline=True)
        embed.add_field(name=":small_orange_diamond:Desert Eagle", value="<:Gcoin:736650744861556749> 35000", inline=True)
        embed.add_field(name=":small_orange_diamond:MP5", value="<:Gcoin:736650744861556749> 50000", inline=True)
        embed.add_field(name=":small_orange_diamond:Bullet(DE)", value="<:Gcoin:736650744861556749> 100", inline=True)
        embed.add_field(name=":small_orange_diamond:Magazine(MP5)", value="<:Gcoin:736650744861556749> 200", inline=True)
        # embed.add_field(name=":small_orange_diamond:PickCD", value="<:Gcoin:736650744861556749> 20000", inline=True)
        # embed.add_field(name=":small_orange_diamond:RobCD", value="<:Gcoin:736650744861556749> 5000", inline=True)
        # embed.add_field(name=":small_orange_diamond:Comming S∞n", value="<:Gcoin:736650744861556749> ??", inline=True)
        embed.set_footer(text="Thank you for coming meow~")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 600, commands.BucketType.user)
    async def give(self, ctx, name: discord.Member, amount: int, typee):
        count(ctx)
        async with ctx.channel.typing():
            if amount < 0:
                await ctx.send(':x: DON\'t try to rob by by typing “.give” command meow!')
                return
            if ws.get_value('A1') != '':
                a = int(ws.get_value('A1'))
                L = ws.get_col(1)[:a+1]
                i, j = 1, 1
                isfind = False
                for x in L[1:]:
                    i+=1
                    if str(x) == str(ctx.author.id):
                        for y in L[1:]:
                            j+=1
                            if str(y) == str(name.id):
                                T = {'Gcoin' : 'B', 'Copper' : 'C', 'Silver' : 'D', 'Gold' : 'E', 'Diamond' : 'F', 'MG' : 'G'}
                                if typee in T:
                                    goods = T[typee]
                                else:
                                    await ctx.send(':x: You can\'t send out this kind of item meow!')
                                    return
                                if ws.get_value('A' + str(i)) == str(name.id):
                                    await ctx.send(f':x: Don\'t try to give property to yourself meow!')
                                    isfind = True
                                    break
                                if int(ws.get_value(goods + str(i))) >= amount:
                                    await ctx.send(f':handshake:  **{ctx.author}** gave **{name}** **{amount} {typee}** meow!!')
                                    ws.update_value(goods + str(i), int(ws.get_value(goods + str(i))) - amount)
                                    ws.update_value(goods + str(j), int(ws.get_value(goods + str(j))) + amount)
                                    ws.update_value('Q' + str(i), int(ws.get_value('Q' + str(i))) - amount*ItDir[goods])
                                    ws.update_value('Q' + str(j), int(ws.get_value('Q' + str(j))) + amount*ItDir[goods])
                                else:
                                    await ctx.send(f':x: **{ctx.author}** don\'t have enough **{typee}** meow!')
                                    return
                                isfind = True
                                break
                            else:
                                if j == a+1:
                                    isfind = True
                                    await ctx.send(f':x: **{name}** didn\'t have an account meow!')
                    else:
                        if i == (a+1) and not(isfind):
                            await ctx.send(':x: You don\'t have an account(enter .pick first meow!)')
            else:
                await ctx.send(':x: can\'t find any user')

    @commands.command()
    @commands.cooldown(1, 80000, commands.BucketType.user)
    async def daily(self, ctx):
        count(ctx)
        if ws.get_value('A1') != '':
            a = int(ws.get_value('A1'))
            L = ws.get_col(1)[:a+1]
            i = 1
            for x in L[1:]:
                i+=1
                if str(x) == str(ctx.author.id):
                    na = str(ctx.author)
                    await ctx.send(f':moneybag: **{na[:-5]}** earned the daily reward meow!')
                    ws.update_value('B' + str(i), int(ws.get_value('B' + str(i))) + 500)
                    ws.update_value('Q' + str(i), int(ws.get_value('Q' + str(i))) + 500)
                    break
                else:
                    if i == a+1:
                        await ctx.send(':x: You don\'t have an account(enter .pick first meow!)')
        else:
            await ctx.send(':x: can\'t find any user')

    @commands.command()
    @commands.cooldown(2, 10800, commands.BucketType.user)
    async def rob(self, ctx, name: discord.Member):
        # count(ctx)
        victim = 0
        conn = pymysql.connect(host = jdata["DB_host"], user = jdata["DB_user"], passwd = jdata["DB_password"], db = jdata["DB_name"])
        cursor = conn.cursor()
        if cursor.execute(f"SELECT * FROM item WHERE ID LIKE {ctx.author.id}"):
            for r in cursor:
                userL = list(r)
            if cursor.execute(f"SELECT * FROM item WHERE ID LIKE {name.id}"):
                victim = 1
                for r in cursor:
                    victimL = list(r)
                isProps = 0
                if userL[7] < 20:
                    userL[7] += 0.5
                    await ctx.send(f'<a:hand:732937258868539483> **{ctx.author}**\'s Robbery skills point + 0.5 ({userL[7]}/20)')
                r = random.randint(1, 100)
                if r <= userL[7]:
                    P = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
                    p = random.choice(P)
                    if userL[14] == 1 and userL[15] > 0:
                        p = victimL[1]
                        isProps = 1
                    elif userL[12] == 1 and userL[13] > 0:
                        p = victimL[1]//2
                        isProps = 2
                    elif userL[11] == 1:
                        p*=2
                        isProps = 3

                    if isProps == 0:
                        await ctx.send(f':money_with_wings: **{ctx.author}** robbed the property form **{name}** meow!!({p} <:Gcoin:736650744861556749>)')
                    elif isProps == 1:
                        await ctx.send(f':money_with_wings: **{ctx.author}** robbed the property form **{name}** meow!!({p} <:Gcoin:736650744861556749>)\n<a:frog_gun:732828139499159625> Because **{ctx.author}** use **MP5** so all the **{name}**\'s Gcoin was taken away meow!')
                    elif isProps == 2:
                        await ctx.send(f':money_with_wings: **{ctx.author}** robbed the property form **{name}** meow!!({p} <:Gcoin:736650744861556749>)\n<a:frog_gun:732828139499159625> Because **{ctx.author}** use **Desert Eagle** so half the **{name}**\'s Gcoin was taken away meow!')
                    else:
                        await ctx.send(f':money_with_wings: **{ctx.author}** robbed the property form **{name}** meow!!({p} <:Gcoin:736650744861556749>)\n<a:frog_gun:732828139499159625> Because **{ctx.author}** use **Knife** so **{ctx.author}** robbed 2x <:Gcoin:736650744861556749> meow!')

                    userL[1] += p
                    victimL[1] -= p
                    userL[16] += p
                    victimL[16] -= p

                else:
                    await ctx.send(f'<a:money:730029539815850045> **{ctx.author}** failed to rob the property form **{name}**\n:police_car: The MeowPolice took your property away meow~(200 <:Gcoin:736650744861556749>)')
                    userL[1] -= 200
                    userL[16] -= 200

                if userL[14] == 1 and userL[15] > 0:
                    userL[15] -= 1
                elif userL[12] == 1 and userL[13] > 0:
                    userL[13] -= 1
            else:
                await ctx.send(f':x: Can\'t find this account:{name}.')
        else:
            await ctx.send(':x: You don\'t have an account, please type ".pick" first.')

        if victim == 1:
            cursor.execute(f"UPDATE item SET {FieldL[1]} = {userL[1]}, {FieldL[7]} = {userL[7]}, {FieldL[13]} = {userL[13]}, {FieldL[15]} = {userL[15]}, {FieldL[16]} = {userL[16]} WHERE ID = {ctx.author.id}")
            cursor.execute(f"UPDATE item SET {FieldL[1]} = {victimL[1]}, {FieldL[16]} = {victimL[16]} WHERE ID = {name.id}")
            
        conn.commit()
        conn.close

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def ibag(self, ctx):
        # count(ctx)
        conn = pymysql.connect(host = jdata["DB_host"], user = jdata["DB_user"], passwd = jdata["DB_password"], db = jdata["DB_name"])
        cursor = conn.cursor()
        if cursor.execute(f"SELECT * FROM item WHERE ID LIKE {ctx.author.id}"):
            for r in cursor:
                userL = list(r)
            na = str(ctx.author)
            embed=discord.Embed(title=f'{na[:-5]}\'s items',color=0xffe26f)
            for i in range(9,16):
                embed.add_field(name=f':small_orange_diamond: **{FieldL[i]}**', value=f'{userL[i]}', inline=False)
        else:
            await ctx.send(':x: You don\'t have an account, please type ".pick" first.')

        await ctx.send(embed=embed)
        conn.close

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def bag(self, ctx):
        # count(ctx)
        conn = pymysql.connect(host = jdata["DB_host"], user = jdata["DB_user"], passwd = jdata["DB_password"], db = jdata["DB_name"])
        cursor = conn.cursor()
        if cursor.execute(f"SELECT * FROM item WHERE ID LIKE {ctx.author.id}"):
            for r in cursor:
                userL = list(r)
            na = str(ctx.author)
            embed=discord.Embed(title=f'{na[:-5]}\'s backpack',color=0xffe26f)
            for i in range(1,7):
                embed.add_field(name=f':small_orange_diamond: **{FieldL[i]}**', value=f'{userL[i]}', inline=False)
        else:
            await ctx.send(':x: You don\'t have an account, please type ".pick" first.')

        await ctx.send(embed=embed)
        conn.close

    @commands.command()
    @commands.cooldown(2, 1800, commands.BucketType.user)
    async def pick(self, ctx):
        # count(ctx)
        conn = pymysql.connect(host = jdata["DB_host"], user = jdata["DB_user"], passwd = jdata["DB_password"], db = jdata["DB_name"])
        cursor = conn.cursor()
        if cursor.execute(f"SELECT * FROM item WHERE ID LIKE {ctx.author.id}"):
            #found the user
            for r in cursor:
                userL = list(r)
            it, num = mine()
            if userL[10] > 0:
                userL[10] -= 1
                num*=4
                await ctx.send(f':boom: You blasted a HUGE hole and you found **{num}** **{Name_ItDir[it]}**!(x4 income)')
            elif userL[9] > 0:
                userL[9] -= 1
                num*=2
                await ctx.send(f':boom: You blasted a BIG hole and you found **{num}** **{Name_ItDir[it]}**!(x2 income)')
            else:
                await ctx.send(f':pick: You pick up **{num}** **{Name_ItDir[it]}**!')
            userL[Index_ItDir[it]] += num
            userL[16] += num*ItDir[it]
            cursor.execute(f"UPDATE item SET {FieldL[9]} = {userL[9]}, {FieldL[10]} = {userL[10]}, {FieldL[16]} = {userL[16]}, {FieldL[Index_ItDir[it]]} = {userL[Index_ItDir[it]]} WHERE ID = {ctx.author.id}")
        else:
            #can't find the user, creat a new account
            cursor.execute(f"INSERT INTO item({FieldL[0]}, {FieldL[1]}, {FieldL[2]}, {FieldL[3]}, {FieldL[4]}, {FieldL[5]}, {FieldL[6]}, {FieldL[7]}, {FieldL[8]}, {FieldL[9]}, {FieldL[10]}, {FieldL[11]}, {FieldL[12]}, {FieldL[13]}, {FieldL[14]}, {FieldL[15]}, {FieldL[16]})VALUES(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)")
            userL = [0] * 18
            userL[0] = ctx.author.id
            it, num = mine()
            userL[Index_ItDir[it]] += num
            userL[16] += num*ItDir[it]
            await ctx.send(f':pick: You pick up **{num}** **{Name_ItDir[it]}**!')
            cursor.execute(f"UPDATE item SET {FieldL[0]} = {userL[0]}, {FieldL[16]} = {userL[16]}, {FieldL[Index_ItDir[it]]} = {userL[Index_ItDir[it]]} WHERE ID = 0")
        cursor.execute(f"UPDATE item SET {FieldL[8]} = {userL[8] + 1} WHERE ID = {ctx.author.id}")
        conn.commit()
        conn.close

    @commands.group()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sell(self, ctx, amount: int, obj):
        # count(ctx)
        obj = obj.lower()
        conn = pymysql.connect(host = jdata["DB_host"], user = jdata["DB_user"], passwd = jdata["DB_password"], db = jdata["DB_name"])
        cursor = conn.cursor()
        if cursor.execute(f"SELECT * FROM item WHERE ID LIKE {ctx.author.id}"):
            pass
        else:
            await ctx.send(':x: You don\'t have an account, please type ".pick" first.')

        for r in cursor:
            userL = list(r)

        if obj == 'copper':
            if amount > userL[2] or amount <= 0:
                await ctx.send(f':x: You DON\'T HAVE so many treasures meow!!')
            else:
                userL[1] += amount*2
                userL[2] -= amount
                cursor.execute(f"UPDATE item SET {FieldL[1]} = {userL[1]}, {FieldL[2]} = {userL[2]} WHERE ID = {ctx.author.id}")
                await ctx.send(f'**:white_check_mark: {amount} Copper** sold successfully meow!')
        elif obj == 'silver':
            if amount > userL[3] or amount <= 0:
                await ctx.send(f':x: You DON\'T HAVE so many treasures meow!!')
            else:
                userL[1] += amount*20
                userL[3] -= amount
                cursor.execute(f"UPDATE item SET {FieldL[1]} = {userL[1]}, {FieldL[3]} = {userL[3]} WHERE ID = {ctx.author.id}")
                await ctx.send(f'**:white_check_mark: {amount} Silver** sold successfully meow!')
        elif obj == 'gold':
            if amount > userL[4] or amount <= 0:
                await ctx.send(f':x: You DON\'T HAVE so many treasures meow!!')
            else:
                userL[1] += amount*200
                userL[4] -= amount
                cursor.execute(f"UPDATE item SET {FieldL[1]} = {userL[1]}, {FieldL[4]} = {userL[4]} WHERE ID = {ctx.author.id}")
                await ctx.send(f'**:white_check_mark: {amount} Gold** sold successfully meow!')
        elif obj == 'diamond':
            if amount > userL[5] or amount <= 0:
                await ctx.send(f':x: You DON\'T HAVE so many treasures meow!!')
            else:
                userL[1] += amount*2000
                userL[5] -= amount
                cursor.execute(f"UPDATE item SET {FieldL[1]} = {userL[1]}, {FieldL[5]} = {userL[5]} WHERE ID = {ctx.author.id}")
                await ctx.send(f'**:white_check_mark: {amount} Diamond** sold successfully meow!')
        elif obj == 'mg':
            if amount > userL[6] or amount <= 0:
                await ctx.send(f':x: You DON\'T HAVE so many treasures meow!!')
            else:
                userL[1] += amount*20000
                userL[6] -= amount
                cursor.execute(f"UPDATE item SET {FieldL[1]} = {userL[1]}, {FieldL[6]} = {userL[6]} WHERE ID = {ctx.author.id}")
                await ctx.send(f'**:white_check_mark: {amount} Miracle Gem** sold successfully meow!')
        
        conn.commit()
        conn.close


def setup(bot):
    bot.add_cog(Fun(bot))