# LOGGING
COG_STARTUP = "starting up %s Cog"
ON_MEMBER_JOIN = "%s has joined, sleeping for 25 seconds before sending welcome"
ON_MEMBER_REMOVE = "%s has left or have been removed from the server"
BOT_STARTUP = "starting up bot with ID: %s, Name: %s"
RECRUIT_TRIGGER = "Recruitment: %s triggered by %s"
KHAN_TRIGGER = "Khan: %s triggered by %s"
WAR_TRIGGER = "Node War: %s triggered by %s"
REACTION_CHOSEN = "reaction chosen: %s"
REACT_TIMEOUT = "%s reaction timeout hit, removing message"
LOGGING_STREAM_FORMAT = '[LOG] [%(asctime)s] [%(levelname)s] [%(funcName)s:%(lineno)s] : %(message)s'
EXT_FAILED_TO_RUN = "an extension failed to run - {0}: {1}"
SCHEDULER_STARTUP = "starting up %s scheduler"
NEXT_ANNC = "next %s announcement set at %s"
SENT_ANNC = "sent %s announcement at %s"
UPCOMING_ANNC = "upcoming %s announced happening at %s"
INACTIVE_ANNOUNCER = "%s announcement INACTIVE, no message sent"
FUN_QUERY_SENT = "%s name passed in: %s"
FUN_QUERY_ERR = "unable to retrieve %s name: %s"
BOSS_NOTIFICATION_SENT = "sending boss notification for %s"
RETRIEVE_PRAW_CONFIG = "retrieving PRAW ID and secret"
ENV_VAR_NOT_FOUND = "%s env var not found, attempting to read %s"
FILE_NOT_FOUND = "%s not found"
RETRIEVE_DISCORD_CONFIG = "retrieving Discord token"
CONFIG_FILE_RETRIEVE_SUCCESS = "%s params retrieved from %s"
NEXT_ROLE_UPDATE_TIME = "next roles update time set at %s"
ROLE_UPDATED_TIME = "roles updated at %s"
NO_ROLE_UPDATED = "no %s role updated today"
ROLE_UPDATED = "Following %s have %s role %s in their roles: [%s]"
ADD_REACTION_FOR_MSG = 'message passed and reaction type %s added'

# NUMBER / FORMATS
ZERO = 0
ONE = 1
TWO = 2
TEN = 10
EIGHTEEN = 18
TWENTY_ONE = 21
SIXTEEN = 16
DT_FORMAT_ANNC = '%d/%m/%Y, %H:%M:%S'
DT_FORMAT_INVITE = 'dddd DD MMM YYYY hh:mm A'
DT_FORMAT_WB = '%H:%M'
DT_FORMAT_SNIPE = 'DD-MM-YYYY'

#COMMANDS
HELP_L = 'help'
BUG_L = 'bug'
HYSTRIA_L = 'hystria'
SYCRAIA_L = 'sycraia'
CALC_L = 'calc'
RECRUIT_L = 'recruit'
HELLO_L = 'hello'
NEZUKO_L = 'nezuko'
KHAN_L = "khan"
TWITCHTV_L = 'twitch.tv'
WAR_L = "war"
MEME_L = "meme"
ANIME_L = "anime"
MANGA_L = "manga"
POPCORN_L = "popcorn"
MARKETPLACE_L = "mp"
WB_L = "wb"
BOSSHUNTER_L = "bosshunter"
DOUGHTART_L = "doughtart"
HALP_L = 'halp'
UWU_L = 'uwu'
SNIPE_L = "snipe"
DUTY_L = "duty"

# STRING
PASTRIES = "Pastries"
NEW_LINE = '\n'
RECRUIT = "Recruit"
KHAN = "Khan"
NODE_WAR = "Node War"
KHAN_ANNC = "Khan announcement"
WAR_ANNC = "War announcement"
STATUS = "STATUS"
OPEN = "OPEN"
CLOSE = "CLOSE"
ACTIVE = "ACTIVE"
INACTIVE = "INACTIVE"
STATUS_MSG_USE_HELP = "use %help"
NEZUKO_BOT = "NezukoBot"
ANIME = "Anime"
MANGA = "Manga"
CARAMEL_POPCORN = "Caramel Popcorn"
GENERAL = "General"
ANNOUNCEMENT = "Announcement"
FUN = "Fun"
MARKET = "Market"
BOSS = "Boss"
BOSS_HUNTER = "Boss Hunter"
PRAW_CLIENT_ID = "PRAW_CLIENT_ID"
PRAW_CLIENT_SECRET = "PRAW_CLIENT_SECRET"
DISCORD_TOKEN = "DISCORD_TOKEN"
DISCORD_TOKEN_FILE = "token.txt"
PRAW_SECRET_FILE = "praw_secrets.txt"
FILE_READ_MODE = 'r'
ROLE_UPDATE = "role update"
CROISSANT = "Croissant"
MACARON = "Macaron"
EGGTART = "Eggtart"
GUILD_MEMBER = "Guild Member"
ADDED = "added"
REMOVED = "removed"
DOUGHTART = "DO-ugh-TArt"
KHAN_CAPS = 'KHAN'
WAR_CAPS = 'WAR'
UPDATE = 'UPDATE'
YES_NO = 'YES_NO'
SNIPE_SCHEDULE_FILE = "snipe_schedule_file.csv"
SNIPE_REMINDER = "Snipe Reminder"

