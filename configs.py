from os import path, getenv
import time
import re
import asyncio
from os import environ as evn
id_pattern = re.compile(r'^.\d+$')

class Config:
    API_ID = int(getenv("API_ID", "28761758"))
    API_HASH = getenv("API_HASH", "92ae33f906891d308ec9225c9cfc6786")
    BOT_TOKEN = getenv("BOT_TOKEN", "5974370439:AAFvTPzADhK13URFU0DS1DDTn6V8lUeqznA")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-1001788635529"))
    SUDO = [int(admin) if id_pattern.search(admin) else admin for admin in evn.get('SUDO', '1217302537').split()]
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://pranjalhu7253:pranjalhu@cluster0.qt8quq4.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
