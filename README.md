## Botlian.
###### Another discord Music BOT

The goal to implement this bot was to bring into practice some advanced programming concepts
such as OOP and asynchronous functions.

The result of the project is nothing more than the adaptation of certain theoretical concepts. 
So there is no claim of originality, it is just an exercise that allowed us to assimilate and 
implement some python concepts, in this case coroutines through music bot connections.


## Set-up.

- Setup properly your python ENV 

- To run this bot you can directly clone this repository and import  and install our requirements.txt

>in your console:
>
>$ git clone https://github.com/julianjimenezm/Botlian.git
>
>$ pip install -r requirements.txt

- Dont forget use your own discord token into your code.

- if you want to access to our server use: https://discord.gg/k2fMPJHC and ask for the current token.


## Events and commands availables.


### General events.
- on_ready(): Automatically displays a message when the bot is connected:
          “ ** Botlian ** your Music Bot is ON!! “

- on_message(): Display a message when you type one predefined word. (under revision)


### General commands.

-/ $ : Predefined prefix

-/help: Displays all the available commands(ping, info, clear)

-/ping: Displays the time of response of our bot and the latency.

-/info: Displays all server information(Owner, Region, users_id , server_id)

-/clear: Will delete the past messages with the amount specified predefined = 5 lines


### Voice channel commands.

- The robot is not programmed to identify if the vocal channel is empty, to avoid execution errors, 
  please access to the vocal channel before executing the $join or $play commands.

- /join - joins our bot to the voice channel
- /leave - leaves our bot from the voice channel
- 

### Music commands:(see: $music).

-/yts str(arg*) : execute a search on youtube and it displays the thumbnail with the link of  the first result.

-/play : Run a search on youtube and play the song on our vocal channel. It also  initializes a volatil playlist(queue).

-/pause:pause the current songs in our vocal channel.

-/resume: resume paused songs.

-/skip:  skips the current song being played.

-/stop:  stops the current song and gets off from the vocal channel.

-/pl - displays the current music queue.



#### Final note:

If you are having any kind of problem with the music bot execution, please let us know.



#### Have fun...
