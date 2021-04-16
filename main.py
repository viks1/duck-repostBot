import discord
import random
import asyncio
from discord import Client
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get

bot = commands.Bot(command_prefix = '.')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('duck1 is online!')

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    embed.set_author(name='Commands')
    embed.add_field(name='ping', value='Returns the latency', inline=False)
    embed.add_field(name='test', value='Returns a quack', inline=False)
    await author.send(embed=embed)
    await ctx.message.delete()

@bot.command()
async def test(ctx):
    await ctx.send('quack')
    await ctx.message.delete()
    
@bot.command()
async def ping(ctx):
    await ctx.send(f'latency is {round(bot.latency * 1000)}ms')
    await ctx.message.delete()

bot.load_extension('pinbot')

async def change_status():
    await bot.wait_until_ready()
    statuses =  ["for 📌", "for your pin emotes"]
    while not bot.is_closed():
        status = random.choice(statuses)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(5)
bot.loop.create_task(change_status())

bot.run('your_token_here')