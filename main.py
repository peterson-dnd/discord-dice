import os
import discord
from discord.ext import commands
import logging
from dice.exceptions import *
from dice.roll import *
from dice.dice import *

client = commands.Bot(command_prefix="!", description="Dice Roll Bot")

def load_token(file: str) -> str:
    with open(file, 'r') as f:
        return f.readline()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def roll(ctx, *args):
    logging.info(f'Got a request!\n {ctx.message}')
    ttl = 18000
    roll_message = "`Roll: `"

    try:
        roll = Roll(list(args))
        roll.roll()
    except DiceComplexityException as e:
        print(f"{e}")
        await ctx.send(f"Failed to roll: {e}", delete_after=ttl)
        return
    roll_str = roll.rolled_dice_to_str()
    if len(roll_str) < 4000 - len(roll_message):
        await ctx.send(f"{roll_message}{roll.rolled_dice_to_str()}", delete_after=ttl) 
    else:
        await ctx.send(f"Roll: too large to output individual rolls", delete_after=ttl)

    #TODO: Output nat 20 and nat 1 as exclamation
    await ctx.send(f"`Total:` {roll.sum:,}", delete_after=ttl) 

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    token = load_token('.discord_token')
    client.run(token)
