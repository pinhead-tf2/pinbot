import aiosqlite


async def create_database():
    async with aiosqlite.connect("backlog_database.sqlite") as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS game_info
            (
                id                INTEGER not null
                    primary key,
                name              TEXT    not null,
                series            TEXT,
                icon_url          TEXT,
                achievement_count INTEGER
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS backlog
            (
                id                    INTEGER                          not null
                    primary key
                    references game_info
                    ON DELETE CASCADE,
                date_updated          INTEGER(8) default (unixepoch()) not null,
                goal                  TEXT       default 'main',
                status                TEXT       default 'unplayed',
                date_completed        INTEGER(8),
                comments              TEXT,
                is_favorite           INTEGER(1) default 0             not null,
                check (goal IN ('fullyComplete', 'mainWithExtras', 'main')),
                check (is_favorite in (0, 1)),
                check (status IN ('complete', 'playing', 'paused', 'unplayed', 'ignored', 'abandoned', 'wishlist'))
            )
        ''')
        await db.execute('''
            CREATE TABLE IF NOT EXISTS personal_data
            (
                id                    INTEGER not null
                    primary key
                    references game_info
                    ON DELETE CASCADE,
                playtime              INTEGER,
                last_played           INTEGER,
                unlocked_achievements INTEGER
            )
        ''')
        await db.commit()
