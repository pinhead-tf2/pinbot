# Games list
Pull games list using 
http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=KEY&steamid=STEAMID64&format=json&include_played_free_games=1&include_appinfo=1
Add appid, name, iconurl

Get game playtime by using the same api with different args
Potentially broken?
http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=KEY&steamid=STEAMID64&format=json&include_played_free_games=1&include_appinfo=1&appids_filter=%7B440%7D


# Achievements

Get achievement info
http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=#######&key=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX&steamid=76561198818675138
iterate through app achievements list, adding achieved to a counter (it is binary 0-1), getting all achievements is as easy as list length