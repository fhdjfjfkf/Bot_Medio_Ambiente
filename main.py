import discord
from discord.ext import commands
import Secrets

intents = discord.Intents.default()
intents.message_content = True
intents.members = True 

bot = commands.Bot(command_prefix="$", intents=intents)


import events
import commands


commands.setup(bot)

bot.run(Secrets.Tokendc)