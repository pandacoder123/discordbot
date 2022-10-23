import discord
import time
import os
from discord.ext import commands
from keep_alive import keep_alive
from discord.utils import get


seconds = 1800
times_used = 0

intents = discord.Intents.all()
client = commands.Bot(command_prefix="?",
                      case_insensitive=True,
                      intents_members=True,intents= discord.Intents.all())


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
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send("Practice Practice Pratice by:")
        await ctx.send(ctx.author)

@client.command()
async def givemeadmin(ctx):
    for n in range(10):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send("pls give admin pls give admin pls give admin:")
        await ctx.send(ctx.author)

@client.command()
async def sssus(ctx):
    for n in range(50):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send("ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ by:")
        await ctx.send("AnonymouPerson#8232")

@client.command()
async def supersusss(ctx):
    for n in range(1000):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send("ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ@kokimaru by:")
        await ctx.send(ctx.author.mention)
        await ctx.send("@here")

@client.command()
async def spammmmm(ctx):
    for n in range(1000):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send("https://tenor.com/view/cat-cats-cat-eating-cat-eating-food-gif-24575246")
        

@client.command()
async def count(ctx):
    for o in range(100):
        # await ctx.send("https://information4u.net @here by:")
        await ctx.send(o)
        o=o+1
        



@client.command()
async def superkickkick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    ctx.send("you got kicked, RIP")

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


@client.command()
async def superbanban(ctx, member: discord.Member, *, reason=None):
    await member.unban(reason=reason)
    ctx.send("you got banned, double RIP")


@client.command()
@commands.has_permissions(kick_members=False)
async def commandkickk(ctx, member : discord.Member, *, reason=None):
    embed = discord.Embed(title="Kicked", description=f"You have been Kicked from {member.guild.name}.")
    embed.add_field(name="Reason:", value=reason)
    embed.add_field(name="Moderator:", value=f"{ctx.message.author.name}#{ctx.message.author.discriminator}")
    await member.send(embed=embed)  
    await member.kick(reason=reason)
    success = discord.Embed(title="Successfully Kicked", description=f"You Kicked {member.name}#{member.discriminator}")
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
#     if message.content == "e":
#         member = message.author
#         role = get(member.guild.roles, name="Blue")
#         await member.remove_roles(role)
#         await member.kick()

# @client.command()
# async def kick(ctx, member: discord.Member, *, reason=None):
#     await member.kick(reason=reason)
#     await ctx.send(f'User {member} has kicked.')


@client.command()
async def superspammm(ctx):
    for n in range(1000):
        await ctx.send(
            "https://tenor.com/view/cat-cats-cat-eating-cat-eating-food-gif-24575246 EEEEEEEEEEEE𝔼𝔼𝔼𝔼𝔼𝔼EEEEEEEEEEEEEE𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼𝔼 THERE IS NO WAY TO STOP THIS @everyone. SEVER NUKED BY:"
        )
        await ctx.send(ctx.author.mention)


@client.event
async def on_ready():
    synced = await client.tree.sync()
    print(f"Synced {len(synced)} command(s)")
    print("online")

@client.tree.command(name="hello")
async def hello(ctx):
  ctx.send("hello")


# @client.event
# async def on_message(ctx):
#     if ctx.content == "e":
#         member = ctx.author
#         role = get(member.guild.roles, name="Announcement Ping")
#         await member.remove_roles(role)
# @client.event
# async def on_message(ctx):
#     if ctx.content == "eee":
#         member = ctx.author
#         role = get(member.guild.roles, name="Violin")
#         await member.add_roles(role)







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














@client.event
async def on_message(message):
    if str(message.channel) == "general" and message.content == "deleteallnogoingback":
        await message.channel.purge(limit=99999)








  
  


async def print_time(total_seconds, ctx):
    total_mins = total_seconds / 60
    seconds = int(total_seconds % 60)
    hours = int(total_mins / 60)
    mins = int(total_mins % 60)
    await ctx.send('Time spend: {}h:{}m:{}s'.format(hours, mins, seconds))

@client.command()
async def practice_starttt(ctx):
  
  start_time = time.time()
  print('counting time...')
  
  
@client.command()
async def practice_end(ctx):
  stop_time = time.time()
  print_time(stop_time - start_time)

  
  
  




@client.command()
async def practice_startt(ctx):
    await ctx.send("Good job practing, remember to practice every day!")
    # await ctx.send(
    #     "Also make sure to play fun games on https://www.information4u.net")
    await ctx.send("Use ?commands to see all commands")
    await ctx.send("||orchestra on top||")
    global times_used
    





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
        "7.(im not typing it...) == DO NOT USE YOU WILL GET BANNED (why did i add this)")
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


@client.command()
async def stats_reset(ctx):
    await ctx.send("Reset practice time")
    await ctx.send("use ?stats to see how much we all practice")
    global times_used
    times_used = 0


keep_alive()
client.run(
    "MTAxNDg5NzE0MzYwMzAwMzQzMw.GoOunp.CapEe4vwQQ7nY4p1F1q4cKnfsd0o8v9UTYL6aY")

#Note: Line 21 is usually where the token goes (instead of TOKEN) but for obvious reasons I have censored it.
