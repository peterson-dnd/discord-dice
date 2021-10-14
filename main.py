import os
import discord
from discord.ext import commands
import logging

client = commands.Bot(command_prefix="!", description="Dice Roll Bot")

def load_token(file: str) -> str:
    with open(file, 'r') as f:
        return f.readline()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#        return
#    if message.content.startswith('$hello'):
#        logging.info('Got a request!')
#        await message.channel.send('Hello!')

@client.command()
async def roll(ctx, *args):
    logging.info(f'Got a request!\n {ctx.message}')
    await ctx.send(f"Hello World! {args}") 

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    token = load_token('.discord_token')
    client.run(token)