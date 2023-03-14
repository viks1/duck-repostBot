import discord
import random
from discord.ext import commands

intents = discord.Intents.default();
intents.members = True

bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('duck1 is online!')


@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(
        colour=discord.Colour.orange()
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
bot.run('your_token_here')
