# This is a very basic bot!
import discord
from discord.ext import commands
import random

description = "A basic bot!"

intents = discord.Intents.default() # Replace default with all if you want to enable all intents
intents.members = True # remove this line if you made it all

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def ping(ctx):
  await ctx.send(bot.latency)


if __name__ == "__main__": # Checks if the file is being imported
    bot.run("") # Put your bot's TOKEN HERE
