from os import path, getenv
import time
import re
import asyncio
from os import environ as evn
id_pattern = re.compile(r'^.\d+$')

class Config:
    API_ID = int(getenv("API_ID", "26417030"))
    API_HASH = getenv("API_HASH", "bb50ad6a328bef08ef2be848e06a97a9")
    BOT_TOKEN = getenv("BOT_TOKEN", "5974370439:AAFvTPzADhK13URFU0DS1DDTn6V8lUeqznA")
    FSUB = getenv("FSUB", "beta_botz")
    CHID = int(getenv("CHID", "-1001805259061"))
    SUDO = [int(admin) if id_pattern.search(admin) else admin for admin in evn.get('SUDO', '1217302537').split(',')]
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://pranjalhu7253:pranjalhu@cluster0.qt8quq4.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
