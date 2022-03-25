import nextcord
from nextcord.ext import commands
import os

TOKEN = '' # add your token here

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
    os.system('reboot')


client.run(TOKEN)
