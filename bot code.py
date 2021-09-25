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

@client.command()
async def bye(ctx):
    farewells = ["Bye!", "See you later!", "Ciao!", "Goodbye!", "Adieu!"]
    await ctx.send(random.choice(farewells))

@client.command()
async def dm(ctx):
  await ctx.message.author.send("Hi! My name is ShellProject, great to meet you!")

@client.command()
async def poll(ctx, question, option1 = None, option2 = None):
  if option1 == None and option2 == None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**\n")
    await message.add_reaction('❎')
    await message.add_reaction('✅')

client.run(TOKEN)