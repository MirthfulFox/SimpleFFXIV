from asyncio.windows_events import NULL
import discord

def syntaxerror(description, title="❌ Wrong syntax!"):
    embed = discord.Embed(title=title, description=description, color=0xFF0000)
    #embed.set_author(name="MirthfulFox", url="https://github.com/MirthfulFox")
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