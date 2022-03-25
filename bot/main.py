import os

import RPi.GPIO as GPIO
import nextcord
from nextcord.ext import commands

TOKEN = ''

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
async def light(ctx, light_number=None, onoff=None):
    GPIO.setmode(GPIO.BCM)
    if light_number == '1':
        pin = 17
        if onoff == 'on':
            embed = nextcord.Embed(
                title=f'Licht {light_number} an!',
                colour=0x3ba55c
            )
            await ctx.send(embed=embed)

            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)
            print('Light 1 on')
        elif onoff == 'off':
            embed = nextcord.Embed(
                title=f'Licht {light_number} aus!',
                colour=0xd15d4b
            )
            await ctx.send(embed=embed)

            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
            print(f'Light {light_number} an!')

        else:
            embed = nextcord.Embed(
                title='Error!',
                colour=0xd15d4b,
            )
            await ctx.reply(embed=embed)

    else:
        embed = nextcord.Embed(
            title='Error!',
            colour=0xd15d4b,
        )
        await ctx.reply(embed=embed)

@client.command()
async def restart(ctx):
    os.system('reboot')


client.run(TOKEN)
