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
                            "tak lawak afiq ammar", "bende bodo afiq ammar", "sudah la afiq ammar"]

    megat_responses = ["diam la megat", "diam bodo megat",
                       "tak lawak megat", "bende bodo megat", "sudah la megat"]

    if message.author.id == 701689699260956724:
        response = random.choice(afiq_ammar_responses)
        await message.channel.send(response)
    elif message.author.id == 636985287897120798:
        response = random.choice(megat_responses)
        await message.channel.send(response)

client.run(TOKEN)
