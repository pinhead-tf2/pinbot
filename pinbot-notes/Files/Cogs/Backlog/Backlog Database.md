handles the game backlog

Columns:
- id | int(32) | not null, primary key, foreign key referencing game info db
- date_updated | integer(6) | not null default (strftime(%s, now))
- goal | text | check (goal in (100%, main + extra, main))
- status | text | check (status in (complete, playing, paused, unplayed, ignored, abandoned, wishlist)), not null, default unplayed
- date_completed | integer(6) 
- comments | text 
- isfavorite | integer(1) | check (isfavorite in (0, 1)) not null, default 0

