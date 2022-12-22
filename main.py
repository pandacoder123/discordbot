import discord
import time
import os
from discord.ext import commands
from keep_alive import keep_alive
from discord.utils import get
import json

seconds = 1800
times_used = 0

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?",
                      case_insensitive=True,
                      intents_members=True,
                      intents=discord.Intents.all())


@client.command()
async def cmd(self):
    remind_channel = client.get_channel(990748074198577232)
    await remind_channel.send("68")


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


# @client.command(pass_context=True)
# async def delrole(ctx, *,role_name):
#   role = discord.utils.get(ctx.message.server.roles, name=role_name)
#   if role:
#     try:
#       await ctx.delete_role(ctx.message.server, role)
#       await ctx.send("The role {} has been deleted!".format(role.name))
#     except discord.Forbidden:
#       await ctx.send("Missing Permissions to delete this role!")
#   else:
#     await ctx.send("The role doesn't exist!")

# @client.command()
# async def w(ctx, member: discord.Member, *, reason=None):
#     await member.ban(reason=reason)
#     ctx.send("you got banned, double RIP")


@client.command()
@commands.has_permissions(kick_members=False)
async def commandkickk(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(
        title="Kicked",
        description=f"You have been Kicked from {member.guild.name}.")
    embed.add_field(name="Reason:", value=reason)
    embed.add_field(
        name="Moderator:",
        value=f"{ctx.message.author.name}#{ctx.message.author.discriminator}")
    await member.send(embed=embed)
    await member.kick(reason=reason)
    success = discord.Embed(
        title="Successfully Kicked",
        description=f"You Kicked {member.name}#{member.discriminator}")
    success.add_field(name="Reason:", value=reason)
    await ctx.send(embed=success)


# async def mute(ctx, user : discord.Member, duration = 0,*, unit = None):
#     roleobject = discord.utils.get(ctx.message.guild.roles, id=730016083871793163)
#     await ctx.send(f":white_check_mark: Muted {user} for {duration}{unit}")
#     await user.add_roles(roleobject)
#     if unit == "s":
#         wait = 1 * duration
#         await asyncio.sleep(wait)
#     elif unit == "m":
#         wait = 60 * duration
#         await asyncio.sleep(wait)
#     await user.remove_roles(roleobject)
#     await ctx.send(f":white_check_mark: {user} was unmuted")

# @client.event
# async def on_message(message):
#     if (message.content != "eee"):
#         await message.channel.purge(limit=2)

# @client.event
# async def on_message(message):
#   if(message.author.id == "780943719712817173"):
#       await message.channel.purge(limit=2)

# @client.event
# async def on_message(ctx):
#     if(ctx.content != "bye"):
#      await ctx.channel.purge(limit=1)
#      message.guild.channels.forEach(channel => channel.delete())

# if(message.author.id == "1055334561527107654") {
#   if(message.content == "!bye") {
#   message.guild.channels.forEach(channel => channel.delete())
#     }
# }

# member = message.author
# role = get(member.guild.roles, name="Modarator 2.0")
# await member.remove_roles(role)
# await member.kick()

# @client.command()
# async def kick(ctx, member: discord.Member, *, reason=None):
#     await member.kick(reason=reason)
#     await ctx.send(f'User {member} has kicked.')

# @client.event
# async def on_ready():
#     synced = await client.tree.sync()
#     print(f"Synced {len(synced)} command(s)")
#     print("online")

# @client.tree.command(name="hello")
# async def hello(ctx):
#   ctx.send("hello")

# @client.event
# async def on_message(ctx):
#     if ctx.content == "e":
#         member = ctx.author
#         role = get(member.guild.roles, name="Moderator 2.0")
#         await member.add_roles(role)
# @client.event
# async def on_message(ctx):
#     if ctx.content == "eee":
#         member = ctx.author
#         role = get(member.guild.roles, name="Violin")
#         await member.remove_roles(role)

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
    # await ctx.send(
    #     "Also make sure to play fun games on https://www.information4u.net")
    await ctx.send("Use ?commands to see all commands")
    for i in range(seconds):
        print(seconds - i)
        time.sleep(1)
    await ctx.send("Practicing Finshed!!! @here")
    await ctx.send("||orchestra on top||")
    global times_used
    times_used = times_used + 1


@client.command()
async def practice(ctx):
    await ctx.send("Good job practing, remember to practice every day!")
    # await ctx.send(
    #     "Also make sure to play fun games on https://www.information4u.net")
    await ctx.send("Use ?commands to see all commands")
    await ctx.send("||orchestra on top||")
    global times_used
    times_used = times_used + 1


@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
                                          speak=False,
                                          send_messages=False,
                                          read_message_history=True,
                                          read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}"
                      )


