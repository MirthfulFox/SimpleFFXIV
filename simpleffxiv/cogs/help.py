from discord.ext import commands
from simpleffxiv.utils.messages import helpmessage

class Help(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="help", aliases=["h"])
    async def help(self, ctx: commands.Context):
        await ctx.send(embed=helpmessage())

def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))