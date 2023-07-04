handles the game info for display purposes
	
Columns:
- id | int(32) | not null, primary key | store appid
- name of game | text | not null 
- series | text | not null | has to be *manually* added because steam api never exposes franchise data
- icon_url | text | not null 

icon url is used in the following url:
http://media.steampowered.com/steamcommunity/public/images/apps/APPID/IMG_ICON_URL.jpg