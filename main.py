import discord
import time
from discord.ext import commands
from keep_alive import keep_alive

seconds = 18

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?",
                      case_insensitive=True,
                      intents_members=True)


@client.command()
async def ping(ctx):
    await ctx.send("pong")


@client.event
async def on_ready():
    print("online")


#DO NOT USE IT IS BUG
# @client.event
# async def on_message(ctx):
#     if ctx.content.startswith('hello'):
#         i = 0
#         i = i + 1
#         print('hi')


@client.command()
async def stats(ctx):

    await client.change_presence(
        activity=discord.Game('You better be practing...'))
    await ctx.send("Practice Bot version 1.0 by Panos")
    await ctx.send("Type ?commands to see all commands")
    print("Practice bot is up.")


@client.command()
async def practice_start(ctx):
    await ctx.send("Practice timer started, will notify in 30min")
    await ctx.send(
        "Also make sure to play fun games on https://www..information4u.net")
    await ctx.send("Use ?commands to see all commands")
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)
    await ctx.send("Practicing Finshed!!! @here")


@client.command()
async def commands(ctx):
    await ctx.send(
        "?practice - when you have practiced   ?commands - see all commands  ?stats - to see stats"
    )


keep_alive()
client.run(
    "TOKEN")
#Note: Line 21 is usually where the token goes (instead of TOKEN) but for obvious reasons I have censored it.
