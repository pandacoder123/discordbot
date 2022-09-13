import discord
import time
from discord.ext import commands
from keep_alive import keep_alive

seconds = 1
times_used = 0

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?",
                      case_insensitive=True,
                      intents_members=True)


@client.command()
async def info(ctx):
    await ctx.send("Hello I am practice bot")
    await ctx.send("I will help you practice more")
    await ctx.send("By: Panos")
    await ctx.send("Use ?commands to see all commands")
    await ctx.send(
        "Also keep in mind that I am slow at sending messages so when sending a commands wait a few seconds so i can process it"
    )
    await ctx.send(
        "If there is anything not working or you want to send me an idea, ping me at @pan521"
    )
    await ctx.send("If you want to view the code dm me")


@client.command()
async def spam(ctx):
    for n in range(10):
        await ctx.send("https://information4u.net @here by:")
        await ctx.send(ctx.author)


@client.command()
async def superspam(ctx):
    for n in range(1000):
        await ctx.send(
            "EEEEEEEEEEEE𝔼𝔼𝔼𝔼𝔼𝔼EEEEEEEEEEEEEE𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼 THERE IS NO WAY TO STOP THIS @everyone. SEVER NUKED BY:"
        )
        await ctx.send(ctx.author.mention)


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

# @client.command()
# async def stats(ctx):

#     await client.change_presence(
#         activity=discord.Game('You better be practing...'))
#     await ctx.send("Practice Bot version 1.0 by Panos")
#     await ctx.send("Type ?commands to see all commands")
#     print("Practice bot is up.")


@client.command()
async def practice_start(ctx):
    await ctx.send("Practice timer started, will notify in 30min")
    await ctx.send(
        "Also make sure to play fun games on https://www.information4u.net")
    await ctx.send("Use ?commands to see all commands")
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)
    await ctx.send("Practicing Finshed!!! @here")
    global times_used
    times_used = times_used + 1


@client.command()
async def commands(ctx):
    await ctx.send("Command list")
    await ctx.send("1. ?practice start -- When you have practiced")
    await ctx.send(
        "2. ?stats -- See how many times everyone has practiced total")
    await ctx.send("3. ?commands -- See all commands")
    await ctx.send(
        "4. ?stats -- See how many times we have all in total practiced")
    await ctx.send("-- SPECIAL COMMANDS --")
    await ctx.send("4. ?spam -- Do not use it is very annoying")
    await ctx.send(
        "5. ..--.. ... ..- .--. . .-. ... .--. .- -- -- DO NOT USE YOU WILL GET BANNED (why did i add this)"
    )
    # await ctx.send(
    #     "?practice_start - when you have started practicing  ?commands - see all commands  ?stats - to see stats ?spam - you should really not do this... ?superspam - DO NOT USE, WILL GET YOU BANNED"
    # )


@client.command()
async def stats(ctx):
    await client.change_presence(
        activity=discord.Game('You better be practing...'))
    await ctx.send("Practice Bot version 1.0 by Panos")
    await ctx.send("Type ?commands to see all commands")
    print("Practice bot is up.")
    await ctx.send("Also, in total we have all practiced:")
    await ctx.send(times_used)
    await ctx.send("times")
    await ctx.send("Or")
    await ctx.send("We have practiced a total of")
    await ctx.send(times_used * 30)
    await ctx.send("minutes")


keep_alive()
client.run(
    "")
#Note: Line 21 is usually where the token goes (instead of TOKEN) but for obvious reasons I have censored it.
