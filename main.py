import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents().default()

client = discord.Client(intents=intents)

greetings = ["hello", "hi", "hey"]
channel_ids = {"welcome": 963791333707894925}

# Client Events


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    print(f"{message.author}, just send the message: {message.content}")
    if message.author == client.user:
        return

    if message.author.id == 379048417353269249:
        for i in range(10):
            if i == 1:
                await message.channel.send("CA GANDA NOOB")

    if any(word in message.content for word in greetings):
        await message.channel.send("Hello!")


@client.event
async def on_member_join(member):
    print(member.name, "just joined!")
    channel = client.get_channel(channel_ids["welcome"])
    role = discord.utils.get(member.server.roles, id="1033854993914150984")

    await channel.send(f"Hi {member.name}, welcome to Dumbfucks!")
    await client.add_roles(member, role)


@client.event
async def on_member_leave(member):
    print(member.name, "just left!")
    channel = client.get_channel(channel_ids["welcome"])
    await channel.send(f"Goodbye {member.name}, it was fun while it lasted")

# Bot Events

# start the bot
client.run(TOKEN)
