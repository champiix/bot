import discord
import random
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("uwu"))
    print("bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command(aliases=["8ball"])
async def _8ball(ctx):
    responses = ["yes",
                 "maybe",
                 "my sources say no",
                 "my sources say yes",
                 "no",
                 "bitch tf you crazy?"]
    await ctx.send( f" {random.choice(responses)}, "+ctx.message.author.mention)

@client.command(aliases=["roll"])
async def dice(ctx):
    responses = ["1",
                 "2",
                 "3",
                 "4",
                 "5",
                 "6"]
    await ctx.send(f"{random.choice(responses)}")

@client.command(aliases=["cf"])
async def coinflip(ctx):
    responses = ["heads",
                 "tails",]
    await ctx.send(f"{random.choice(responses)}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"kicked {member} for {reason}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned {member} for {reason}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f"{member} muted")

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send(f'{member} unmuted')


@client.command()
async def pravda(ctx):
    await ctx.send("Workers of the world unite!")

@client.command()
async def culprits(ctx):
    await ctx.send("AKM > AK103")

@client.command(pass_context=True, aliases=["propaganda"])
async def manifesto(ctx):

  embed = discord.Embed(
    colour = discord.Colour.red()
  )

  embed.set_author(name="Pravda Manifesto Preface")
  embed.add_field(name="uwu", value="The Pravda Union is a conglomeration of United Republics spanning from Eastern Europe and Northern Asia into Siberia. The works of the party have driven the parasites out of her borders and have continued to ensure safety within her beloved empire. The Central Committee and works have exceeded their mortal ambitions, and restored order and prosperity to the vast Union. Pravda stands as a turning point in history, about the enter into a state of hard work and productivity. To accomplish such a remarkable task, we must end the exploitation by the bourgeoisie, spread out socialist ideals and stand victorious over our foes. Workers of the world, unite! ☭")

  await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(title="red velvet", description="communist bot with a kpop pfp", color=0xf4c2c2)

    # give info about you here
    embed.add_field(name="Author", value="champii~")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="not a public bot rn")

    await ctx.send(embed=embed)

@client.command()
async def logo(ctx):
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_image(url="https://cdn.discordapp.com/attachments/684090883158573109/697947452099002378/1586474027404.gif")
    await ctx.send(embed=embed)

@client.command()
async def eesti(ctx):
  embed = discord.Embed(colour=discord.Colour.blue())
  embed.set_image(url="https://media.tenor.com/images/2cac9910ace64c5a882dc6f6e5a7fed5/tenor.gif")
  await ctx.send(embed=embed)

@client.command(aliases=["coughon"])
@commands.has_role('infected')
async def cough(ctx, member: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name='infected')
  await member.add_roles(role)
  await ctx.send(f"{member.mention} got coughed on by "+ctx.message.author.mention)

@client.command(aliases=["gitrepo"])
async def repo(ctx):
  embed=discord.Embed(title="discord bot github repo", url="https://github.com/champiix/bot", description="ayaya", color=0xff00ff)
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/590944283675328541/702653440966524988/JPEG_20190814_011853.jpg")
  await ctx.send(embed=embed)

@client.command()
@commands.has_role("doctor")
async def heal(ctx, member: discord.Member):
  role = discord.utils.get(ctx.guild.roles, name='infected')
  await member.remove_roles(role)
  await ctx.send(f"{member.mention} got healed by "+ctx.message.author.mention)

@client.command()
async def t(ctx):
  await ctx.send("stfu")

@client.command(aliases=["n"])
async def nordvpn(ctx):
  await ctx.send("Being on the internet can be very scary. With nord VPN, it can shield you from those harmful sites and safe guard your nudes you send to people like Insan. Be sure to use CODE pravda at checkout for a discount on the 3 yr plan which is only as low as 3.99 per month!")

@client.command()
async def tunnelbear(ctx):
  await ctx.send("Tunnelbear is the simple VPN app that makes it easy to browse privately and enjoy a more open internet. With tunnelbear turned on, your connection via landline or Wi-Fi is secured and your online activity is kept private from your internet provider advertizers, hackers and anyone else who's trying to track you or profit from your data. They have a top rated privacy policy and they do not log your activity and you can try it for free, with 500 megabytes of free data and no credit card required over at the link in the description. And, if you choose to get an unlimited plan you can save 10 percent by going to tunnelbear.com/pravda also linked in the video description, actually the same link; Yeah!")

@client.command()
async def pia(ctx):
  await ctx.send("Looking for an affordable and reliable VPN? Private Internet Access encrypts your internet traffic and uses a safe protected IP. It also works on both your computer and smartphone. Check it out today at privateinternetaccess.com/

@client.command()
async def slap(ctx, member : discord.Member):
  responses=["https://media.tenor.com/images/bd092fb261df4588a51f9dd1f4815fea/tenor.gif",
  "https://media.tenor.com/images/ac09dd389d43f3bc0adad6432a942532/tenor.gif",
  "https://media.tenor.com/images/6dbd997e3e79f21b7841b244833325c0/tenor.gif",
  "https://media.tenor.com/images/604a56f1e6e594beb00c265ea7a40dca/tenor.gif",
  "https://media.tenor.com/images/56387025912c48b5af27c0711a2645b8/tenor.gif",
  "https://media.tenor.com/images/f8f050aa79f92f3e45669ef8db45ed1e/tenor.gif",
  "https://media.tenor.com/images/79c666d38d5494bad25c5c023c0bbc44/tenor.gif",
  "https://media.tenor.com/images/47698b115e4185036e95111f81baab45/tenor.gif",
  "https://media.tenor.com/images/53b846f3cc11c7c5fe358fc6d458901d/tenor.gif",
  "https://media.tenor.com/images/091e0502e5fda1201ee76f5f26eea195/tenor.gif"]
   embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url=f"{random.choice(responses)}")
  await ctx.send(f"{member.mention} got slapped by "+ctx.message.author.mention, embed=embed)
keep_alive()
client.run("TOKEN")
