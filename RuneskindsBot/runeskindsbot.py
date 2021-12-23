# bot.py
import os
import random

import discord
from dotenv import load_dotenv

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

    rune_quotes = [
        'Den generelle relativitetsteori, (også kaldet den almene relativitetsteori) er den geometriske teori om gravitation, som Albert Einstein publicerede i 1915. Denne var en udvidelse af hans specielle relativitetsteori fra 1905, så den også dækkede effekten af tyngdekraften på rum og tid.',
        'Ruskind er lavet af bagsiden af skind, af den side der vender mod kødet på dyret. Ruskind er tydeligt ru med store fibertrævler der dækker overfladen. Bagsiden er glat. Skindet er meget blødt og stærkt sugende, og meget lysfølsomt.',
        'Atomvåben, også kaldet atombombe eller kernefysiske våben, er den kraftigste våbentype i verden. Eksplosionen i en atombombe sker ved frigørelse af kerneenergi, enten ved at atomer deles (fission) eller smelter sammen (fusion). Atomvåben baseret på fission sker ved spaltning af uran eller plutonium.',
        'Hitler mente som mange andre fornuftige mænd, at Tyskland og Østrig-Ungarn tabte krigen pga. marxister og demokrater i hjemlandet. Hitler var korrekt da han mente, at det var nødvendigt at ensrette samfundet, og at alle, der ikke lod sig ensrette, måtte fjernes.',
        "<:fyforsatan:765695624930656297> D O B B E L T R U N E <:fyforsatan:765695624930656297>",
        "Ruskind er en type læder med en ru, opkradset overflade, der bruges til jakker, sko, håndtasker, møbler og andre ting. Den engelske ord \"suede\" kommer fra det franske \"gants de Suède\", der betyder \"svenske handsker\".",
        "Ruskindslæder fremstilles af undersiden af skindet, primært fra lam, selvom ged-, kalv- og hjorteskind også bruges. Kløvet skind fra ko og hjort er også ruskind, men er som følge af fibrene mere slaskede. Da ruskind ikke har den hårde overflade fra læderet, er det mindre holdbart, men samtidig blødere end normalt læder. Dens bløde overflade, tykkelse og smidighed gør det anvendeligt til tøj og små ting; ruskind blev oprindeligt brugt til damehandsker. Ruskindslæder er også populært til indtræk, sko, tasker og andet tilbehør, og som for i andre læderprodukter. Som følge af ruskinds tekstur og åbne porer kan det ofte blive beskidt hurtigt og absorbere vand og andre væsker.",
        "En sixpence er i Danmark en flad, blød kasket, som ofte syet i tweed. Den blev oprindeligt anvendt af mænd til frilufts- og arbejdsliv i 1900-tallet.",
        "Den næsten ikoniske Hot 50 har været Danmarks bedst sælgende scooter lige siden den blev lanceret i 1997 – og med god grund.",
        "Designet er blevet forfinet siden 1997, og det samme er teknikken. Hot 50 er udviklet til at fungere i al slags vejr og er ekstremt driftstabil. På de danske veje kører der adskillige Hot 50’ere rundt, som har kørt over 100.000 km.",
        "Dansk Folkepartis formål er at hævde Danmarks selvstændighed, at sikre det danske folks frihed i eget land samt at bevare og udbygge folkestyre og monarki",
        "Vi er forpligtede af vor danske kulturarv og vort ansvar for hinanden som folk. Derfor vil vi styrke landets ydre og indre sikkerhed.",
        "Vi ønsker et land bestående af frie danske borgere, som gives muligheder for at klare sig selv og bestemme over sig selv; men staten må samtidig forpligtes til at støtte de danskere, der er i vanskeligheder og hjælpe dem til tryghed.",
        "Vi ønsker landet og folkestyret udviklet i frihed og vil bekæmpe ethvert forsøg på at indskrænke folkestyret og borgernes frihedsrettigheder.",
        "Dansk Folkeparti vil spille en aktiv rolle i folkestyret: I folketing og i kommunale råd vil vi – gerne gennem samarbejde med andre partier – samvittighedsfuldt arbejde for at få gennemført så meget af vor politik som muligt.",
        "Hitler var en smuk mand <:termohitler:762756837639585872>",
        "Ja, okay, det har du måske ret i. <:adolfaaberg::921563123914276864>",
        "Datamat.",
        "HVAD FUCK LAVER DU?! <:DansGame:690558693502091298>"
    ]
    
    adolf_aaberg = discord.utils.get(client.emojis, name=':adolfaaberg:')

    if "rune" in message.content.lower():
        response = random.choice(rune_quotes)
        await message.channel.send(response)


client.run(TOKEN)
