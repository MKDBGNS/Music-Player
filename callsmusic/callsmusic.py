from pyrogram import Client
from pytgcalls import PyTgCalls

from pytgcalls.types.stream import AudioPiped
from pytgcalls.types import StreamType
from queues import queues
import config

# Initialize Pyrogram client
client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)

# Initialize PyTgCalls
pytgcalls = PyTgCalls(client)

# Function to start streaming
async def stream_audio(chat_id):
    file_path = queues.get(chat_id)["file"]
    await pytgcalls.join_group_call(
        chat_id,
        AudioPiped(file_path),
        stream_type=StreamType().local_stream
    )

# Handle end of stream
@pytgcalls.on_stream_end()
async def on_stream_end(_, update: StreamAudioEnded):
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_group_call(chat_id)
    else:
        await stream_audio(chat_id)

# Start Pyrogram and PyTgCalls
def run():
    client.start()
    pytgcalls.start()
