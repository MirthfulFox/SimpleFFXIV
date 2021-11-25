from os import getenv
import discord
from discord.ext import commands
from dotenv.main import load_dotenv
from simpleffxiv.utils.managereactions import deleteplayer, addplayer

load_dotenv()
bot = commands.Bot(command_prefix=getenv("prefix"))

bot.remove_command('help')

bot.load_extension("simpleffxiv.cogs.xivsearch")
bot.load_extension("simpleffxiv.cogs.help")
bot.load_extension("simpleffxiv.cogs.xivutils")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(getenv("BOT_STATUS")))

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot: return
    await reaction.remove(user)
    if (reaction.emoji == "🛡") or (reaction.emoji == "💊") or (reaction.emoji == "⚔"):
        #if(catchplayers(user, reaction)):
            await addplayer(user, reaction, ctx=await bot.get_context(reaction.message))
    if reaction.emoji == "❌": await deleteplayer(user, reaction, ctx=await bot.get_context(reaction.message))


bot.run(getenv("TOKEN"))