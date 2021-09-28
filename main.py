import discord
from discord.ext import commands
import youtube_dl
from urllib import parse, request
import os
import re

client = commands.Bot(command_prefix='$')

#1. veryfing connection: ok

@client.event
async def on_ready():
    print('the bot is already ON ')


@client.command()
async def ping(ctx):
    await ctx.send(f'ping back from {client.user} to {ctx.author} with latency equal to  {client.latency}')

#2. Deleting chat : ok

@client.command()
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit = amount)
  print(f'total messages deleted {amount}')


#3.First attempt - youtube connection

@client.command()
async def youtube(ctx, *, search):
    query = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query)
    search_results =  re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

my_secret = os.environ['token']
client.run(my_secret)
