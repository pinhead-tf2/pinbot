# Welcome to pinbot!

This is pinbot, the bot I use in my server to deal with modmail and more. It is easily customized so people can make their own version and run the bot if they wish. I will supply all the required things below and what specific things there are to note. 

# Installing the Requirements

For a start, I used Python 3.9.5 and VSCode 1.56.2. You are also expected to have downloaded the Discord.py libraries. A comprehensive guide to installing the first few requirements for a Discord bot is available here: https://discordpy.readthedocs.io/en/stable/intro.html#installing

All of these installations should work after you install Python and restart your computer. All that's left to do is paste these in Command Prompt.

PyYAML: 0.19.2 - pip install PyYAML

asyncio 3.4.3 - pip install asyncio

sLOUT 0.1 - (Already supplied with the bot)

# Requirement Install Locations

These paths can just be entered in the Windows Explorer bar, note that it will not work if you used anything besides Python 3.9.

Make sure all of these are placed in the right folder, typically located at %userprofile%\AppData\Local\Programs\Python\Python39\Lib\site-packages

If they are not installed there, go to %userprofile%\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages

I do not know if the package folder will be named different for each user, but as something to note, it will always be named something like PythonSoftwareFoundation.Python.

# Final Notes

Please note that this bot is not finished and is still a thing I'm working on as I learn the ropes of Python. Some things like writing logModmail to the .txt logs do not work at the moment. Please bare with me as I progress.

Credit to the ASCII headers goes to https://patorjk.com/software/taag

AND PAY ATTENTION TO THE CODE COMMENTS IN PINBOT.PY, THAT IS TELLING YOU EVERYTHING YOU NEED TO KNOW ABOUT CUSTOMIZING THE BOT FOR YOUR SERVER.
