## Setting up our Python enviroment

import discord
from discord.utils import get
from discord.ext import commands
from Music import MusicSet 
from urllib import parse, request
import os
import re


## This is how to work with the dot-enviroment to keep safe your private info. 

# ".env" is the container folder for private info.
#from dotenv import load_dotenv  
#load_dotenv()
#token = os.getenv('token1')

######################################################################################""

#Initializing BOT

client = commands.Bot(command_prefix='$',help_command=None, intents = discord.Intents.all())

# Getting Ready:

@client.event
async def on_ready():
    print(f' ** Botlian ** your  Music Bot is ON!!!')


@client.command()
async def ping(ctx):
    await ctx.channel.send(f'ping back from {client.user} to {ctx.author} with latency equal to  {client.latency}')


## Help commands

@client.command() 
async def help(ctx):
   
    emBed = discord.Embed(title="Bot help", description="All available help commands", color=0x42f5a7)
    emBed.add_field(name="ping", value="Test the systems response time and latency", inline=False)
    emBed.add_field(name="info", value="Retrive server information", inline=False)
    emBed.add_field(name="clear", value="Clearing chat, (5 lines by default)", inline=False)
    emBed.set_footer(text='test footer', icon_url='https://media-exp1.licdn.com/dms/image/C560BAQFHd3L0xFcwcw/company-logo_200_200/0/1550868149376?e=2159024400&v=beta&t=LyKtz-V4W8Gfwzi2ZqmikaI9GcUXI3773_aa3F3nIhg')
    await ctx.channel.send(embed=emBed)


# Server information

@client.command(help = "Prints Server Information")
async def info(ctx):
    owner=str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc=ctx.guild.description
    
    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    members=[]
    async for member in ctx.guild.fetch_members(limit=150) :
        await ctx.send(f"Name : {member.display_name}\t Status : {str(member.status)}\n Joined at {str(member.joined_at)}")



##  Setting up some events  

# Send private message to new members

    
#  Setting up default messages. 

#(on_message events) dont work at the same time with other command or events
# automaticlly all the bot stops working. I dont understand the theoric concepts why this occurs.
"""
@client.event
async def on_message(message):
  if message.content.startswith('$salut'):
    await message.channel.send(f'Salut {message.author} Bienvenue')
  if message.content.startswith('$hola'):
     await message.channel.send(f'Hola {message.author} Bienvenido')
  if message.content.startswith('$hello'):
    await message.channel.send(f'Grettings {message.author} Welcome')
"""


## Manual methods to get in/out of voice channel.
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.send('Connected to the voice channel')


@client.command()
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    await ctx.send('disconnected from voice channel')


## clearing Environnement
'''Deletting chat'''

@client.command()
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit = amount)
  print(f'total messages deleted {amount}')



## Music Instances
''' With this presentation is more clear to know all the actions we have available to play music with our bot'''

InstanceOf = MusicSet()

#  retreive youtube thumbnailed song
@client.command() 
async def yts(ctx, * ,search):
    '''Youtube search and reatriving first element with the own Youtube tumbnail'''
    query = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query)
    search_results =  re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
    print(search_results)

# Logical buttons to play music, its possible to implement "Physical" buttoms implementing some embeds formats.

@client.command() 
async def play(ctx,* ,search: str):
    await InstanceOf.play(ctx, search)

@client.command()
async def stop(ctx):
    await InstanceOf.stop(ctx)

@client.command()
async def pause(ctx):
    await InstanceOf.pause(ctx)

@client.command()
async def resume(ctx):
    await InstanceOf.resume(ctx)

@client.command()
async def pl(ctx):
    await InstanceOf.pl(ctx)

@client.command()
async def skip(ctx):
    await InstanceOf.skip(ctx)

# List of musics commands
@client.command()
async def music(ctx):

   
    emBed = discord.Embed(title=" Music help", description="All available music bot commands", color=0x40f5a7)
    emBed.add_field(name="play", value="start a song and gets available the playlist", inline=False)
    emBed.add_field(name="stop", value="stop current song", inline=False)
    emBed.add_field(name="pause", value="pause current song", inline=False)
    emBed.add_field(name="resume", value="resume paused current song", inline=False)
    emBed.add_field(name="pl", value="queue info", inline=False)
    emBed.add_field(name="skip", value="skip the songs", inline=False)
    emBed.set_footer(text='Botlian your Discord Music bot!', icon_url='https://media-exp1.licdn.com/dms/image/C560BAQFHd3L0xFcwcw/company-logo_200_200/0/1550868149376?e=2159024400&v=beta&t=LyKtz-V4W8Gfwzi2ZqmikaI9GcUXI3773_aa3F3nIhg')   
    await ctx.channel.send(embed=emBed)

token1 = "your own discord token"

client.run(token1)
