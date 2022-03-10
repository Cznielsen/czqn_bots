#!/usr/bin/env python
# bot.py
import os
import random
import discord
import requests
from discord.message import Message
from dotenv import load_dotenv
import messages
import unit_conversion as uc
import re

def find_word_match_dumb(keywords, string):
    words = []
    for word in string.split():
        if word in keywords:
            words.append(word)
        if len(words) > 1:
            return words
    return words

def calculate_btc_in_dkk():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    rate = (1 / 7.44) / float(data["bpi"]["EUR"]["rate_float"])
    return rate

def handle_conversions(message_content):
    if any(num.isdigit() for num in message_content) and any(key in message_content for key in uc.length_dict_ny.keys()):
        number = float(re.search(r'\d+', message_content).group())
        unit = find_word_match_dumb(uc.length_dict_ny.keys(), message_content)
        
        gammel = bool(random.getrandbits(1))
        gammel_suffix = " (før 1835). <:DendiFace:690558683138097152>" if gammel else ". <:DendiFace:690558683138097152>"
        
        if len(unit) == 0:
            return
        elif len(unit) == 1:
            result_val, result_key = uc.length_to_random(unit[0], number, gammel)
        else:
            result_val, result_key = uc.length_to_length(unit[0], number, unit[1], gammel)
            
        response = f'{number:,} {unit[0]} svarer til {result_val:,} {result_key}{gammel_suffix}'.replace(',', ' ')
        return response
        


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

    conversion = handle_conversions(message.content.lower())
    if conversion:
        await message.channel.send(conversion)
        
    if "rune" in message.content.lower() or (message.author.id == 350370882394259457 and random.randint(0, 1) == 0):
        response = random.choice(messages.rune_quotes)
        await message.channel.send(response)
          
    elif message.author.id == 247448396548407300 and random.randint(0, 30) >= 5:
        response = random.choice(messages.mikkel_quotes)
        await message.channel.send()
        
    elif message.author.id == 151073786198753281 and random.randint(0, 30) >= 27:
        response = random.choice(messages.kineser_quotes)
        await message.channel.send(response)
        
    if "<:pogconnect:690570562589818891>" in message.content or "<:RuneCoin:765693246574821406>" in message.content or "<:bitconnect:690569885331357726>" in message.content:
        await message.channel.send(f"En ægte dansk krone er lige nu {calculate_btc_in_dkk():.20f} Bitcoins værd <:RuneCoin:765693246574821406>")
        



client.run(TOKEN)