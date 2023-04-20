from os import path, getenv
import time
import re
import asyncio
from os import environ as evn
id_pattern = re.compile(r'^.\d+$')

class Config:
    API_ID = int(getenv("API_ID", "0112234"))
    API_HASH = getenv("API_HASH", "abcdefg")
    BOT_TOKEN = getenv("BOT_TOKEN", "1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW")
    FSUB = getenv("FSUB", "beta_botz")
    CHID = int(getenv("CHID", "-1001858865209"))
    SUDO = [int(admin) if id_pattern.search(admin) else admin for admin in evn.get('SUDO', '5558249587').split()]
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
