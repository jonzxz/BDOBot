# BDOBot
This project is a Discord Bot written in Python for the online MMORPG Black Desert Online.
The bot is my first Discord bot and my first side project that I have decided to take up in order to create some convenience.

## Features
- This bot provides multiple features that may aid in the gameplay or additional fun features
- Gameplay related features: 
    - `%foodname`: retrieves ingredients for cooking / alchemy (i.e. %5 beer)
    - `%wb`: shows upcoming world boss and time
    - `%bosshunter`: register or unregister for a 'Boss Hunter' role to be notified of boss spawns
    - `%mp`: calculates profits for marketplace sales
    - `%hystria`: sends a map of Hystria dungeon
    - `%sycraia`: sends a map of Sycraia underwater dungeon
- Non gameplay related features:
    - `%popcorn`: register or unregister for a 'Caramel Popcorn' role to be notified when there's a movie stream in the guild
    - `%anime`: uses mal API to retrieve anime information from MyAnimeList
    - `%manga`: uses mal API to retrieve manga information from MyAnimeList
    - `%calc`: calculator
    - `%meme`: uses praw API to retrieve random memes from selected subreddits
- Additional features:
    - `%recruit`: updates recruitment status to determine newcomer message
    - Automatic message for when a new user joins, sending welcome and Q&A or recruitment closed message depending on %recruit status
    - `%khan`: updates Khan announcement status
    - Automatic Khan raid announcement for next upcoming Khan raid
    - `%war`: updates Node War announcement status
    - Automatic Node War announcement for next upcoming node war

## Future implementation
- Implementation of dockerized noSQL database to store configuration values


## Contribution
- Pull requests are welcomed, as well as suggestions or code critic or reviews. This bot is still in the development phase and will be for a while as it is a side project.
- Some of the code are working but not the most efficient or elegant, any pull request for cleaner code is always appreciated.
