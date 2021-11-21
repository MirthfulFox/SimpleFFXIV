from os import getenv
import discord
from discord.ext import commands
from dotenv.main import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix="?")

bot.load_extension("simpleffxiv.cogs.itemsearch")
bot.load_extension("simpleffxiv.cogs.xivsearch")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(getenv("BOT_STATUS")))  # Update Bot status

bot.run(getenv("TOKEN"))