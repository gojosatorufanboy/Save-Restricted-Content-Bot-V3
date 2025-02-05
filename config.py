# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "9976721"))
API_HASH = getenv("API_HASH", "3ef17a8cdb938335bd8ba292e6d816aa")
BOT_TOKEN = getenv("BOT_TOKEN", "7391468728:AAGysMmgglpE4SuHXSK3R0KXUDgBldvd1E0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7172796863").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://userbot:djgftfyyfty@cluster0.7yorw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002151484823")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002151484823"))

