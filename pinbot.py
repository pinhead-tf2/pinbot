#   ___                            _       
#  |_ _|_ __ ___  _ __   ___  _ __| |_ ___ 
#   | || '_ ` _ \| '_ \ / _ \| '__| __/ __|
#   | || | | | | | |_) | (_) | |  | |_\__ \
#  |___|_| |_| |_| .__/ \___/|_|   \__|___/
#                |_|

import discord
import os
import yaml
import asyncio
import datetime as DT 
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import bot
from typing_extensions import runtime
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#   ____        _     ____       _               
#  | __ )  ___ | |_  / ___|  ___| |_ _   _ _ __  
#  |  _ \ / _ \| __| \___ \ / _ \ __| | | | '_ \ 
#  | |_) | (_) | |_   ___) |  __/ |_| |_| | |_) |
#  |____/ \___/ \__| |____/ \___|\__|\__,_| .__/ 
#                                         |_|                  

#  __   __  ___            ___  __  
# |__) /  \  |     | |\ | |__  /  \ 
# |__) \__/  |     | | \| |    \__/                            

botPrefix = 'p!' # Choose your prefix 
bot = commands.Bot(command_prefix=botPrefix, help_command=None) # Don't worry about bot and client, they just needed the prefix you set above this line
client = discord.Client()
botName = "pinbot" # Your bot's name goes here
botCreator = "pinhead#4946" # Your identity here
botCreatorID = 246291288775852033 # Your user ID goes here
ver = ['v1.1.0', '06-06-2021'] # Bot version and release date goes here, Recommended format: major update.minor update.bugfix update
config = 'config.yml' # Open this file and put your bot's name and token there
botStartTime = DT.datetime.now()

#    __      __   ___ ___       __  
# | |  \    /__` |__   |  |  | |__) 
# | |__/    .__/ |___  |  \__/ |    

botLogsName = 'pinbot-logs' # Bot log channel goes here
botInboxName = 'pin-box' # Bot log channel goes here
botCommandsName = 'bot-cmds' # Community bot commands channel name goes here
botCommandsID = 852633053318742016 # Community bot commands channel ID goes here
botCommandsStaffName = 'pinbot-commands' # Staff commands channel name goes here
botCommandsStaffID = 852632618587652116 # Staff commands channel ID goes here
staffRoleID = 827723335072481311 # Staff role ID goes here

sayPermIDs = [246291288775852033, 495303865214959618, 474759210056548353, 488414757628411934, 638864530964742184] # People you want to give say perms go here
sayPermWordBlacklist = ['uwu', 'owo']

angerEmoji = '<:angerHeavy:851646266106445865>'
confusedEmoji = '<:sniperConfused:852004183544823849>'
disgustEmoji = '<:scoutDisgust:852004183381114921>'
unswagEmoji = '<:swagCatThumbsDown:852004183698964490>'
swagEmoji = '<:swagCatThumbsUp:852004184004755497>'
deathEmoji = '<a:death:851662800434626580>'
liveEmoji = '<a:live:851662800262529044>'

#  __   ___       __          __       ___  __       ___ 
# |__) |__   /\  |  \ \ /    /  \ |  |  |  |__) |  |  |  
# |  \ |___ /~~\ |__/  |     \__/ \__/  |  |    \__/  |  

@bot.event
async def on_ready():
    client.loop.create_task(rotateStatus())
    botVersion = ('{}'.format(ver[0]))
    botVersionReleaseDate = ('released {}'.format(ver[1]))
    botLogs = discord.utils.get(bot.get_all_channels(), name=botLogsName)
    await botLogs.send('**-------------- ' + botName + ' ' + botVersion + ' ' + botVersionReleaseDate + ' ---------------**\n **Current Time: **' + str(DT.datetime.now()) + '\n **Time to start:** ' + str((DT.datetime.now() - botStartTime)))

#   ____                                          _     
#  / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
# | |__| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
#  \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/

#       ___       __  
# |__| |__  |    |__) 
# |  | |___ |___ |    

