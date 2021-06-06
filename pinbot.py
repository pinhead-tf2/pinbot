from typing_extensions import runtime
import discord
import os
import datetime as DT 
import sLOUT as lout
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix='p$', help_command=None) # Choose your prefix here, don't worry about help_command as it is created later
botPrefix = 'p$' # Choose your prefix again, things like sendHelp use this prefix autofill
botName = "pinbot" # Your bot's name goes here
botCreator = "pinhead#4946"
ver = ['v1.0.0', '06-06-2021'] # Bot version and release date goes here, major update.minor update.bugfix update.

guild_ids = [827647182051737651] # Server ID goes here
sayPermIDs= [246291288775852033, 495303865214959618, 474759210056548353, 488414757628411934, 638864530964742184]
botStartTime = DT.datetime.now()
config = 'config.yml' # Open this file and put your bot's name and token there

lout.writeFile(botName + 'Logs.txt', '\n' + botName + 'Initialized Successfully!', True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pinhead's server | p$help")) # Choose your status here
    pinbotLogs = discord.utils.get(bot.get_all_channels(), name="pinbot-logs") # Bot log channel goes here
    botVersion = ('{}'.format(ver[0]))
    botVersionReleaseDate = ('released {}'.format(ver[1]))
    await pinbotLogs.send('**-------------- ' + botName + ' ' + botVersion + ' ' + botVersionReleaseDate + ' ---------------**')
    await pinbotLogs.send('**Current Time:** ' + str(DT.datetime.now()))
    await pinbotLogs.send('**Time to start:** ' + str((DT.datetime.now() - botStartTime)))
    await pinbotLogs.send('**Done Loading!**')
    lout.log(config, botStartTime, None, None, True)

#   ____                                          _     
#  / ___|___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
# | |   / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
# | |__| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
#  \____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/

@bot.command(pass_context=True, aliases=['lag'])
async def ping(ctx):
    startTime = DT.datetime.now()
    pinbotLogs = discord.utils.get(bot.get_all_channels(), name="pinbot-logs") # Bot log channel goes here
    botLatency = bot.latency*1000
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    embed.add_field(name='Pong! Delay:', value=botLatency)
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'ping')

@bot.command(pass_context=True, aliases=['serverTime'])
async def time(ctx):
    startTime = DT.datetime.now()
    pinbotLogs = discord.utils.get(bot.get_all_channels(), name="pinbot-logs") # Bot log channel goes here
    embed = discord.Embed(
        color = discord.Color.gold()
    )
    embed.add_field(name='Server Time:', value=DT.datetime.now())
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'time')

@bot.command(pass_context=True, aliases=['runTime', 'runDuration'])
async def uptime(ctx):
    startTime = DT.datetime.now()
    runTime = startTime.replace(microsecond=0) - botStartTime.replace(microsecond=0)
    pinbotLogs = discord.utils.get(bot.get_all_channels(), name="pinbot-logs") # Bot log channel goes here
    embed = discord.Embed(
        color = discord.Color.blue()
    )
    embed.add_field(name='Uptime (hh:mm:ss):', value=runTime)
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'uptime')

@bot.command(pass_context=True, aliases=['vers'])
async def version(ctx):
    startTime = DT.datetime.now()
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.add_field(name=botName + ' {}'.format(ver[0]), value='Released {}'.format(ver[1]))
    await ctx.send(embed=embed)
    lout.log(config, startTime, 'version ({})'.format(ver[0]))

@bot.command(pass_context=True) # This is the help command, make sure you put your commands here!
async def help(ctx):
    startTime = DT.datetime.now()
    author = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name="Staff") # Your server's staff role goes here
    botVersion = ('{}'.format(ver[0]))
    botVersionReleaseDate = ('Released {}'.format(ver[1]))
    embed = discord.Embed(
        color = discord.Color.red()
    )
    embed.set_author(name='Help and Commands', icon_url='https://cdn.discordapp.com/avatars/850785536133693480/ef462c3c61506768a0e82ac07b56170b.png?size=4096')
    embed.add_field(name=botPrefix + 'ping, lag', value=botName + ' reports how long it takes to respond to a command or message.', inline=False)
    embed.add_field(name=botPrefix + 'time, serverTime', value='States what time it is on the server that the bot is hosted on', inline=False)
    embed.add_field(name=botPrefix + 'uptime, runTime, runDuration', value=botName + ' reports how long it has run without going offline.', inline=False)
    embed.add_field(name=botPrefix + 'version, vers', value='Gives the version (and its release date) being run', inline=False)
    if role in ctx.author.roles: # If user has the role you defined, show commands in the if statement, highly recommended you put staff only commands here
        embed.add_field(name=botPrefix + 'mail, sendMail, dm', value='Command used to send modmail to users. Staff only command. Command goes as follows, and yes "" is required: mail 246291288775852033 "Modmail content"', inline=False)
    embed.add_field(name=botPrefix + 'shutdown, stop, kill', value='Shuts down the bot safely and outputs it to logs.', inline=False)
    embed.set_footer(text=botName + ' ' + botVersion + ' | ' + botVersionReleaseDate + ' | Created by pinhead [' + botCreator + ']') # Your name goes in the place of pinhead
    await author.send(embed=embed)
    lout.log(config, startTime, 'help')

