from os import getenv
import discord
from discord.ext import commands
from discord.utils import get
from dotenv.main import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix=getenv("prefix"))

bot.remove_command('help')

bot.load_extension("simpleffxiv.cogs.xivsearch")
bot.load_extension("simpleffxiv.cogs.help")
bot.load_extension("simpleffxiv.cogs.xivutils")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(getenv("BOT_STATUS")))


bot.run(getenv("TOKEN"))