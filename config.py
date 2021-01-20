# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 2683038
API_HASH = "d154a57a4927403a628a39267aec1fef"

# Get this from @Botfather
TOKEN = "1598780599:AAETr651Lkqgc_V82bHS6BhM1D_aDxicYdE"

# Your mongodb uri
MONGO_DB_URI = "mongodb+srv://sixteenbit:7jwh6a3oafsq6b32@vc.uwxyv.mongodb.net/vc?retryWrites=true&w=majority"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    383407735,
    1477263666,
    1191438732
]

# The ID of the group where your bot streams
GROUP = -1001331840504

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = True

# Send "now playing" messages to the group
LOG = True

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# No need to touch the following.
LOG_GROUP = GROUP if LOG else None
SUDO_FILTER = filters.user(SUDO_USERS)
