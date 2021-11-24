from os import getenv
from discord.ext import commands
import pyxivapi
from simpleffxiv.utils.messages import syntaxerror, nolistings,notfound, itempricesWorld, itempricesDC, nolistings, unexpectederror
from simpleffxiv.utils.itemid import getitemid
import requests
import json
import time

class XIVSearch(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="playersearch", aliases=["ps", "player"])
    async def playersearch(self, ctx: commands.Context, *args):
        if (len(args)!=3):
            await ctx.send(embed=syntaxerror(description=getenv("prefix") + "playersearch `forename` `surname` `world`"))
            return
        client = pyxivapi.XIVAPIClient(api_key=getenv("XIVAPIKey"))
        character = await client.character_search(world=args[2], forename=args[0], surname=args[1])
        try:
            if(character is not None):
                if(character['Pagination']['Results'] > 0):
                    charID=(character['Results'][0]['ID'])
                    async with ctx.typing():
                        response = requests.get("https://ffxiv-character-cards.herokuapp.com/characters/id/%s.png" % charID)
                        for i in range (0,10):
                            if response.ok:
                                await ctx.send(response.url)
                                await ctx.send("<https://eu.finalfantasyxiv.com/lodestone/character/%s>" % str(charID))
                                break
                            response = requests.get("https://ffxiv-character-cards.herokuapp.com/characters/id/%s.png" % charID)
                            time.sleep(1)
                    if not response.ok:
                        await ctx.send("<https://eu.finalfantasyxiv.com/lodestone/character/%s>" % str(charID))
                else:
                    await ctx.send(embed=notfound("Character"))
                await client.session.close()
            else:
                await self.playersearch(ctx = ctx, args = args)
        except:
            await ctx.send(embed=unexpectederror())
            await client.session.close()
    

    @commands.command(name="itemprice", aliases=["ip", "price"])
    async def itemprice(self, ctx: commands.Context, *args):
        if (len(args)<2 or len(args)>3):
            await ctx.send(embed=syntaxerror(opt=True, description=getenv("prefix") + "itemprice `\"item name\"` `world OR datacenter` `[hq|nq]`"))
            return
        client = pyxivapi.XIVAPIClient(api_key=getenv("XIVAPIKey"))
        item = await getitemid(name=args[0], client=client)
        if(item['Pagination']['Results'] == 1):
            itemID=(item['Results'][0]['ID'])
            URL = "https://universalis.app/api/" + args[1] + "/" + str(itemID) + "?listings=10"
            if (len(args)==3):
                if (args[2] == "hq"):
                    URL += "&hq=true"
            response = requests.get(URL)
            if response.status_code == 200:
                rt = json.loads(response.text)
                if (len(rt['listings'])==0):
                    await ctx.send(embed=nolistings())
                    await client.session.close()
                    return
                rt = rt['listings']
                priceperunit = []
                quantity = []
                hq = []
                for i in rt:
                    priceperunit.append(i["pricePerUnit"])
                    quantity.append(i["quantity"])
                    hq.append(i["hq"])     
                if (rt[0].get('worldName', True) == True):
                    await ctx.send(embed = itempricesWorld(args[0], args[1], priceperunit, quantity, hq))
                else:
                    worldname = []
                    for i in rt:
                        worldname.append(i["worldName"])
                    await ctx.send(embed = itempricesDC(args[0], args[1], priceperunit, quantity, hq, worldname))
            else:
                await ctx.send(embed=notfound("Item"))
        else:
            await ctx.send(embed=notfound("Item"))
        await client.session.close()


    @commands.command(name="itemsearch", aliases=["is", "item"])
    async def itemsearch(self, ctx: commands.Context, *args):
        if (len(args)==0):
            await ctx.send(embed=syntaxerror(description=getenv("prefix") + "itemsearch `item`"))
            return
        search = ""
        for i in args:
            search = search + "_" + i.capitalize()
        search = search[1:]
        fullURL = "https://ffxiv.gamerescape.com/wiki/" + search
        async with ctx.typing():
            response = requests.get(fullURL)
        if response.status_code == 200:
            await ctx.send(f'<{fullURL}>')
        else:
            await ctx.send(embed=notfound("Item"))

def setup(bot: commands.Bot):
    bot.add_cog(XIVSearch(bot))