# CONFIGS
STATUS_LOOP_TIME_SECONDS = 20
REACTION_TIMEOUT_SECONDS = 7
PREFIX_PERCENT = "%"
MEME_SUBREDDITS = ['memes', 'animemes', 'meme', 'goodanimemes']
UWU_SUBREDDITS = ['goldenretrievers']
BOSS_NOTIFICATION_NOTICE_SECONDS = 1800

MODULES_GENERAL = 'Modules.General'
MODULES_MARKET = 'Modules.Market'
MODULES_BOSS = 'Modules.Boss'
MODULES_FUN = 'Modules.Fun'
MODULES_ANNOUNCE = 'Modules.Announcement'
STARTUP_COG_MODULES = [MODULES_GENERAL, MODULES_MARKET, MODULES_BOSS, MODULES_FUN, MODULES_ANNOUNCE]

# ANIME/MANGA
MSG_FUN_RESPONSE = '```{0}```\n```{1}```\n{2}'
MSG_FUN_ERR = "An error occured while retrieving {0} {1} :("

# BOSS
MSG_NEXT_BOSS_ANNC = "```diff\n- The next boss is {0} at {1} hrs, GMT+8```"
MSG_NEXT_BOSS_REMINDER = "{0} \n```md\n {1} will spawn in 30 minutes time!```"

# CALC
MSG_CALC_FAIL = "```Sorry, I didn\'t get that, please use +, -, *, /, % only!```"
MSG_CALC_RES = "```{0} is {1}```"

# GENERAL
MSG_BUG_DISCOVERED = "<@!{}> A bug have been discovered!"
MSG_COMD_DENIED = "```Only Crème brûlées are allowed to use this feature!```"
MSG_HELLO_MENTION = "Hello {0.mention}!"
MSG_HELP_MSG = "```yaml\n" \
          "List of Commands\n----------------\n\n" \
          "%help - shows this message\n\n" \
          "%halp - shows this message\n\n" \
          "%foodname - retrieves ingredients i.e. %5 beer\n\n" \
          "%wb - shows the upcoming world boss\n\n" \
          "%bosshunter - (un)register the Boss Hunter role." \
          "Receive notifications 30 minutes before world boss!\n\n" \
          "%popcorn - (un)register the Caramel Popcorn role.\n\n" \
          "%doughtart - (un)register the DOugh-TArt role.\n\n" \
          "%mp - shows profit with(out) VP from selling in MP i.e. %mp 43500000\n\n" \
          "%hystria - sends a map of hystria!\n\n" \
          "%meme - sends a random meme\n\n" \
          "%uwu - sends a golden retriever doggo\n\n" \
          "%calc - built-in calculator, supports +, -, *, /, %\n\n" \
          "%anime <title> - retrieves anime information from MyAnimeList\n\n" \
          "%manga <title> - retrieves manga information from MyAnimeList\n\n" \
          "%recruit - Update recruitment status (Crème brûlées only!)\n\n" \
          "%khan - Update Khan announcement status (Crème brûlées only!)\n\n" \
          "%war - Update Node War announcement status (Crème brûlées only!)\n\n" \
          "%snipe - Upload a .csv file for daily node war snipe reminder (Crème brûlées only!)\n\n" \
          "%bug <message> - reports a bug to Kagi\n\n```"
MSG_INVALID_COMD = "No results or commands was retrieved." \
        "\nPerhaps you wanna use '%help'?"
MSG_ON_MEMBER_REMOVE = "```{0} has left or have been removed from the server```"
MSG_TWITCH_WARNING = "Hello {0.mention}, it seems like you have pasted a Twitch link. All videos or stream advertisements goes to {1.mention}, thank you!"
MSG_ROLE_REGISTER = "{0.author.mention} is now registered as a {1}!"
MSG_ROLE_RESIGN = "{0.author.mention} have resigned as a {1}!"
MSG_ROLE_UPDATE = "Following `{0}` have `{1}` {2} in their roles: \n```{3}```"

