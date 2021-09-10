import discord

client = discord.Client()

def load_token(file: str) -> str:
    with open(file, 'r') as f:
        return f.readline()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


token = load_token('.discord_token')
client.run(token)