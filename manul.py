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
                            "tak lawak afiq ammar", "bende bodo afiq ammar"]

    if message.author.id == 701689699260956724:
        response = random.choice(afiq_ammar_responses)
        await message.channel.send(response)

client.run(TOKEN)
