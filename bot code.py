import discord
import random
from discord import channel
from discord.ext import commands
import asyncio

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
    leaveMessage = discord.Embed(title = "A user has left the guild", color=discord.Color.dark_red())
    #leaveMessage.setTitle("A user has left the guild")
    #leaveMessage.setMessage(client.get_user)
    leaveMessage.add_field(name="Member Name", value=member.name, inline=True)
    leaveMessage.add_field(name="Display Name", value=member.display_name, inline=False)
    leaveMessage.add_field(name="Join Date" , value=member.joined_at, inline=False)
    leaveMessage.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=leaveMessage)

@client.command()
async def hi(ctx):
    greetings = ["Hello there!", "Hiya scrub", "Hi", "Want a shell?", "Greetings!"]
    await ctx.send(random.choice(greetings))

@client.command()
async def bye(ctx):
    farewells = ["Bye!", "See you later!", "Ciao!", "Goodbye!", "Adieu!"]
    await ctx.send(random.choice(farewells))

@client.command()
async def dm(ctx):
  await ctx.message.author.send("Hi! My name is ShellProject, great to meet you!")

@client.command()
async def delete(ctx, amount=1):
    #print("This went through")
    amount = amount + 1
    await ctx.channel.purge(limit=amount)

@client.command()
async def poll(ctx, question, option1 = None, option2 = None):
  if option1 == None and option2 == None:
    await ctx.channel.purge(limit=1)
    message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**\n")
    await message.add_reaction('❎')
    await message.add_reaction('✅')

client.run(TOKEN)
