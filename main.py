import discord
import random
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="uwu hewwo", url="https://www.twitch.tv/champii"))
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
    await ctx.send(f"{random.raninit(1,6)})")

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
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"kicked {member} for {reason}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned {member} for {reason}")

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f"{member} muted")

@client.command()
@commands.has_permissions(kick_members=True)
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

@client.command(aliases=["simpdetector"])
async def simprate(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% a simp")

@client.command()
async def hackerman(ctx):
  responses = ["i have severe braindamage", "crack is fun", "just kill me", "crack addiction isnt bad its great"]
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url="https://cdn.discordapp.com/attachments/684090883158573109/709999393239072898/ezgif.com-video-to-gif.gif")
  embed.set_footer(text=f"{random.choice(responses)}")
  await ctx.send(embed=embed)

@client.command()
async def alike(ctx):
  embed=discord.Embed(color=0x800080)
  embed.set_image(url="https://i.imgur.com/J0irbhm.png")
  await ctx.send(embed=embed)
  embed=discord.Embed(color=0x800080)
  embed.set_image(url="https://i.imgur.com/CnvQbWF.jpg")
  await ctx.send(embed=embed)

@client.command(aliases=["gay"])
async def gayrate(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% gay")

@client.command(aliases=["overwatch"])
async def ice(ctx):
  embed=discord.Embed(color=0xd7fffe)
  embed.set_image(url="https://media1.tenor.com/images/31e9558485e1c445420b81096d7c9f12/tenor.gif?itemid=7349756")
  await ctx.send(embed=embed)

@client.command()
async def lolirate(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% loli")

@client.command(aliases=["chii"])
async def champii(ctx):
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url="https://i.imgur.com/rZapsKT.jpg")
  await ctx.send(embed=embed)
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url="https://i.imgur.com/IyFiOMK.jpg")
  await ctx.send(embed=embed)

@client.command()
async def kill(ctx, member : discord.Member):
  responses=["https://thumbs.gfycat.com/DapperDevotedLeonberger-size_restricted.gif",
  "https://media.tenor.com/images/bef50761d75e855c95cb94139c8c292f/tenor.gif",
  "https://media.tenor.com/images/6880dffc2f95f820d48633e1e3fc84f1/tenor.gif",
  "https://media.tenor.com/images/cc188df8e2541acfe485e6fd802d3b0d/tenor.gif",
  "https://media.tenor.com/images/a0c111e14b73a5ff9a876eb6beab6729/tenor.gif"]
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url=f"{random.choice(responses)}")
  await ctx.send(f"{member.mention} got killed by "+ctx.message.author.mention, embed=embed)

@client.command()
async def scam(ctx):
  embed=discord.Embed(title="Free Discord Nitro!", description="We here at discord want to give you a special gift in these times of need. Just click the link below for a **free** year of **Discord Nitro**! \n[𝗖𝗹𝗶𝗰𝗸 𝗺𝗲!](https://youtu.be/TsLHEDLhBGg)")
  embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/684090883158573109/715668142918991892/4a54064.png")
  await ctx.send(embed=embed)

