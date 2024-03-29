# Changelog

## 4 Nov 2021
- Removed ping and reactions on node war announcement message
- Added handling for %intro if user is unable to be fetched to send a generic message instead

## 21 Oct 2021
- Updated war announcement message to be 3 times a week, added new logic to retrieve date
- Removed snipe reminders

## 9 Sep 2021
- Removed use of secrets.txt and praw_secrets.txt, secrets now grabbed from .env
- Added Development Cog for new features to be developed in there
- Added development mode in Constants.py to toggle between production and development mode (dev mode disables all other modules live)

## 6 Sep 2021
- Fixed missing positional arguments if no snipe duty for the day

## 2 Sep 2021
- Fixed closed recruitment message line breaks
- Updated %snipe to send schedule if no .csv file is submitted

## 1 Sep 2021
- Fixed a bug where logging error causes snipe reminder to fail
- Fixed missing line in war announcement

## 31 Aug 2021
- Fixed missing Constants causing closed recruitment message to not send
- Added %intro feature to resend questionnaire
- Condensed all role giving features (%bh, %popcorn, %doughtart) into a single %role menu

## 30 Aug 2021
- Added check for if snipe duty officer exist to prevent null

## 26 Aug 2021
- Updated Welcome, Khan, Node War messages 

## 24 Aug 2021
- Added %halp as a %help alternative (@/Laviz request)
- Added %uwu to send random golden retriever pics (let me know if you have more subreddit for cute animals)
- Added %snipe to receive a valid .csv file of [DD-MM-YYYY,Name,Discord_ID,NotificationPreference,Day] format from discord uploads
- Added %duty to show officer on node war snipe duty for the day
- Added auto reminder to ping duty officer at 1730hrs GMT+8 in bot-channel

## 1 Aug 2021
- Added %doughtart to register/unregister dota role
- Added scheduled task daily to update 'Guild Member' roles for Croissant/Macaron/Eggtart

## 19 Jul 2021
- fixed error in %mp not showing correct profit values

## 16 Jul 2021
- fixed %meme with asyncpraw
- migrated bot to amazon AWS EC2 (again, finally)
- fixed a bug where khan / war announcement will be set to next announcement date if bot is restarted on announcement day, even if announcement has yet to be sent

## 9 Jul 2021
- added automated Khan and node war announcements
- added %khan and %war for officers to toggle announcement status
- updated welcome message to have poster on top and link to #about-us properly

## 16 May 2021
- added %sycraia
- default recruitment status to open

## 15 Apr 2021
- Updated sad message when recruitment is closed
- Added %recruit for officers to update guild recruitment status. if recruitment is closed bot will send a sad message instead of the whalecome message

## 14 Apr 2021
- Added %manga and %popcorn information in %help
- Added %popcorn to (un)register yourself to be part of the movie gang
- Added an error message to be sent when retrieving anime or manga results in an error

## 9 Apr 2021
- Increased delay for welcome message to 25 seconds
- Redid %anime
- Added %manga
- Backend cleanup

## 11 Jan 2020
- BETA: added %anime feature to search for anime and returns a synopsis and an image

---- Lost in time ----

## 12 Jan 2019
added %calc - calculator function 
