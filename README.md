## Botlian 
###### Another discord Music BOT
###### "This robot is an attempt to learn advanced python programming concepts, including topics such as OOP and asynchronous functions."




To run this bot you can directly clone this repository and import our requirements.txt

Remember/
in your console: $git clone https://github.com/julianjimenezm/Botlian.git

## Events and commands availables.

## General events.
- on_ready(): Automatically displays a message when the bot is connected:
          “ ** Botlian ** your Music Bot is ON!! “

- on_message(): Display a message when you type one predefined word. (under revision)


## General commands.
-/ $ : Predefined prefix

-/help: Displays all the available commands(ping, info, clear)

-/ping: Displays the time of response of our bot and the latency.

-/info: Displays all server information(Owner, Region, users_id , server_id)

-/clear: Will delete the past messages with the amount specified predefined = 5 lines

## Voice channel commands.
- /join - joins our bot to the voice channel
- /leave - leaves our bot from the voice channel

## Music commands:(see: $music).

-/yts str(arg*) : execute a search on youtube and it displays the thumbnail with the link of  the first result.

-/play : Run a search on youtube and play the song on our vocal channel. It also  initializes a volatil playlist(queue).

-/pause:pause the current songs in our vocal channel.

-/resume: resume paused songs.

-/skip:  skips the current song being played.

-/stop:  stops the current song and gets off from the vocal channel.

-/pl - displays the current music queue.



#### Final note: The robot is not programmed to identify if the vocal channel is empty, to avoid execution errors, 
#### please access to the vocal channel before executing the $join or $play commands.








# Have fun...
