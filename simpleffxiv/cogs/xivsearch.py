from os import getenv
from discord import message
from discord.ext import commands
import pyxivapi
from simpleffxiv.utils.messages import badsyntax

class XIVSearch(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="playersearch")
    async def playersearch(self, ctx: commands.Context, *args):
        if (len(args)!=3):
            await ctx.send(embed=badsyntax(description=getenv("prefix") + "playersearch `forename` `surname` `world`"))
            #await ctx.send("Syntax is: "+ getenv("prefix") +"playersearch forename surname world")
        else:
            client = pyxivapi.XIVAPIClient(api_key=getenv("XIVAPIKey"))
            character = await client.character_search(world=args[2], forename=args[0], surname=args[1])

            if(character['Pagination']['Results'] == 1):
                charID=(character['Results'][0]['ID'])
                await ctx.send("https://eu.finalfantasyxiv.com/lodestone/character/"+str(charID))
            else:
                await ctx.send("Character not found")

            await client.session.close()
        

def setup(bot: commands.Bot):
    bot.add_cog(XIVSearch(bot))