# MARKETPLACE
MSG_MP_RESULT = "Without VP: {0} \nWith VP: {1}\nValues might be a little off depending on your family fame!"

# KHAN
MSG_KHAN_ENQUIRY = 'Please react to enquire or update Khan announcement status!\n\n' \
                ':bread: - Khan Announcement Status\n\n:o: - Activate Khan Announcement \n\n:x: - Deactivate Khan Announcement'
MSG_KHAN_OPEN_UPDATE = "{0.mention} ```Updated Khan Announcement status to active!```"
MSG_KHAN_CLOSE_UPDATE = "{0.mention} ```Updated Khan Announcement status to inactive!```"
MSG_KHAN_STATUS = "```Khan Announcement Status: {0}```"

MSG_KHAN_INVITE = ':whale:**HI BREADS! LET\'S DO KHAN RAID TOMOROWWW!!:whale:\n\n' \
':calendar_spiral:Mark your calendar!**\n' \
'`{0} GMT+8`\n\n' \
':pretzel:Server will be announced in guild chat 1 hour before the raid starts!\n' \
':pretzel:Please bring your PVP-safe character (Lv49 or less) to avoid grifers!\n' \
':pretzel:CTG to OE, and taxi back to mainland will be provided\n' \
':pretzel:We will be doing XL (Tier 3)! Let us know if you have friends interested to come to WH!\n\n' \
'> *New to Khan Raid? Just come and join uss! We fully support every breads who wanna try new experiences! <:yay:707879651804053565>\n' \
'> No gear req needed as you\'ll shoot em fish with cannon! >:D*\n' \
'> Check this Video Guide to learn about Cannon Rotation so you can deal damage to the big fish more efficiently!\n' \
'> https://www.youtube.com/watch?v=h1jY7r6bGQk\n' \
'> Or kindly poke {1.mention} for your Khan related questions!\n\n' \
'**Confirm your attendance**\n' \
'> by reacting :regional_indicator_y: if you\'re going to attend, or :regional_indicator_n: if you\'re not!\n' \
'*Don\'t miss out seeing El getting Khan\'s Heart! See you this Saturday, breados!*<:yay:707879651804053565>'
#'<@&574641817505497106> <@&635776028048097290> <@&574641855229067264>'

# RECRUIT
MSG_REC_CLOSED_MSG = ":pretzel:**Welcome to Pastries!**:pretzel:\n\n' \
                'Hello {0.mention}, Thank you for visiting our discord!\n' \
                'We\'d really love to have you joining our little bakery.\nBut unfortunately, ' \
                ':no_entry_sign:**our recruitment is CLOSED**:no_entry_sign: for the time being!\n' \
                'Hopefully we\'d meet again in the next chance!\n\nIf you have any questions ' \
                'feel free to mention Crème brûlée!\n' \
                '*While you\'re here, please have some free cheese garlic bread* :sparkles:\n"
MSG_RECRUIT_ENQUIRY = "Please react to enquire or update recruitment status!\n\n" \
    ":bread: - Recruitment Status\n\n:o: - Opening of recruitment \n\n:x: - Closing of recruitment"
MSG_RECRUIT_OPEN_UPDATE = "{0.mention} ```Updated recruitment status to open!```"
MSG_RECRUIT_CLOSE_UPDATE = "{0.mention} ```Updated recruitment status to closed!```"
MSG_RECRUIT_STATUS = "```Recruitment Status: {0}```"

MSG_REC_OPEN_MSG =':sparkles::pretzel:**Hello fresh dough {0.mention}, welcome to Pastries!**:sparkles::pretzel:\n' \
               'We would like you to answer the following short questions before proceeding!\n\n' \
               '> **01. What\'s your in-game Family Name? Where did you find our guild from?** *i.e. from server-chat advertisement, recommendation from a friend (please identify), Guild Rank Board, BDO SEA community forum, etc*\n\n' \
               '> **02. What are you looking for in a guild?** *i.e. Payouts, socializing, guidance in game*\n\n' \
               '> **03. Have you been in a guild before?** *If YES, what guild and why did you leave?*\n\n' \
               '> **04. What kind of player do you consider yourself as?** *PVE, PVP, Lifeskill-oriented, or an all-rounded?*\n\n' \
               '> **05. OPTIONAL - Where are you from? What timezone do you live in?** *We got people from MY/SG/INA/PH and a few more other countries inside!*\n\n' \
               ':cake:By answering these questions, you also acknowledge that Pastries is a **chill International PVX/Lifeskill guild**\n' \
               ':cake:**We do not tolerate any form of unhealthy or immature behaviours when you are with us!**\n' \
               ':cake:Please head over to {1.mention} for more info and our guild rules!\n\n' \
               '**Thank you for answering the questions - Please mention @/[Officer] Crème brûlée or @/[Officer]Brioche Bun when you are done**\n' \
               '*We look forward to get to know you better!*\n\n'

