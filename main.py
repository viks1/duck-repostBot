import discord
import json
from discord.ext import commands
import tracemalloc

tracemalloc.start()
with open('required files/cfg.json') as f:
    data = json.load(f)
    token = data["token"]

bot = commands.Bot(command_prefix='.', intents=discord.Intents.all()) #the new discord.py update broke it a year ago with intents

@bot.event
async def on_ready():
    print('duck1 is online!')
    try:
        sync = await bot.tree.sync()  # to sync the commands
        print("commands working")
    except Exception as bro:
        print(bro)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("quack")

@bot.tree.command(name="help")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message("if you have issues: https://github.com/viks1/duck-pinbot")

@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(round(bot.latency*1000))


bot.load_extension('pinbot')
bot.run(token)