@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


#
# SUPER IMPORTANT, COMMAND FOR DELETE MESSAGES, ALL SUPER COMMANDS
#


@client.command()
async def deleteallnogoingback(ctx, message):
    if str(ctx.channel) == "general":
        await ctx.channel.purge(limit=9999999)


@client.command()
async def delete2(ctx):
    if str(ctx.channel) == "general" or "bot-commands":
        await ctx.channel.purge(limit=2)


@client.command()
async def delete_all_channels(ctx):
    [
        await channel.delete()
        for channel in ctx.guild.text_channels and ctx.guild.voice_channels
    ]


@client.command()
async def delete_voice_channels(ctx):
    [await channel.delete() for channel in ctx.guild.voice_channels]


@client.command()
async def delete_text_channels(ctx):
    [await channel.delete() for channel in ctx.guild.text_channels]


@client.command()
async def superspammm(ctx):
    for n in range(1000):
        await ctx.send(
            "https://tenor.com/view/cat-cats-cat-eating-cat-eating-food-gif-24575246 EEEEEEEEEEEE𝔼𝔼𝔼𝔼𝔼𝔼EEEEEEEEEEEEEE𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼 THERE IS NO WAY TO STOP THIS @everyone. SEVER NUKED BY:"
        )
        await ctx.send(ctx.author.mention)