# NODE WAR
MSG_WAR_ENQUIRY = 'Please react to enquire or update NW announcement status!\n\n' \
                ':bread: - NW Announcement Status\n\n:o: - Activate NW Announcement \n\n:x: - Deactivate NW Announcement'
MSG_WAR_OPEN_UPDATE = "{0.mention} ```Updated War Announcement status to active!```"
MSG_WAR_CLOSE_UPDATE = "{0.mention} ```Updated War Announcement status to inactive!```"
MSG_WAR_STATUS = "```War Announcement Status: {0}```"
MSG_NO_ATTACHMENTS = "```No attachments found in message, please send .csv with valid format!```"

MSG_WAR_INVITE = ':crossed_swords:**PREPARE YOUR KNAIFU WE GOT SOME BUTTER TO SPREAD!:crossed_swords:\n\n' \
':calendar_spiral:Mark your calendar!**\n' \
'`{0} GMT+8`\n\n' \
':pretzel:We will be participating in **Tier 1** Node War! Server will be announced 1 hour before Node War starts!\n' \
':pretzel:We have up to 55 slots for everyone to join in. **No minimum gearscore required**, EVERYONE is invited to join in the fun, the more the merrier!\n' \
':pretzel:Shotcalls will be on Discord so joining in voice chat is mandatory! <:kagi_proudmum:830388637073145907>\n\n' \
'> *New to Node War? Just come and join us! We fully support every breads who wanna try new experiences!* \n' \
'> While knowing how to PVP is crucial, there are so much more into NW if you prefer the \'less-agressive\' way to contribute, i.e. Carrack-captain, Elephant-rider + Spear-thrower, Flame Tower pilot, Cannoneer, Hwacha pilot, etc!' \
'> Kindly poke any of our officers if you\'re interested or have any questions in any of these stuff!\n' \
'> Alternatively, Node War guides and discussions are on {1.mention}\n\n' \
'> Please post/update your character gear info in {2.mention} to help us in making team compositions easier!\n' \
'> More details about the node we will be fighting in and platoon composition will be posted here on war day!\n\n' \
'**CONFIRM YOUR ATTENDANCE**\n' \
'> by reacting :regional_indicator_y: if you\'re going to attend, or :regional_indicator_n: if you\'re not!\n' \
'*With consideration of participant caps, members with :regional_indicator_y: reacted in this post will be guaranteed a slot*\n' 
'<@&574641817505497106> <@&635776028048097290> <@&574641855229067264>'

# ASSETS
ASSET_POSTER = "assets/poster.png"
ASSET_REC_CLOSE = "assets/garlic_bread.png"
ASSET_HYSTRIA = "assets/hystria.png"
ASSET_SYCRAIA = "assets/sycraia.png"
ASSET_NEZUKO = "assets/nezuko.gif"
ASSET_KHAN_ANNC = "assets/KHAN_ANN.png"
ASSET_NW_ANNC = "assets/NW_ANN.png"

# REACTION / EMOJI
EMOJI_STATUS = "\U0001f35e"
EMOJI_OPEN = "\U00002b55"
EMOJI_CLOSE = "\U0000274c"
EMOJI_Y = "\U0001F1FE"
EMOJI_N = '\U0001F1F3'
REACTION_ADD = 'reaction_add'

# ID
ID_CHN_ABOUT_US = 575282309947850822
ID_CHN_ENTRY = 574641679575941137
ID_CHN_BAKERY = 574641537548550156
ID_CHN_MEDIA = 587559616188121108
ID_CHN_BOT_CHN = 574646616489721887
ID_CHN_MENU_BOARD =574650178183626771
ID_CHN_ACTIV_DISCUSS = 645931876107943967
ID_CHN_GEAR_CLASS = 801731373147881515
ID_CHN_KAGI_PLAYGROUND = 871250117120909362
ID_ROLE_BOSSHUNTER = 623100796833234955
ID_ROLE_BRIOCHE = 635776028048097290
ID_ROLE_CREME = 574641817505497106
ID_ROLE_CROISSANT = 574641855229067264
ID_ROLE_EGGTART = 659629130375102465
ID_ROLE_MACARON = 575188744617852939
ID_ROLE_POPCORN = 707958341539856404
ID_ROLE_GMEMBER = 801718825128034335
ID_ROLE_OFFICER = 801808081398792203
ID_ROLE_GM = 574802564596367361
ID_USER_EL = 193314826779361281
ID_USER_KAGI = 382152478810046464
ID_SERVER_PASTRIES = 574641536214630401
