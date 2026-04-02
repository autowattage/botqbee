# botqbee
fun litle discord bot i made for me and my friends on sky:cotl!

features to implement:
- color nametags
- birthdays
- gambling

current implemented features:
- swear jar

## how to use
1. create users.json with `touch users.json`
  a. this is where saved user data resides
2. create swearjar.json with `swearjar.json`
  a. this is where the list of swearwords reside. make an array of swearwords for the bot to detect
3. create .env with `touch .env && echo "BOT_TOKEN={your token}" > .env`
4. set up the python virtual environment
  a. `python3 -m venv bot-env`
  b. `source bot-env/bin/activate` (use `deactivate` command to exit)
5. install required packages
  a. `pip install discord.py`
  b. `pip install dotenv`
