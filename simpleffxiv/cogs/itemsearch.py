from discord.ext import commands
import requests
from simpleffxiv.utils.messages import notfound, syntaxerror, unexpectederror
from os import getenv

class ItemSearch(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="itemsearch")
    async def itemsearch(self, ctx: commands.Context, *args):
        if (len(args)==0):
            await ctx.send(embed=syntaxerror(title="Syntax is:", description=getenv("prefix") + "itemsearch `item`"))
            return
        search = ""
        for i in args:
            search = search + "_" + i.capitalize()
        search = search[1:]
        fullURL = "https://ffxiv.gamerescape.com/wiki/" + search

        response = requests.get(fullURL)
        if response.status_code == 200:
            await ctx.send(fullURL)
        else:
            await ctx.send(embed=notfound("Item"))


def setup(bot: commands.Bot):
    bot.add_cog(ItemSearch(bot))