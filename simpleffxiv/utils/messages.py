import discord

def badsyntax(description, title="❌ Bad syntax!"):
    embed = discord.Embed(title=title, description=description, color=0xFF0000)
    #embed.set_author(name="MirthfulFox", url="https://github.com/MirthfulFox")
    return embed