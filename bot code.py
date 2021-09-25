import discord
import random
from discord.ext import commands

TOKEN = open("token.txt","r").readline()

client = commands.Bot(command_prefix= '!')

@client.event
async def ready_msg():
    print("Systems Online!")

@client.command()
async def hi(ctx):
    greetings = ["Hello there!", "Hiya scrub", "Hi", "Want a shell?", "Test"]
    await ctx.send(random.choice(greetings))

client.run(TOKEN)
