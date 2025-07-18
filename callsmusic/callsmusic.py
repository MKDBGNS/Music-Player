from pyrogram import Client

from pytgcalls.group_call_factory import GroupCallFactory

from queues import queues
import config

# Initialize Pyrogram client (user session)
client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)

# Create GroupCallFactory instance
group_call_factory = GroupCallFactory(client)

# Create PyTgCalls instance
pytgcalls = group_call_factory.get_group_call()

# Function to start streaming
async def stream_audio(chat_id):
    file_path = queues.get(chat_id)["file"]
    await pytgcalls.join(chat_id, file_path)

# Handle end of stream (basic loop handler)
@pytgcalls.on_network_status_changed
async def on_stream_end(_, update):
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave(chat_id)
    else:
        await stream_audio(chat_id)

# Start Pyrogram and PyTgCalls
def run():
    client.start()
    pytgcalls.start()
