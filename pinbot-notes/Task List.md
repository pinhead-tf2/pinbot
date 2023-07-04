## bot.py
- [/] Finish status changing

## Backlog
- [d] Add Steam library synchronization
	- [d] Complete Steam Web API request
	- [B] Create iterator to loop through and gather all needed data for `backlog` database
		- [!] Make call to `steam_applist` to get proper game name for registration in `game_info` database
	- [ ] Plug data values into `backlog` where possible

- [ ] Add achievement tracking for owned games (only happens when viewing one game, or a collection of games)
	- [ ] Create Steam Web API request to get all of a game's achievements
	- [ ] Create iterator to get the amount of completed achievements, compared to length of achievement list
	- [ ] Add achievement amount to `game_info`
	- [ ] Add earned achievements to `personal_data` database

## [[Image, please!]]
- [ ] todo: write this todo list