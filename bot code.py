import discord
import random
import string
from discord import channel
from discord.ext import commands
import asyncio
import requests
import json

from discord.ext.commands import context

TOKEN = open("token.txt","r").readline()

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = commands.Bot(command_prefix= '!', intents = intents)

URL = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,racist&type=single"

print(discord.__version__)

@client.event
async def on_ready():
    print("Systems Online!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(891084381681229837)
    roleList = client.get_guild(891084381681229834).roles
    await member.add_roles(roleList[1])
    await channel.send("Welcome " + member.mention + "! Enjoy your stay!")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(891373492489060462)
    leaveMessage = discord.Embed(title = "A user has left the guild", color=discord.Color.dark_red())
    #leaveMessage.setTitle("A user has left the guild")
    #leaveMessage.setMessage(client.get_user)
    leaveMessage.add_field(name="Member Name", value=member.name, inline=True)
    leaveMessage.add_field(name="Display Name", value=member.display_name, inline=False)
    leaveMessage.add_field(name="Join Date" , value=member.joined_at, inline=False)
    leaveMessage.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=leaveMessage)    

#event vs command

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
async def spongebob(ctx, input):
    new_msg = ""
    for s in input:
        num = random.randint(1, 100)
        if(num % 2 == 0):  
            new_msg += s.lower()
        else:
            new_msg +=s.upper()
    await ctx.send(new_msg)

@client.command()
async def img(ctx):
    chars = string.ascii_letters + string.digits
    code = ""
    for x in range(5):
        code+= random.choice(chars)
    #imglink = "https://i.imgur.com/" + code + ".jpg"
    rand = random.randint(0,1000000)
    imglink = 'https://source.unsplash.com/random?sig=' + str(rand)

    msg = discord.Embed(title="I found an image!")
    msg.set_image(url=imglink)
    await ctx.send(embed=msg)

@client.command()
async def poll(ctx, question, option1 = None, option2 = None, option3 = None, option4 = None, option5= None, option6 = None):
    if option1 == None and option2 == None:
        await ctx.channel.purge(limit=1)
        message = await ctx.send(f"```New poll: \n{question}```\n**✅ = Yes**\n**❎ = No**\n")
        await message.add_reaction('✅')
        await message.add_reaction('❎')
    else:
        await ctx.channel.purge(limit=1)
        pollQuestion = discord.Embed(title="Poll Question: " + question, description="🇦 " + option1 + "\n🇧 " + option2, color=discord.Color.blue())

        addOptions = [option3, option4, option5, option6]
        reactOptions =  ['🇨', '🇩', '🇪', '🇫']
        index = 0

        for x in addOptions:
            if x is None:
                break

            pollQuestion.description += "\n" + reactOptions[index] + " " + x
            index = index + 1

        msg = await ctx.send(embed=pollQuestion)
        await msg.add_reaction('🇦')
        await msg.add_reaction('🇧')

        for emoteReaction in reactOptions[:index]:
            await msg.add_reaction(emoteReaction)

@client.command()
async def get_joke(ctx):
    request = requests.get(URL)
    json_data = json.loads(request.text)
    joke = json_data["joke"]
    await ctx.send(joke)
    
            
client.run(TOKEN)