@bot.command(pass_context=True) # This is the help command, make sure you put your commands here
async def help(ctx):
    msg = await ctx.fetch_message(ctx.message.id)
    author = ctx.message.author
    botVersion = ('{}'.format(ver[0]))
    botVersionReleaseDate = ('Released {}'.format(ver[1]))
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.set_thumbnail('https://cdn.discordapp.com/avatars/850785536133693480/ef462c3c61506768a0e82ac07b56170b.png?size=4096')
    embed.set_author(name="Please note that commands can't be sent here.")
    embed.add_field(name=botPrefix + 'ping, lag, latency', value=botName + ' reports how long it takes to respond to a command or message.', inline=False)
    embed.add_field(name=botPrefix + 'time, serverTime', value='States what time it is on the server that the bot is hosted on', inline=False)
    embed.add_field(name=botPrefix + 'uptime, runTime, runDuration', value=botName + ' reports how long it has run without going offline.', inline=False)
    if ctx.guild.get_role(staffRoleID) in ctx.author.roles: # If user has the role you defined, show commands in the if statement, highly recommended you put staff only commands here
        embed.add_field(name=botPrefix + 'mail, sendMail, dm', value='Command used to send modmail to users. Staff only command. Command goes as follows, and yes "" is required: mail 246291288775852033 Hello!', inline=False)
    if ctx.author.id in sayPermIDs:
        embed.add_field(name=botPrefix + 'say', value='Forces ' + botName + ' to send a message. Command is as follows: ' + botPrefix + 'say Hello There.', inline=False)
    embed.add_field(name=botPrefix + 'reactions', value='Displays info about the various reactions ' + botName + ' uses.', inline=False)
    embed.add_field(name=botPrefix + 'shutdown, stop, kill', value='Shuts down the bot safely and outputs it to logs.', inline=False)
    embed.set_footer(text=botName + ' ' + botVersion + ' | ' + botVersionReleaseDate + ' | Created by [' + botCreator + ']') 
    await author.send(embed=embed)
    await msg.add_reaction(swagEmoji)

#  __          __  
# |__) | |\ | / _` 
# |    | | \| \__> 

@bot.command(pass_context=True, aliases=['lag', 'latency'])
async def ping(ctx):
    msg = await ctx.fetch_message(ctx.message.id)
    if msg.channel.id == botCommandsID or msg.channel.id == botCommandsStaffID:
        botLatency = bot.latency*1000
        embed = discord.Embed(
            color = discord.Color.blue() 
        )
        embed.add_field(name='Pong! Delay:', value=botLatency)
        await ctx.send(embed=embed)
        return
    else:
        await msg.add_reaction(unswagEmoji)
        return

# ___          ___ 
#  |  |  |\/| |__  
#  |  |  |  | |___ 

@bot.command(pass_context=True, aliases=['serverTime'])
async def time(ctx):
    msg = await ctx.fetch_message(ctx.message.id)
    if msg.channel.id == botCommandsID or msg.channel.id == botCommandsStaffID:
        embed = discord.Embed(
            color = discord.Color.gold()
        )
        embed.add_field(name='Server Time:', value=DT.datetime.now())
        await ctx.send(embed=embed)
        return
    else:
        await msg.add_reaction(unswagEmoji)
        return

#       __  ___          ___ 
# |  | |__)  |  |  |\/| |__  
# \__/ |     |  |  |  | |___ 

@bot.command(pass_context=True, aliases=['runTime', 'runDuration'])
async def uptime(ctx):
    startTime = DT.datetime.now()
    msg = await ctx.fetch_message(ctx.message.id)
    if msg.channel.id == botCommandsID or msg.channel.id == botCommandsStaffID:
        runTime = startTime.replace(microsecond=0) - botStartTime.replace(microsecond=0)
        embed = discord.Embed(
            color = discord.Color.blue()
        )
        embed.add_field(name='Uptime (hh:mm:ss):', value=runTime)
        await ctx.send(embed=embed)
        return
    else:
        await msg.add_reaction(unswagEmoji)
        return

#  __           
# /__`  /\  \ / 
# .__/ /~~\  |  

@bot.command(pass_context=True)
async def say(ctx, *messageContent):
    if str(ctx.channel.type) == "private": 
        embed = discord.Embed(
            color = discord.Color.red()
        )
        embed.add_field(name='An error occured while executing the command "say". The error is as follows:', value="```diff\n - This command can't be run in my DMs!```")
        return await ctx.send(embed=embed)
    msg = await ctx.fetch_message(ctx.message.id)
    if messageContent == ():
        return await msg.add_reaction(confusedEmoji)
    else:
        if 'owo' in messageContent: 
            return await msg.add_reaction(angerEmoji)
        if 'uwu' in messageContent: 
            return await msg.add_reaction(angerEmoji)
        if ctx.author.id in sayPermIDs:
            await ctx.send(" ".join(messageContent[:]))
            await msg.delete()
        else:
            await msg.add_reaction(deathEmoji)

#  __   ___       __  ___    __        __  
# |__) |__   /\  /  `  |  | /  \ |\ | /__` 
# |  \ |___ /~~\ \__,  |  | \__/ | \| .__/ 

# @bot.command(pass_context=True, aliases=['reactions'])
# async def reactions(ctx):
    

#  __            ___  __   __            
# /__` |__| |  |  |  |  \ /  \ |  | |\ | 
# .__/ |  | \__/  |  |__/ \__/ |/\| | \| 

