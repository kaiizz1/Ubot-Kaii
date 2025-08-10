import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "110"))

DEVS = list(map(int, os.getenv("DEVS", "6699855714").split()))

API_ID = int(os.getenv("API_ID", "22398048"))

API_HASH = os.getenv("API_HASH", "a0bd13df765158e4992af9d2cdf755a8")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8363798119:AAFHj-56J4bxFeAGY9j-iKCVCuup4t9Lj0o")

OWNER_ID = int(os.getenv("OWNER_ID", "6699855714"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "MA2sUZ4HdAfBegL36HiG4BUG")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://kaii:6699855714@cluster0.5zgg4u9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4810169289"))
