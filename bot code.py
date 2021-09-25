import discord
import random
from discord.ext import commands

TOKEN = open("token.txt","r").readline()

client = commands.Bot(command_prefix= '!')

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guild = True

client2 = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    channel = client2.get_channel(891084381681229837)
    await channel.send("Welcome!" + "You are currently " + member.status)


@client.event
async def ready_msg():
    print("Systems Online!")


@client.command()
async def hi(ctx):
    greetings = ["Hello there!", "Hiya scrub", "Hi", "Want a shell?", "Test"]
    await ctx.send(random.choice(greetings))

client.run(TOKEN)
