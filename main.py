import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import json

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

# turn swearword.json into editable python dictonary
with open("swearjar.json", "r") as f:
    swdata = json.load(f)
swearwords = swdata["swears"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    
    # swear jar
    if any(swear in message.content.lower() for swear in swearwords):
        # update count (i know this is ugly ill fix it later)
        if message.author.id in swdata["users"]:
            swdata["users"][message.author.id] += 1
        else:
            swcount = swdata["users"].setdefault(message.author.id, 1)
        # writing update to json
        with open("swearjar.json", "w") as f:
            json.dump(swdata, f, ensure_ascii=False, indent=3)
        # warn user
        await message.channel.send(f"Hey {message.author.name}! Watch your language! You've sworn {swcount} time{"s" if swcount!=1 else ""}!")

    await bot.process_commands(message)

# test command
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(os.getenv('BOT_TOKEN'))
