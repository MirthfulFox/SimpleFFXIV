from discord.ext import commands
from discord.ext.commands import bot
from simpleffxiv.utils.messages import syntaxerror, partyembed
from os import getenv

class XIVUtils(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="createparty", aliases=["cp", "party"])
    async def help(self, ctx: commands.Context, *args):
        if (len(args)<1 or len(args)>2):
            await ctx.send(embed=syntaxerror(opt=True, description=f'{getenv("prefix")}createparty `\"max players\"` `[\"description\"]`'))
            return
        try: maxplayers = int(args[0])
        except:
            await ctx.send(embed=syntaxerror(description=f'First argument have to be a number.\n**F.ex:** {getenv("prefix")}createparty 4  \"leveling roulette\"'))
            return
        if (len(args)==1): embed=partyembed(ctx)
        else: embed=partyembed(ctx, desc=args[1])
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("🛡")
        await msg.add_reaction("💊")
        await msg.add_reaction("⚔")
        await msg.add_reaction("❌")
        #https://stackoverflow.com/questions/61934630/detect-reactions-only-on-specific-messages-sent-by-the-bot-in-discord-py

def setup(bot: commands.Bot):
    bot.add_cog(XIVUtils(bot))