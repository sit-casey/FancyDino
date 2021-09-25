import discord
import random
from discord.ext import commands

TOKEN = open("token.txt","r").readline()

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix= '!', intents = intents)

print(discord.__version__)

@client.event
async def on_ready():
    print("Systems Online!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(891084381681229837)
    await channel.send("Welcome " + member.mention + "! Enjoy your stay!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(891084381681229837)
    leaveMessage = discord.Embed
    leaveMessage.setTitle("A user has left the guild")
    leaveMessage.setMessage(client.get_user)
    leaveMessage.set_image("testing.png")
    await channel.send(leaveMessage)

#Above is events, below is commands?

@client.command()
async def hi(ctx):
    greetings = ["Hello there!", "Hiya scrub", "Hi", "Want a shell?", "Greetings!"]
    await ctx.send(random.choice(greetings))


client.run(TOKEN)
