import json
import os

from aiohttp import ClientSession
import aiosqlite
from time import time
from asyncio import get_event_loop


#                         To be replaced with bot: discord.Bot, it supplies client and key
async def get_owned_games(session: ClientSession):
        # ?key=KEY&steamid=STEAMID64&format=json&include_played_free_games=1&include_appinfo=1
    async with session.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/',
                           params={
                               # "key": self.bot.steamworks.key
                               "key": "566BC004D45237E894F20581D625B460",
                               "steamid":


                           }) as response:

    return


loop = get_event_loop()
loop.run_until_complete(get_owned_games(ClientSession()))
