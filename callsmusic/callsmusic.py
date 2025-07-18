from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls.types import Update

from pytgcalls.types.input_stream import AudioPiped
from queues import queues
import config

# Initialize Pyrogram client
client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)

# Initialize PyTgCalls
pytgcalls = PyTgCalls(client)

# Handle end of stream
@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update) -> None:
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await pytgcalls.change_stream(
            chat_id,
            AudioPiped(queues.get(chat_id)["file"])
        )

# Start PyTgCalls
run = pytgcalls.start
