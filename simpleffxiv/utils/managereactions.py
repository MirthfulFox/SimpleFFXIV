import discord

def partyembed(ctx, maxpl, desc = "none"):
    if desc == ("none"):
        embed = discord.Embed(title=f"{ctx.author.name}'s party", color=0x2f233c)
    else:
        embed = discord.Embed(title=f"{ctx.author.name}'s party", color=0x2f233c, description=desc)
    embed.add_field(name="Tank", value="-", inline=True)
    embed.add_field(name="Healer", value="-", inline=True)
    embed.add_field(name="DPS", value="-", inline=True)
    embed.set_footer(text=f'Players: [0/{maxpl}]')
    return embed

def addplayertoparty(previousembed, emoji, player):
    embed = previousembed
    dict = previousembed.to_dict()

    for i in dict['fields']:
        if i['value'].find(player) != -1: return embed

    currentplayers = int(dict['footer']['text'][dict['footer']['text'].find('[')+1:dict['footer']['text'].find('/')])
    maxplayers = int(dict['footer']['text'][dict['footer']['text'].find('/')+1:dict['footer']['text'].find(']')])
    if currentplayers < maxplayers:
        if emoji=="🛡":
            playersaux = dict['fields'][0]['value']
            embed.remove_field(0)
            if playersaux == "-":
                embed.insert_field_at(0, name="Tank", value=player, inline=True)
            else:            
                embed.insert_field_at(0, name="Tank", value=f'{playersaux}\n{player}', inline=True)
        if emoji=="💊":
            playersaux = dict['fields'][1]['value']
            embed.remove_field(1)
            if playersaux == "-":
                embed.insert_field_at(1, name="Healer", value=player, inline=True)
            else:            
                embed.insert_field_at(1, name="Healer", value=f'{playersaux}\n{player}', inline=True)
        if emoji=="⚔":
            playersaux = dict['fields'][2]['value']
            embed.remove_field(2)
            if playersaux == "-":
                embed.insert_field_at(2, name="DPS", value=player, inline=True)
            else:            
                embed.insert_field_at(2, name="DPS", value=f'{playersaux}\n{player}', inline=True)
        currentplayers+=1
        embed.set_footer(text=f'Players: [{currentplayers}/{maxplayers}]')
    return embed

def removeplayerfromparty(previousembed, player):
    embed = previousembed
    dict = previousembed.to_dict()
    currentplayers = int(dict['footer']['text'][dict['footer']['text'].find('[')+1:dict['footer']['text'].find('/')])
    maxplayers = int(dict['footer']['text'][dict['footer']['text'].find('/')+1:dict['footer']['text'].find(']')])
    for i in dict['fields']:
        i['value'] = i['value'].replace(player, '')
        if i['value'] == '': i['value'] = '-'
    embed = discord.Embed.from_dict(dict)
    if currentplayers > 0:
        currentplayers-=1
        embed.set_footer(text=f'Players: [{currentplayers}/{maxplayers}]')
    return embed

async def deleteplayer(user, reaction, ctx) -> None:
    await reaction.message.edit(embed=removeplayerfromparty(reaction.message.embeds[0], user.mention))

async def addplayer(user, reaction, ctx) -> None:
    await reaction.message.edit(embed=addplayertoparty(reaction.message.embeds[0], reaction.emoji, user.mention))