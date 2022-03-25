import os

import nextcord
from nextcord.ext import commands

TOKEN = 'OTUxNTYyNTg2MDYxNjg4OTQy.YipRtw.MpyW2wU6xysWfBgdZNj7NCnFgwU'

client = commands.Bot(intents=nextcord.Intents.all(), command_prefix='!')
client.remove_command('help')


@client.event
async def on_ready():
    print('Eingelogged als ' + client.user.name)


@client.command()
async def ping(ctx):
    embed = nextcord.Embed(
        title='Pong!',
        color=0x5865f2
    )
    embed.add_field(name='Latenz:', value=f'```{round(client.latency * 1000)} ms```')
    await ctx.send(embed=embed)


@client.command()
async def light1on(ctx):
    embed = nextcord.Embed(
        title='Licht an!',
        colour=0x3ba55c
    )
    await ctx.send(embed=embed)
    os.system('python3 on.py')


@client.command()
async def light1off(ctx):
    embed = nextcord.Embed(
        title='Licht aus!',
        colour=0xd15d4b
    )
    await ctx.send(embed=embed)
    os.system('python3 off.py')


@client.command()
async def restart(ctx):
    if ctx.author.id != '634856429538508801':
        embed = nextcord.Embed(
            title='Keine Rechte!',
            colour=0xd15d4b
        )
        # embed.set_footer(icon_url=ctx.author.)
        await ctx.send(embed=embed)
        return
    embed = nextcord.Embed(
        title='Neustart!',
        colour=0x3ba55c
    )
    await ctx.send(embed=embed)

    os.system('sudo reboot')


client.run(TOKEN)
