# BDOBot
This project is a Discord Bot written in Python for the online MMORPG Black Desert Online.
The bot is my first Discord bot and my first side project that I have decided to take up in order to create some convenience.

## Features
- The bot is able to retrieve cooking/crafting materials of a certain craft product/food that exists in the game. For example, The command '%beer' returns the ingredients required for a 'Beer' food in the game, whereas '%5 beer' returns the count for 5 of the food item.
- The bot has a function that calculates the profit made from selling an item in the game's Central Marketplace, with or without an additional tax exemption from 'Value Pack'
- The bot is built with a 'World Boss' feature to respond to users querying about the next upcoming World Boss, as well as the ability to give a Discord role to users that wants to be reminded(mentioned) 30 minutes before a boss spawns

## Usage
- Clone the repository and change the server_id to your Discord Server ID and run main.py (Optionally you could rename my BDOBot instance, and remove the auto-reply to send a .gif)
- The bot is prefixed with the symbol '%'
- Any command that exist within '%help' or any valid cook/craft item will retrieve the list of raw materials required
- The bot is currently hardcoded to work in my guild's Discord Guild.

## Contributing
- Pull requests are welcomed, as well as suggestions or code critic or reviews. This bot is still in the development phase and will be for a while as it is a side project.
- Some of the code are working but not the most efficient or elegant, any pull request for cleaner code is always appreciated.
