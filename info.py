import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '27335730'))
API_HASH = environ.get('API_HASH', 'ae5a5f660ffdf3e08997d493c32932f5')
BOT_TOKEN = environ.get('BOT_TOKEN', '6110043034:AAEi_w1qbyaXEbNVJIaGpkyTsk8h_58Bz6I')
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://te.legra.ph/file/9b5025f328c4c09a55e70.jpg https://te.legra.ph/file/74198e2f82e1eb11fc8f1.jpg https://te.legra.ph/file/bb6b80f0320164d1886a2.jpg https://te.legra.ph/file/ca639cf01449180c9a9b8.jpg https://te.legra.ph/file/35ffb77757c87ffcb60ae.jpg https://te.legra.ph/file/5fd2aa764307225847b65.jpg https://te.legra.ph/file/bbb903aa6b25622d69b29.jpg https://te.legra.ph/file/ef1a2064429c78700ea12.jpg https://te.legra.ph/file/02328095431092b233831.jpg https://te.legra.ph/file/e629eaad65bd2a88e078c.jpg https://te.legra.ph/file/7d7bc5d91da4676849680.jpg https://te.legra.ph/file/9c966e9d690e59da82b8f.jpg https://te.legra.ph/file/6f1c8418d2ce0663a92ff.jpg https://te.legra.ph/file/409a17e6f1b5fbc0310e1.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1735392935').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001676598701').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Anantharamu:Anantharamu@cluster0.z6pztvq.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Anantharamu")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL','-1001661350712'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'AR Films_Support')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '𒆜𝐀𝐑 𝐅𝐢𝐥𝐦𝐬࿐')
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>𝗤𝘂𝗲𝗿𝘆: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 𝗧𝗶𝘁𝗹𝗲: <a href={url}>{title}</a>\n🎭 𝗚𝗲𝗻𝗿𝗲𝘀🤩: {genres}\n📆 𝗬𝗲𝗮𝗿: <a href={url}/releaseinfo>{year}</a>\n🌟 𝗥𝗮𝘁𝗶𝗻𝗴: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

UPSTREAM_REPO = environ.get('UPSTREAM_REPO', 'https://github.com/TamilanBotsZ/AwesomeFilterPro')

AUTO_DELETE_SECONDS = int(environ.get('AUTO_DELETE_SECONDS', 300))
AUTO_DELETE = environ.get('AUTO_DELETE', True)
if AUTO_DELETE == "True":
    AUTO_DELETE = True

#Sample
SHORTNER_SITE = "omegalinks.in"
SHORTNER_API = "0ffce356f0dc1ce0b37703468078765181aeca0a"

