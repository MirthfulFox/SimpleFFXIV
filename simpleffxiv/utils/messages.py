from asyncio.windows_events import NULL
import discord
from os import getenv

def syntaxerror(description, title="❌ Wrong syntax!", opt=False):
    embed = discord.Embed(title=title, description=description, color=0xFF0000)
    if opt==True:
        embed.set_footer(text="Parameters inside [ ] are optional.")
    return embed

def notfound(titlename):
    embed = discord.Embed(title="💔 " + titlename + " not found", color=0xFF0000)
    return embed

def nolistings():
    embed = discord.Embed(title="🕳 There are no listings for this item", color=0xFF0000)
    return embed

def itempricesWorld(item, world, prices, quantity, hq):
    item = item.capitalize()
    world = world.capitalize()
    embed = discord.Embed(title="💰 " + item, color=0x4D96F4, description="In " + world)
    for i in range(0,len(hq)):
        if (hq[i] == True):
            hq[i] = "💎"
        else:
            hq[i] = "🪨"
    values = ""
    hqvalues = ""
    for i in range(0, len(prices)):
        quantity[i] = str(quantity[i])
        prices[i] = str(prices[i])
        values = ''.join([values, "%sg x %s\n" % (prices[i], quantity[i])])
        hqvalues = ''.join([hqvalues, "*%s*\n" % (hq[i])])
    embed.add_field(name="HQ", value=hqvalues, inline=True)
    embed.add_field(name="Lowest prices", value=values, inline=True)
    return embed

def itempricesDC(item, world, prices, quantity, hq, worldname):
    item = item.capitalize()
    world = world.capitalize()
    embed = discord.Embed(title="💰 " + item, color=0x4D96F4, description="In " + world)
    for i in range(0,len(hq)):
        if (hq[i] == True):
            hq[i] = "💎"
        else:
            hq[i] = "🪨"
    values = ""
    worlds = ""
    hqvalues = ""
    for i in range(0, len(prices)):
        quantity[i] = str(quantity[i])
        prices[i] = str(prices[i])
        values = ''.join([values, "%sg x %s\n" % (prices[i], quantity[i])])
        worlds = ''.join([worlds, "*%s*\n" % (worldname[i])])
        hqvalues = ''.join([hqvalues, "*%s*\n" % (hq[i])])
    embed.add_field(name="HQ", value=hqvalues, inline=True)
    embed.add_field(name="Lowest prices", value=values, inline=True)
    embed.add_field(name="World", value=worlds, inline=True)
    return embed

def unexpectederror():
    embed = discord.Embed(title="⚠️ Unexpected error.", description="Try again later", color=0xFF0000)
    return embed

def helpmessage():
    embed = discord.Embed(title="❓ Help", color=0x4D96F4)

    commands_name = f'`{getenv("prefix")}itemsearch | item | is`\n'
    commands_name += f'`{getenv("prefix")}playersearch | player | ps`\n'
    commands_name += f'`{getenv("prefix")}itemprice | price | ip`\n'
    commands_name += f'`{getenv("prefix")}createparty | party | cp`'

    commands_syntax = f'`item name`\n`forename` `surname` `world`\n`\"item name\"` `world OR datacenter` `[hq|nq]`\n`\"max players\"` `[\"description\"]`'

    embed.add_field(name="Command", value=commands_name, inline=True)
    embed.add_field(name="Syntax", value=commands_syntax, inline=True)

    embed.set_footer(text="Parameters inside [ ] are optional.")
    return embed