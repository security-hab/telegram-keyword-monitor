from telethon import TelegramClient, events
import asyncio
import re

# Insert your credentials here
api_id = 'YOUR_API_ID'  # Replace with your Telegram API ID
api_hash = 'YOUR_API_HASH'  # Replace with your Telegram API Hash
password = 'YOUR_PASSWORD'  # Replace with your two-factor authentication password, if enabled
channels_to_monitor = [
    'CHANNEL_1', 'CHANNEL_2', 'CHANNEL_3'
]  # Replace with the list of channel usernames to monitor
keywords = ['KEYWORD_1', 'KEYWORD_2', 'KEYWORD_3']  # Replace with the list of keywords to search for
group_id_for_notifications = 'YOUR_GROUP_ID'  # Replace with your group's chat ID

# Create a Telethon client
client = TelegramClient('session_name', api_id, api_hash)

# Function to parse links from a message
def extract_links(message_text):
    """
    Extracts all URLs from the given text.
    :param message_text: Text of the message
    :return: List of extracted URLs
    """
    links = re.findall(r'(https?://\S+)', message_text)
    return links

# Asynchronous function to monitor channels
@client.on(events.NewMessage(chats=channels_to_monitor))
async def handler(event):
    """
    Event handler that triggers when a new message is posted in the monitored channels.
    If the message contains any of the keywords, it forwards the message to the specified group.
    :param event: New message event
    """
    message_text = event.message.message

    # Check if any of the keywords exist in the message
    if any(keyword.lower() in message_text.lower() for keyword in keywords):
        print(f"Keyword found in message: {message_text}")
        links = extract_links(message_text)
        if links:
            print("Found links:", links)

        # Forward the message to the specified group
        await client.forward_messages(group_id_for_notifications, event.message)

# Bot startup function with two-factor authentication support
async def main():
    """
    Main function to start the bot and keep it running.
    Handles two-factor authentication if enabled.
    """
    try:
        # Start the client with the specified password
        await client.start(password=password)
        print("Bot is running and monitoring channels...")
        await client.run_until_disconnected()
    except Exception as e:
        print(f"Authentication or connection error: {e}")

# Run the main function using asyncio
asyncio.run(main())
