import pytgcalls
import os

print("✅ PyTgCalls installed at:", pytgcalls.__path__)

for path in pytgcalls.__path__:
    stream_path = os.path.join(path, "stream")
    print("📁 pytgcalls/stream exists:", os.path.isdir(stream_path))
    if os.path.isdir(stream_path):
        print("📄 Contents:", os.listdir(stream_path))

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
