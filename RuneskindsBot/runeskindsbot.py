#!/usr/bin/env python
# bot.py
import os
import random
import discord
import requests
from discord.message import Message
from dotenv import load_dotenv
from messages import *

def calculate_btc_in_dkk():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    rate = (1 / 7.44) / float(data["bpi"]["EUR"]["rate_float"])
    return rate


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return


        
    if "rune" in message.content.lower() or (message.author.id == 350370882394259457 and random.randint(0, 1) == 0):
        response = random.choice(rune_quotes)
        await message.channel.send(response)
          
    elif message.author.id == 247448396548407300 and random.randint(0, 30) >= 27:
        response = random.choice(mikkel_quotes)
        await message.channel.send()
        
    elif message.author.id == 151073786198753281 and random.randint(0, 30) >= 27:
        response = random.choice(kineser_quotes)
        await message.channel.send(response)
        
    if "<:pogconnect:690570562589818891>" in message.content or "<:RuneCoin:765693246574821406>" in message.content or "<:bitconnect:690569885331357726>" in message.content:
        await message.channel.send(f"En ægte dansk krone er lige nu {calculate_btc_in_dkk():.20f} Bitcoins værd <:RuneCoin:765693246574821406>")
        



client.run(TOKEN)