@client.command()
async def copypasta(ctx):
  responses = ["Being on the internet can be very scary. With nord VPN, it can shield you from those harmful sites and safe guard your nudes you send to people like Insan. Be sure to use CODE pravda at checkout for a discount on the 3 yr plan which is only as low as 3.99 per month!",
  " I just don't understand what's wrong with like worshiping a girl. There's nothing wrong with that. Girls deserve to be worshiped. Not saying specifically me...but girls should be worshiped. Simping  isn't  bad. Simping is KING SHIT okay. You're a king if you're not afraid to simp.",
   "okay dude, that’s it, you’ve been acting a little gay lately and I’m genuinely concerned about your motives. Listen man, I honestly don’t care if you’re gay but when you do this gay ass shit to me it makes me feel extremely uncomfortable bro. I’m gonna ask you to stop right now",
   "What do you listen to dude? Rap? Bro, I'm only 12 and listen to kpop. You've probably never heard of it before, it's much too diverse for your liking. I'm not a fan of.. what's his name? Lilliam Pumpernickle? Yeaa, I can't stand that sort of music. Rap is always about big booty bitches and money and is far too mainstream. That's why I also listen to Jpop. It kinda lowkey and underground at the moment, but you should check out Twice, GFRIEND and IZ*one. Your rap can go take a hike while I listen to kpop and jpop with my friends. All of you think is that rap is superior and you wanna become a rapper. Well Kpop trainees take vigorous hours to be perfected meanwhile your stinky drug addict, alcoholic, horny rappers rap in some shitty bedroom that stinks of weed. Kpop idols have clean studios that are cleaned daily. Kpop music has a story meanwhile your stinky rap talks about bad stuff like drugs and alcohol. This is why kpop is superior and child friendly.",
   "Shut yo ching chong wing wong chila bila ping pong bling blong ring rong dinga dinga ding dong qing qong wing wong walla walla wing wong ying yong ying yang yingy yingy ying yang jing jong xing xong jinga xinga jing xang sing song sing sang sannga sannga sing sang iing iang ingy ingy iing iang ging gang ging ging ginga ginga ging gang hing haung hing hau hauie mauie hau hau ning nang ning nang ninga ningo ning ning zing zing zong zong zinga zingo zong zing ass the fuck up",
   "I don't think you guys realize how cool I am. Unlike you peasants, I have Discord **NITRO!** Thats right, full nitro. What do you fucking idiots have? Classic? Get outta here. No Nitro? Fucking loser lol. None of you will **EVER** be on my level cause I have Nitro and you don't. Do you get animated profile pictures? Thats what I thought. Do you get ***TWO FREE SERVER BOOSTS?*** Thats what I thought. You also don't get to change your discrim! Thats right, the four numbers at the end of your username that you haven't payed ANY attention to. How does that make you feel, non-nitro?"]
  embed=discord.Embed(title="funny pasta", description=f"{random.choice(responses)}")
  await ctx.send(embed=embed)

@client.command(aliases=["hornyrate"])
async def horny(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% horny")

@client.command()
@commands.has_permissions(kick_members=True)
async def pmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Parasites')
    await member.add_roles(role)
    await ctx.send(f"{member.mention} was sent to the gulag.")

@client.command()
@commands.has_permissions(kick_members=True)
async def punmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Parasites')
    await member.remove_roles(role)
    await ctx.send(f'{member.mention} was freed from the gulag by Western forces.')

@client.command()
async def kiss(ctx, member: discord.Member):
  responses = ["https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/tenor.gif?itemid=5649376",
  "https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515",
  "https://media1.tenor.com/images/7fd98defeb5fd901afe6ace0dffce96e/tenor.gif?itemid=9670722",
  "https://media1.tenor.com/images/3d56f6ef81e5c01241ff17c364b72529/tenor.gif?itemid=13843260",
  "https://media1.tenor.com/images/0ec5382910e34ca5649f6c328124daa1/tenor.gif?itemid=15556555",
  "https://media1.tenor.com/images/632a3db90c6ecd87f1242605f92120c7/tenor.gif?itemid=5608449"]
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url=f"{random.choice(responses)}")
  await ctx.send(f"{member.mention} got kissed by "+ctx.message.author.mention, embed=embed)

@client.command()
async def hug(ctx, member : discord.Member):
  responses = ["https://media1.tenor.com/images/e58eb2794ff1a12315665c28d5bc3f5e/tenor.gif?itemid=10195705",
  "https://media1.tenor.com/images/2d4138c7c24d21b9d17f66a54ee7ea03/tenor.gif?itemid=12535134",
  "https://media1.tenor.com/images/f20151a1f7e003426ca7f406b6f76c82/tenor.gif?itemid=13985247",
  "https://media1.tenor.com/images/969f0f462e4b7350da543f0231ba94cb/tenor.gif?itemid=14246498",
  "https://media1.tenor.com/images/4d89d7f963b41a416ec8a55230dab31b/tenor.gif?itemid=5166500",
  "https://media1.tenor.com/images/b77fd0cfd95f89f967be0a5ebb3b6c6a/tenor.gif?itemid=7864716",
  "https://media1.tenor.com/images/34a1d8c67e7b373de17bbfa5b8d35fc0/tenor.gif?itemid=8995974",
  "https://media1.tenor.com/images/8055f0ab4e377e35f5884dfe3e3fec52/tenor.gif?itemid=5210972",
  "https://media1.tenor.com/images/edea458dd2cbc76b17b7973a0c23685c/tenor.gif?itemid=13041472"]
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url=f"{random.choice(responses)}")
  await ctx.send(f"{member.mention} got a hug from "+ctx.message.author.mention, embed=embed)

keep_alive()
client.run("TOKEN")