@bot.command(pass_context=True, aliases=['stop', 'kill'])
async def shutdown(ctx):
    if ctx.author.id == 246291288775852033: # Your user ID goes here
        botShutdownTime = DT.datetime.now()
        pinbotLogs = discord.utils.get(bot.get_all_channels(), name="pinbot-logs") # Bot log channel goes here
        await pinbotLogs.send(botName + " is shutting down...")
        lout.log(config, botShutdownTime, 'shutdown')
        exit()
    else:
        await ctx.send("Only pinhead can shut me down!") # Put your name here

# @bot.command(pass_context=True)
# async def say(ctx, *messageContent):
#     if ctx.author.id == sayPermIDs:
#          await ctx.send('{}', ' '.join(messageContent))

 # __  __           _                 _ _ 
 #|  \/  | ___   __| |_ __ ___   __ _(_) |
 #| |\/| |/ _ \ / _` | '_ ` _ \ / _` | | |
 #| |  | | (_) | (_| | | | | | | (_| | | |
 #|_|  |_|\___/ \__,_|_| |_| |_|\__,_|_|_|

@bot.listen('on_message')
async def on_message(ctx):
    startTime = DT.datetime.now()
    sender_id = str(ctx.author.id)
    modmail_channel = discord.utils.get(bot.get_all_channels(), name="pin-box") # Bot inbox/modmail receive channel goes here
    pinbotLogs = discord.utils.get(bot.get_all_channels(), name="pinbot-logs") # Bot log channel goes here
    if ctx.author == bot.user:
        return
    if str(ctx.channel.type) == "private":  
        await pinbotLogs.send("**New Modmail!**\n" + "**From:** <@" + sender_id + ">!\n" + "**Message: **" + ctx.content)
        embed = discord.Embed(
            color = discord.Color.green()
        )
        embed.add_field(name='User ID:', value=sender_id)
        await modmail_channel.send("**New Modmail!**\n" + "**From:** <@" + sender_id + ">!\n" + "**Message: **" + ctx.content, embed=embed)
        lout.logModmail(config, startTime, 'modmailRecieved', ctx.content)

@bot.command(pass_context=True, aliases=['sendMail', 'dm'])
async def mail(ctx, user: discord.User, messageContent: str = None):
    # if user != str:
    #     embed = discord.Embed(
    #         color = discord.Color.red()
    #     )
    #     embed.add_field(name='An error occured while executing the command "mail". The error is:', value='```diff - You need to give a valid user ID.\n+ Command usage: mail 246291288775852033 "Hello!"```')
    #     return await ctx.send(embed=embed)
    if messageContent is None:
        embed = discord.Embed(
            color = discord.Color.red()
        )
        embed.add_field(name='An error occured while executing the command "mail". The error is:', value='```diff\n - The message content is empty.\n + Command usage: mail 246291288775852033 "Hello!"```')
        return await ctx.send(embed=embed)
    role = discord.utils.get(ctx.guild.roles, name="Staff") # Your server's staff role goes here
    if role in ctx.author.roles:
        if str(ctx.channel) == "pinbot-commands":
            startTime = DT.datetime.now()
            pinbotLogs = discord.utils.get(bot.get_all_channels(), name="pinbot-logs") # Bot log channel goes here
            await user.send("**New Modmail from** <@" + str(ctx.author.id) + ">!\n" + messageContent)
            await pinbotLogs.send("**Modmail sent to** <@" + str(user.id) + ">.\n**Message sent:** " + messageContent)
            lout.logModmail(config, startTime, 'modmailSent', messageContent)
    else:
        embed = discord.Embed(
            color = discord.Color.red()
        )
        embed.add_field(name='An error occured while executing the command "mail". The error is:', value="```diff\n - You're not staff!```")
        return await ctx.send(embed=embed)

bot.run(lout.fetchToken(config))