@bot.command(pass_context=True, aliases=['stop', 'kill'])
async def shutdown(ctx):
    msg = await ctx.fetch_message(ctx.message.id)
    botLogs = discord.utils.get(bot.get_all_channels(), name=botLogsName)
    if ctx.author.id == botCreatorID:
        await botLogs.send("**" + botName + " is shutting down...**")
        await msg.add_reaction(deathEmoji)
        exit()
    else:
        await msg.add_reaction(angerEmoji)

# __  __           _                 _ _ 
#|  \/  | ___   __| |_ __ ___   __ _(_) |
#| |\/| |/ _ \ / _` | '_ ` _ \ / _` | | |
#| |  | | (_) | (_| | | | | | | (_| | | |
#|_|  |_|\___/ \__,_|_| |_| |_|\__,_|_|_|

@bot.listen('on_message')
async def on_message(ctx):
    msg = await ctx.fetch_message(ctx.message.id)
    sender_id = str(ctx.author.id)
    botLogs = discord.utils.get(bot.get_all_channels(), name=botLogsName)
    botInbox = discord.utils.get(bot.get_all_channels(), name=botInboxName)
    if ctx.author == bot.user:
        return
    if str(ctx.channel.type) == "private": 
        if ctx.content.startswith("p!"):
            msg.add_reaction(unswagEmoji)
            return
        await botLogs.send("**New Modmail!**\n" + "**From:** <@" + sender_id + ">!\n" + "**Message: **" + ctx.content)
        embed = discord.Embed(
            color = discord.Color.green()
        )
        embed.add_field(name='User ID:', value=sender_id)
        await botInbox.send("**New Modmail!**\n" + "**From:** <@" + sender_id + ">!\n" + "**Message: **" + ctx.content, embed=embed)

#  |\/|  /\  | |    
#  |  | /~~\ | |___ 

@bot.command(pass_context=True, aliases=['sendMail', 'dm'])
async def mail(ctx, user: discord.User, *messageContent):
    msg = await ctx.fetch_message(ctx.message.id)
    botLogs = discord.utils.get(bot.get_all_channels(), name=botLogsName)
    botCommandsStaff = discord.utils.get(bot.get_all_channels(), name=botCommandsStaffName)
    if messageContent == ():
        return await msg.add_reaction(confusedEmoji)
    if ctx.guild.get_role(staffRoleID) in ctx.author.roles:
        if ctx.channel == botCommandsStaff: # Staff commands channel goes here
            sendToUser = "**New Modmail from** <@" + str(ctx.author.id) + ">!\n"
            sendToLogs = "**Modmail sent to** <@" + str(user.id) + ">.\n**Message sent:** "
            embed = discord.Embed(
            color = discord.Color.green()
            )
            embed.add_field(name='Modmail sent!', value="Sucessfully sent modmail to <@" + str(user.id) + ">.")
            await user.send(sendToUser + " ".join(messageContent[:]))
            await botLogs.send(sendToLogs + " ".join(messageContent[:]))
            await ctx.send(embed=embed)
        else: 
            await msg.add_reaction(deathEmoji)
    else:
        await msg.add_reaction(deathEmoji)

#   ____             _                                   _   _____         _        
#  | __ )  __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| | |_   _|_ _ ___| | _____ 
#  |  _ \ / _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` |   | |/ _` / __| |/ / __|
#  | |_) | (_| | (__|   < (_| | | | (_) | |_| | | | | (_| |   | | (_| \__ \   <\__ \
#  |____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|   |_|\__,_|___/_|\_\___/
#                        |___/                                                      

#  __   __   ___  __   ___       __   ___     __   __  ___      ___    __       
# |__) |__) |__  /__` |__  |\ | /  ` |__     |__) /  \  |   /\   |  | /  \ |\ | 
# |    |  \ |___ .__/ |___ | \| \__, |___    |  \ \__/  |  /~~\  |  | \__/ | \| 

async def rotateStatus():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pinhead's server"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="what time it is"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for modmail, DM me to send some!"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Discord latency"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for errors"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game(name="Team Fortress 2"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for new members"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="uptime"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for messages to react to"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for pings"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="to status recommendations"))
        await asyncio.sleep(60)
        await bot.change_presence(activity=discord.Game(name="Titanfall 2"))
        await asyncio.sleep(60)

#   ____                ____        _             ____              _ _     _____                _     
#  |  _ \ _   _ _ __   | __ )  ___ | |_          |  _ \  ___  _ __ ( ) |_  |_   _|__  _   _  ___| |__  
#  | |_) | | | | '_ \  |  _ \ / _ \| __|  _____  | | | |/ _ \| '_ \|/| __|   | |/ _ \| | | |/ __| '_ \ 
#  |  _ <| |_| | | | | | |_) | (_) | |_  |_____| | |_| | (_) | | | | | |_    | | (_) | |_| | (__| | | |
#  |_| \_\\__,_|_| |_| |____/ \___/ \__|         |____/ \___/|_| |_|  \__|   |_|\___/ \__,_|\___|_| |_|

bot.run(TOKEN)