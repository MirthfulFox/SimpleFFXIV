from discord.ext import commands
import requests

class ItemSearch(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(name="itemsearch")
    async def itemsearch(self, ctx: commands.Context, *args):
        
        #The code below concatenates the args and gets the first character of each word uppercase.
        search = ""
        for i in args:
            search = search + "_" + i.capitalize()
        search = search[1:]
        fullURL = "https://ffxiv.gamerescape.com/wiki/" + search

        response = requests.get(fullURL)
        if response.status_code == 200:
            await ctx.send(fullURL)
        else:
            await ctx.send("The item hasn't been found")

def setup(bot: commands.Bot):
    bot.add_cog(ItemSearch(bot))