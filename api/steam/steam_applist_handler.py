import json
import os
from os import remove, stat

import aiosqlite
from time import time
from aiohttp import ClientSession


async def cache_game_list():
    async with ClientSession() as session:
        async with session.get('http://api.steampowered.com/ISteamApps/GetAppList/v2') as response:
            print("Status:", response.status)
            payload = await response.json()
            with open('api/steam/steamapplist.json', 'w') as file:
                json.dump(payload, file)

    await load_applist_into_db()


async def create_database():
    async with aiosqlite.connect("api/steam/steam_applist.sqlite") as db:
        await db.execute('''
                    CREATE TABLE IF NOT EXISTS app_data
                    (
                        appid INTEGER not null
                            primary key,
                        name  TEXT
                    )
                ''')
        await db.commit()


async def load_applist_into_db():
    start_time = time()
    counter = 0
    print("Started")

    with open("api/steam/steamapplist.json") as file:
        payload = json.load(file)
        apps = payload["applist"]["apps"]
        print(f"All data loaded and set up after {round(time() - start_time, 4)} seconds")

        async with aiosqlite.connect("api/steam/steam_applist.sqlite") as db:
            for entry in apps:
                # this is horribly inefficient but i quite honestly don't care
                # PLEASE gaben, make a better api
                await db.execute("INSERT OR IGNORE INTO app_data(appid, name) "
                                 "VALUES (?, ?)",
                                 (entry['appid'], entry['name']))

                counter += 1
                if counter % 100 == 0:
                    await db.commit()
                    
    os.remove("api/steam/steamapplist.json")
    db_size = stat("api/steam/steam_applist.sqlite").st_size / (1024 * 1024)
    print(f"Finished after {round(time() - start_time, 4)} seconds\n"
          f"End size of db: {counter} entries ({db_size} MB)")


async def find_game_by_appid(app_id: int):
    async with aiosqlite.connect("api/steam/steam_applist.sqlite") as db:
        async with db.execute(f"SELECT name FROM app_data WHERE appid = {app_id}") as cursor:
            result = await cursor.fetchone()  # steam and the db prevent multiples
            return result[0]

# loop = asyncio.get_event_loop()
# loop.run_until_complete(find_game_by_appid(1235140))
