import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client(intents=discord.Intents.default())

greetings = ['hello', 'hi', 'hey']
welcome_channel = 963791333707894925


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == 379048417353269249:
        await message.channel.send('CA GANDA NOOB')

    if any(word in message.content for word in greetings):
        await message.channel.send('Hello!')


@client.event
async def on_member_join(member):
    channel = client.get_channel(welcome_channel)
    role = discord.utils.get(member.server.roles, id='1033854993914150984')

    await channel.send(f'Hi {member.name}, welcome to Dumbfucks!')
    await client.add_roles(member, role)


async def on_member_leave(member):
    channel = client.get_channel(welcome_channel)
    await channel.send(f'Goodbye {member.name}, it was fun while it lasted')

client.run(TOKEN)
