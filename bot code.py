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
    leaveMessage = discord.Embed(title = "A user has left the guild")
    #leaveMessage.setTitle("A user has left the guild")
    #leaveMessage.setMessage(client.get_user)
    leaveMessage.add_field(name="Member Name", value=member.name, inline=True)
    leaveMessage.add_field(name="Display Name", value=member.display_name, inline=True)
    leaveMessage.add_field(name="Join Date" , value=member.joined_at, inline=False)
    leaveMessage.set_thumbnail(url="https://i.pinimg.com/564x/6b/05/d9/6b05d9114529fe7833ae94a2d790f2fc.jpg")
    await channel.send(embed=leaveMessage)

@client.command()
async def hi(ctx):
    greetings = ["Hello there!", "Hiya scrub", "Hi", "Want a shell?", "Greetings!"]
    await ctx.send(random.choice(greetings))

client.run(TOKEN)
