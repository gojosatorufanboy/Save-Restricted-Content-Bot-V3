# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "28611965"))
API_HASH = getenv("API_HASH", "d36cfa9250dd3d0d46678b538836ca8b")
BOT_TOKEN = getenv("BOT_TOKEN", "7442602363:AAFnHnlOkUctvxRyEe4rNW_MjNMmlwQrnL0")
OWNER_ID = list(map(int, getenv("OWNER_ID", "772384743").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://BinaryBandiT69:BinaryBandiT69@db3.vxnexhs.mongodb.net/?retryWrites=true&w=majority&appName=DB3")
LOG_GROUP = getenv("LOG_GROUP", "-1002164324803")
CHANNEL_ID = int(getenv("CHANNEL_ID", "TBots_Father"))

