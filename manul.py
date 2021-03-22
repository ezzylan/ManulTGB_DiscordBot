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
            print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    afiq_ammar_responses = ["diam la afiq ammar", "diam bodo afiq ammar",
                            "tak lawak afiq ammar", "bende bodo afiq ammar",
                            "sudah la afiq ammar", "buto ah afiq ammar",
                            "dah la afiq ammar, gi main bully tu", "cringe bodo afiq ammar",
                            "diam bodo afiq ammar, dah la main fifa tak pandai, baik tak yah main",
                            "macam tiber tapi senanya aku dah lama suka kau do fiq",
                            "aduh fiq sudah la tu, bila nak insaf ni"]

    sorry_responses = ["don't be sorry, be better", "takpe, jangan buat lagi"]

    manul_responses = ["jangan lah begitu"]

    if message.author.id == 701689699260956724:
        response = random.choice(afiq_ammar_responses)
        await message.channel.send(response)
    elif message.author.id == 693060533976301629:
        response = random.choice(manul_responses)
        await message.channel.send(response)
    elif 'sorry' in message.content or 'soghi' in message.content or 'sori' in message.content or 'maaf' in message.content:
        response = random.choice(sorry_responses)
        await message.channel.send(response)
    elif 'buto' in message.content:
        await message.channel.send('apa buto buto ni, tak baik mencarut')
    elif 'oi' in message.content:
        await message.channel.send('amende oi oi ni, cakap elok2 boleh tak')

client.run(TOKEN)
