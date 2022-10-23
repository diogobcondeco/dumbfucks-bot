import discord
import os
from dotenv import load_dotenv
load_dotenv()

client = discord.Client(intents=discord.Intents.default())

greetings = ['hello', 'hi', 'hey']


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg for word in greetings):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
