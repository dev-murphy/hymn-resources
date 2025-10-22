# Hymn Resource

## Breakdown

There are three folders, namely, `resources`, `mp3`, `srt`. Each of these folder serve a special purpose which we will be going into more information below.

### mp3 - Music folder

This folder contains all audio files for most if not all the hymns in the Seventh-Day Adventist hymns.

### resources - Other folder

This folder contails miscallenious files such as the json file with all the hymn data. It also contains [create-db.sql](./resources/create-db.sql) which is generated SQL file use to create a sqlite database, in this case, [hymns.db](./resources/hymns.db).

**Please Note**: How it works, it is that I would the `convert.py` to create the SQL file from the json file. Then, with the newly created SQL file, we would do to a SQL to SQLite website. This [link](https://www.rebasedata.com/convert-sql-to-sqlite-online) is an example.

## srt - Text files

This folder contains all SRT file... but it kinda serves no purpose.