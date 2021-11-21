import discord
import simpleffxiv

def myembed(c=0xDB7752):
    embed = discord.Embed(colour=c)
    embed.set_footer(text=simpleffxiv.copyright())
    return embed