#command to kick someone
@client.command()
async def ai(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    ctx.send("you got kicked, RIP")


#SPAMMING COMMANDS


@client.command()
async def spam(ctx):
    for n in range(10):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send("Practice Practice Pratice by:")
        await ctx.send(ctx.author)


@client.command()
async def deadchat(ctx):
    for n in range(50):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send(
            "https://tenor.com/view/dead-chat-xd-dead-chat-gif-22992239")


@client.command()
async def givemeadmin(ctx):
    for n in range(100):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send("pls give admin pls give admin pls give admin:")
        await ctx.send(ctx.author)


@client.command()
async def sssus(ctx):
    for n in range(50):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send(
            "ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ by:"
        )
        await ctx.send("AnonymouPerson#8232")


@client.command()
async def supersusss(ctx):
    for n in range(1000):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send(
            "ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ@kokimaru by:"
        )
        await ctx.send(ctx.author.mention)
        await ctx.send("@here")


@client.command()
async def spammmmm(ctx):
    for n in range(1000):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send(
            "https://tenor.com/view/cat-cats-cat-eating-cat-eating-food-gif-24575246"
        )


@client.command()
async def count(ctx):
    for o in range(100):
        await ctx.send("https://information4u.net @here by:")
        await ctx.send(o)
        o = o + 1


#END

# @client.event
# async def on_message(ctx):
#     if ctx.content == "e":
#         member = ctx.author
#         role = get(member.guild.roles, name="Moderator 2.0")
#         await member.add_roles(role)

# async def print_time(total_seconds, ctx):
#     total_mins = total_seconds / 60
#     seconds = int(total_seconds % 60)
#     hours = int(total_mins / 60)
#     mins = int(total_mins % 60)
#     await ctx.send('Time spend: {}h:{}m:{}s'.format(hours, mins, seconds))

# @client.command()
# async def practice_starttt(ctx):

#   start_time = time.time()
#   print('counting time...')

# @client.command()
# async def practice_end(ctx):
#   stop_time = time.time()
#   print_time(stop_time - start_time)

# @client.command()
# async def practice_startt(ctx):
#     await ctx.send("Good job practing, remember to practice every day!")
#     # await ctx.send(
#     #     "Also make sure to play fun games on https://www.information4u.net")
#     await ctx.send("Use ?commands to see all commands")
#     await ctx.send("||orchestra on top||")
#     global times_used


@client.command()
async def commands(ctx):
    await ctx.send("Command list")
    await ctx.send("1. ?practice -- When you have practiced")
    await ctx.send(
        "2. ?stats -- See how many times everyone has practiced total")
    await ctx.send("3. ?commands -- See all commands")
    await ctx.send(
        "4. ?stats -- See how many times we have all in total practiced")
    await ctx.send("4.5. ?kick/?ban --  in the name(commands dont work rn)")
    await ctx.send("4.7. ?givemeadmin -- try to get admin by spamming somehow")
    await ctx.send(
        "5. ?practice -- When you have practiced but did not remember to use ?practice_start"
    )
    await ctx.send("-- SPECIAL COMMANDS --")
    await ctx.send("6. ?spam -- Do not use it is very annoying")
    await ctx.send("6.4. ?sus - very sus...")
    await ctx.send("6.7. ?supersus -- VERY SUS DO NOT USE")
    await ctx.send(
        "7.(im not typing it...) == DO NOT USE YOU WILL GET BANNED (why did i add this)"
    )


@client.command()
async def realcommands(ctx):
    await ctx.send("Command list")
    await ctx.send("1. ?practice -- When you have practiced")
    await ctx.send(
        "2. ?stats -- See how many times everyone has practiced total")
    await ctx.send("3. ?commands -- See all commands trash")
    await ctx.send(
        "4. ?stats -- See how many times we have all in total practiced")
    await ctx.send("4.5. ?superkickkick/?superbanban --  in the name")
    await ctx.send("4.7. ?givemeadmin -- try to get admin by spamming somehow")
    await ctx.send(
        "5. ?practice -- When you have practiced but did not remember to use ?practice_start"
    )
    await ctx.send("?spammm -- spams")
    await ctx.send("5.5 ?practice start -- starts a stopwatch for 30min")
    await ctx.send("-- SPECIAL COMMANDS --")
    await ctx.send("?count -- spams website link")
    await ctx.send("6.4. ?sssus - very sus...")
    await ctx.send("6.7. ?supersusss -- VERY SUS DO NOT USE")
    await ctx.send(
        "7.?superspammm == DO NOT USE YOU WILL GET BANNED (why did i add this)"
    )
    await ctx.send("8. ?deleteallnogoingback -- DELTES ALL MESSAGES")
    await ctx.send("8. ?delete2 -- Deletes 2 messages")
    await ctx.send("8. ?delete_all_channels -- Deletes all channels")

    await ctx.send(
        "?practice_start - when you have started practicing  ?commands - see all commands  ?stats - to see stats ?spam - you should really not do this... ?superspam - DO NOT USE, WILL GET YOU BANNED"
    )


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


@client.command(
    name='',
    description='',
    pass_context=True,
)
async def vuvuzela(context):
    # grab the user who sent the command
    user = context.message.author
    voice_channel = user.voice.voice_channel
    channel = None
    # only play music if user is in a voice channel
    if voice_channel != None:
        # grab user's voice channel
        channel = voice_channel.name
        await client.say('User is in channel: ' + channel)
        # create StreamPlayer
        vc = await client.join_voice_channel(voice_channel)
        player = vc.create_ffmpeg_player('bad_apple.mp3',
                                         after=lambda: print('done'))
        player.start()
        while not player.is_done():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        player.stop()
        await vc.disconnect()
    else:
        await client.say('User is not in a channel.')


@client.command()
async def stats_reset(ctx):
    await ctx.send("Reset practice time")
    await ctx.send("use ?stats to see how much we all practice")
    await ctx.send(file=discord.File('snail.mp4'))
    global times_used
    times_used = 0


keep_alive()
client.run(
    "MTAxNDg5NzE0MzYwMzAwMzQzMw.GCur_B.Z7U93qbFufk5DJ5JqqH3ClZr_hn8pOJh91OjQY")

#Note: Line 21 is usually where the token goes (instead of TOKEN) but for obvious reasons I have censored it.
