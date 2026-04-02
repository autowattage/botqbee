import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import json

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

with open("swearjar.json", "r") as f: swears = json.load(f)
with open("users.json", "r") as f: userjson = json.load(f)
print(userjson)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user: return
    
    # swear jar
    if any(word in message.content.lower() for word in swears):
        # update count (i know this is ugly ill fix it later)
        userjson.setdefault(str(message.author.id), 0)
        userjson[str(message.author.id)] += 1
        # writing update to json
        with open("users.json", "w") as f:
            json.dump(userjson, f, ensure_ascii=True, indent=3)
                # warn user
        await message.channel.send(f"Hey {message.author.name}! Watch your language! You've sworn {userjson[str(message.author.id)]} time{"s" if userjson[str(message.author.id)] !=1 else ""}!")

    await bot.process_commands(message)

# test command
@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

bot.run(os.getenv('BOT_TOKEN'))
