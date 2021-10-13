oken")
import discord
from discord.ext import commands
import youtube_dl
from urllib import parse, request
import os
import re

client = commands.Bot(command_prefix = '$')

# Connection and first responses

@client.event
async def on_ready():
    print('Botlian is ON')


@client.command()
async def ping(ctx):
    await ctx.send(f'ping back from {client.user} to {ctx.author} with latency equal to  {client.latency}')


#  This event causes conflicts with the others events and commands, i dont know why. to check!!!
'''
@client.event
async def on_message(message):
  if message.content.startswith('$salut'):
    await message.channel.send(f'Salut {message.author} Bienvenue')
  if message.content.startswith('$hola'):
     await message.channel.send(f'Hola {message.author} Bienvenido')
  if message.content.startswith('$hello'):
    await message.channel.send(f'Grettings {message.author} Welcome')
'''
# Clearing chat

@client.command()
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit = amount)
  print(f'total messages deleted {amount}')


#joining and leaving Vocal channel

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
# Search and reatrive youtube url

@client.command()
async def youtube(ctx, *, search):
    query = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query)
    search_results =  re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
    print(search_results)



# Download YouTube MP3
 # > Not reivent the Wheel, learn how to use properly

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' 
}

ffmpeg_format_options = {'options': '-vn'}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

# What is Classmethod used for?
#    Uses of classmethod() function are used in factory design patterns where we want to call 
#    many functions with the class name rather than an object.


    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_format_options), data=data)

@client.command(name='play', help='This command plays music')
async def play(ctx, url):
    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send(f'**Now playing:** {player.title}')

@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")

@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    await ctx.send('disconnected from voice channel')

# details of our server

@client.command(help = "Prints details of Server")
async def where(ctx):
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
        await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name,str(member.status),str(member.joined_at)))

my_secret = os.environ['token1']
client.run(my_secret)
