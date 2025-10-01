import discord
import asyncio
from api import obtener_chiste  # Import the function that fetches jokes from the API

# Define the bot's "intents" (what events it can listen to)
intents = discord.Intents.default()
intents.message_content = True  # Allow the bot to read the content of messages

# Create the client (the bot instance) with the chosen intents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """Event triggered when the bot successfully connects to Discord."""
    print(f'Bot connected as {client.user}')

@client.event
async def on_message(message):
    """
    Event triggered whenever a message is sent in a channel.
    The bot checks if the message starts with one of its commands.
    """
    # Prevent the bot from responding to its own messages
    if message.author == client.user:
        return

    # Command: "!chiste" → Get a joke in Spanish
    if message.content.startswith('!chiste'):
        chiste = obtener_chiste("es")
        await enviar_chiste(message, chiste)

    # Command: "!joke" → Get a joke in English
    elif message.content.startswith('!joke'):
        chiste = obtener_chiste("en")
        await enviar_chiste(message, chiste)

async def enviar_chiste(message, chiste):
    """
    Sends the joke to the user who requested it.
    Supports one-part and two-part jokes.
    """
    # If the API request failed, notify the user
    if not chiste:
        await message.channel.send(f"{message.author.mention} An error occurred while fetching the joke.")
        return

    # If the joke has a "setup" and a "delivery" (two-part joke)
    if 'setup' in chiste:
        # Send the setup (first part of the joke)
        await message.channel.send(f"{message.author.mention} {chiste['setup']}")
        
        # Wait 1 second before sending the punchline (delivery)
        if 'delivery' in chiste:
            await asyncio.sleep(1)
            await message.channel.send(chiste['delivery'])
    
    # If the joke is only one part (simple joke)
    elif 'joke' in chiste:
        await message.channel.send(f"{message.author.mention} {chiste['joke']}")

# Run the bot with your Discord token
client.run('INSERT TOKEN HERE')
