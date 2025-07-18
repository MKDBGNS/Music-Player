from pyrogram import Client
from pytgcalls import idle
from callsmusic import run
from config import API_ID, API_HASH, STRING_SESSION
import pytgcalls
print("✅ PyTgCalls version:", getattr(pytgcalls, "__version__", "unknown"))

userbot = Client(STRING_SESSION, API_ID, API_HASH)
userbot.start()
run()
idle()
