# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
🤖 **Bot** : File Store Bot

👲 **Developer** : [ᴍʜᴅ ᴍᴜꜰᴀz](https://telegram.me/Mufaz123)

📣 **Channel** : @BX_Botz

👥 **Group** : [ʙx sᴜᴘᴘᴏʀᴛ](https://t.me/BxSupport)

💻 **Source** : [Click here](https://t.me/nokiyirunnoippokitum)

🎧 **Language** : [Python3](https://python.org/)

📚 **Library** : [Pyrogram v1.2.0](https://pyrogram.org/)

🧑‍💻 **Server** : [Heroku](https://heroku.com/)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:[ᴍʜᴅ ᴍᴜꜰᴀᴢ](https://t.me/mufaz123)
"""
	HOME_TEXT = """
Hai, [{}](tg://user?id={})

`Iam a Simple File Store Bot.
Send me any file I will give you permenent sharable link`

👲 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : [ʙx ʙᴏᴛᴢ](https://t.me/BX_Botz)
"""
         HELP_TEXT = f"""
Join My Update Channel @BX_Botz
"""
