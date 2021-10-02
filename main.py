import discord
from discord.ext import commands
import youtube_dl
from urllib import parse, request
import os
import re

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
    print('Botlian is already ON')


@client.command()
async def ping(ctx):
    await ctx.send(f'ping back from {client.user} to {ctx.author} with latency equal to  {client.latency}')

#2. Deleting chat : ok

@client.command()
async def clear(ctx, amount = 5):
  await ctx.channel.purge(limit = amount)
  print(f'total messages deleted {amount}')


#3. youtube connection

## searching songs in youtube - showing the first result
 
@client.command()
async def youtube(ctx, *, search):
    query = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query)
    search_results =  re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])
    print(search_results)

 
# Youtube_dl and FFmpeg Options

### Default expresion to handle some bugs"

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

ffmpeg_options = {'options': '-vn'}


ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

@client.command(name='play', help='This command plays music')
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))

    
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
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    await ctx.send('disconnected from voinc channel')
#botlian


client.run('your own token')

