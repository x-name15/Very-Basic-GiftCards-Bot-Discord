import random, string
import os, discord
from discord.ext import commands
from discord.ext.commands import bot
from discord import Game

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
Game = [
    "Variable1",
    "Variable2",
    "Variable3",
    "Variable4"
]
gamePlaying = random.choice(Game)

@bot.event
async def on_ready():
    print("Im ready!")
    print("----------")
    print('Logged in:')
    print(bot.user.name)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(gamePlaying))

def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

def NitroBox():
    code1 = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
    return f'https://discord.com/billing/promotions/xbox-game-pass/redeem/{code1}'

def Nike():
  code2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
  return f'Nike Code: {code2}'

def Netflix():
  code3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
  return f'Netflix Code: {code3}'

def Spotify():
  code4 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=19))
  return f'Spotify Code: {code4}'

def Blizzard():
    code5 = ('').join(random.choices(string.ascii_uppercase + string.digits, k=20))
    return f'Blizzard Code: {code5}'

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='All Commands', description=None)
    embed.set_thumbnail(url="https://i.imgur.com/pEePm5E.gif")
    embed.add_field(name="!help", value="Displays all available commands", inline=False)
    embed.add_field(name="!nitro", value="Generates a random Nitro Unchecked code", inline=False)
    embed.add_field(name="!nitrobox", value="Generates a random Xbox Nitro Code Unchecked",inline=False)
    embed.add_field(name="!netflix", value="Generates a random Netflix Unchecked Code", inline=False)
    embed.add_field(name="!nike", value="Generates a random Nike Unchecked Code", inline=False)
    embed.add_field(name="!blizzard", value="Generates a random Blizzard Unchecked Code", inline=False)
    embed.add_field(name="!spotify", value="Generates a random Spotify Unchecked Code", inline=False)
    embed.set_footer(text="This bot is open source: https://github.com/x-name15/Very-Basic-GiftCards-Bot-Discord")
    await ctx.send(embed=embed)

@bot.command()
async def nitro(ctx):
    await ctx.send(Nitro())

@bot.command()
async def nitrobox(ctx):
    await ctx.send(NitroBox())

@bot.command()
async def nike(ctx):
    await ctx.send(Nike())

@bot.command()
async def netflix(ctx):
    await ctx.send(Netflix())

@bot.command()
async def spotify(ctx):
    await ctx.send(Spotify())

@bot.command()
async def blizzard(ctx):
    await ctx.send(Blizzard())    
    
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)
