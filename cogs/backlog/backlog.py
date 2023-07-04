import aiosqlite
import discord.ext.commands
from discord import option
from discord.ext import commands
from discord.commands import SlashCommandGroup
from api.steam.steam_applist_handler import find_game_by_appid


class Backlog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    backlog = SlashCommandGroup("backlog", "Commands related to the game backlog")

    @backlog.command(name="register",
                     description="Manually register a game in the game info database. Avoid using, is missing some data points.")
    @option("appid", description="The Steam AppID of the game to register")
    @option("series", description="The series the game belongs to. Not required.",
            required=False,
            default=None)
    @commands.is_owner()
    async def register(self, ctx,
                       appid: int,
                       series: str):
        # call GetPlayerAchievements to get the amount of achievements
        # this only works on owned games, for everything else use ISteamApps/GetAppList
        # GetAppList doesn't return app icons though so that sucks
        name = await find_game_by_appid(appid)  # FUCK STEAM SERIOUSLY THIS TOOK HOURS
        if not name:
            return await ctx.respond(f"AppID `{appid}` cannot be found in app list, "
                                     f"ensure you have the correct AppID or update the cached app database.",
                                     ephemeral=True)

        async with aiosqlite.connect("backlog_database.sqlite") as db:
            try:
                await db.execute("INSERT INTO game_info (id, name, series) "
                                 "VALUES (?, ?, ?)",
                                 (appid, name, series))
                await db.commit()
                await ctx.respond(f"*{name}* successfully registered in game info database.")
            except aiosqlite.IntegrityError:
                return await ctx.respond(f'**Error:** *{name}* already exists in database.', ephemeral=True)

    @backlog.command(name="deregister", description="Removes a game from all databases.")
    @option("appid", description="The Steam AppID of the game to deregister")
    @commands.is_owner()
    async def deregister(self, ctx,
                         appid: int):
        async with aiosqlite.connect("backlog_database.sqlite") as db:
            try:
                await db.execute(f"DELETE FROM game_info WHERE id={appid}")
                await db.commit()
                assert db.total_changes > 0
                await ctx.respond(f"AppID `{appid}` removed from all databases.")
            except AssertionError:
                return await ctx.respond(f"**Error:** AppID `{appid}` not found in game info database.", ephemeral=True)

    @backlog.command(name="importall", description="Imports all your owned Steam apps into the backlog.")
    @commands.is_owner()
    async def importall(self, ctx):
        await ctx.respond(f"Not Implemented", ephemeral=True)


def setup(bot):
    bot.add_cog(Backlog(bot))
