import asyncio
from discord.ext import commands
from simpleffxiv.utils.managereactions import partyembed
from simpleffxiv.utils.messages import syntaxerror
from os import getenv
import discord



class XIVUtils(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="createparty", aliases=["cp", "party"])
    async def createparty(self, ctx: commands.Context, *args):
        if (len(args)<1 or len(args)>2):
            await ctx.send(embed=syntaxerror(opt=True, description=f'{getenv("prefix")}createparty `\"max players\"` `[\"description\"]`'))
            return
        try: maxplayers = int(args[0])
        except:
            await ctx.send(embed=syntaxerror(description=f'First argument have to be a number.\n**F.ex:** {getenv("prefix")}createparty 4  \"leveling roulette\"'))
            return
        if (len(args)==1): embed=partyembed(ctx, maxplayers)
        else: embed=partyembed(ctx, maxplayers, desc=args[1])
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("🛡")
        await msg.add_reaction("💊")
        await msg.add_reaction("⚔")
        await msg.add_reaction("❌")


def setup(bot: commands.Bot):
    bot.add_cog(XIVUtils(bot))
    