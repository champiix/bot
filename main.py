import discord
import random
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="ayaya", url="https://www.twitch.tv/champii"))
    print("bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("That command doesn't exist!")
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("You forgot to mention a user!")

@client.command(aliases=["p"])
async def ping(ctx):
    await ctx.send(f'finding your local egirl took **{round(client.latency * 1000)}ms**')
 
@client.command(aliases=["8ball"])
async def _8ball(ctx):
    responses = ["yes",
                 "maybe",
                 "my sources say no",
                 "my sources say yes",
                 "no",
                 "idk but stan twice"]
    await ctx.send( f" {random.choice(responses)}, "+ctx.message.author.mention)

@client.command(aliases=["roll"])
async def dice(ctx):
    await ctx.send(f"{random.randint(1,6)}")

@client.command(aliases=["cf"])
async def coinflip(ctx):
    responses = ["heads",
                 "tails",]
    await ctx.send(f"{random.choice(responses)}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount +1)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"kicked {member.mention} for {reason}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned {member.mention} for {reason}")

@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, reason=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role, reason=reason)
    await ctx.send(f"{member.mention} muted for {reason}")

@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send(f'{member.mention} unmuted')

@client.command()
async def pravda(ctx):
    await ctx.send("Workers of the world unite!")

@client.command(aliases=["zach", "zachary"])
async def culprits(ctx):
  embed=discord.Embed(colour=0x1BFF00)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906508/peach%20bot/5qAZzdj_vfmswb.png")
  await ctx.send("AKM > AK103", embed=embed)
  embed=discord.Embed(colour=0x1BFF00)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906266/peach%20bot/shEOdYn_gwunqp.png")
  await ctx.send(embed=embed)

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
    embed = discord.Embed(title="peach", description="communist bot with a kpop pfp", color=0xf4c2c2)

    # give info about you here
    embed.add_field(name="Author", value="champii~")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="not a public bot rn")

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

@client.command(aliases=["cure"])
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
  await ctx.send("Looking for an affordable and reliable VPN? Private Internet Access encrypts your internet traffic and uses a safe protected IP. It also works on both your computer and smartphone. Check it out today at privateinternetaccess.com/pravda")

@client.command()
async def slap(ctx, member : discord.Member):
  responses=["https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956",
"https://media1.tenor.com/images/3fd96f4dcba48de453f2ab3acd657b53/tenor.gif?itemid=14358509",
"https://media1.tenor.com/images/74db8b0b64e8d539aebebfbb2094ae84/tenor.gif?itemid=15144612",
"https://media1.tenor.com/images/4a6b15b8d111255c77da57c735c79b44/tenor.gif?itemid=10937039",
"https://media1.tenor.com/images/dcd359a74e32bca7197de46a58ec7b72/tenor.gif?itemid=12396060",
"https://media1.tenor.com/images/d14969a21a96ec46f61770c50fccf24f/tenor.gif?itemid=5509136",
"https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif?itemid=7958720",
"https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943",
"https://media1.tenor.com/images/89309d227081132425e5931fbbd7f59b/tenor.gif?itemid=4880762"]
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url=f"{random.choice(responses)}")
  await ctx.send(f"{member.mention} got slapped by "+ctx.message.author.mention, embed=embed)
  
@client.command(aliases=["simpdetector", "simp"])
async def simprate(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% a simp.")

@client.command(aliases=["miku"])
async def suzuka(ctx):
  embed=discord.Embed(color=0xff1d8e)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906632/peach%20bot/aYJ8x3E_oa8fvb.png")
  await ctx.send(embed=embed)

@client.command()
async def braindamage(ctx):
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906657/peach%20bot/9RGxJ2c_yjjjlx.png")
  await ctx.send(embed=embed)

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
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906693/peach%20bot/ILczO3H_mvlyg4.png")
  await ctx.send(embed=embed)
  embed=discord.Embed(color=0x800080)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906712/peach%20bot/CnvQbWF_ofyjwz.jpg")
  await ctx.send(embed=embed)
  embed=discord.Embed(color=0x800080)
  embed.set_image(url="https://cdn.discordapp.com/attachments/617112983901962260/716897276617949334/unknown.png")
  await ctx.send(embed=embed)
  embed=discord.Embed(color=0x800080)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906739/peach%20bot/9YNxywz_cm8k03.png")
  await ctx.send(embed=embed)

@client.command()
async def mochi(ctx):
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906851/peach%20bot/ze6Wn0w_ligvre.jpg")
  await ctx.send(embed=embed)
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906874/peach%20bot/mEESSOZ_zznx5a.png")
  await ctx.send(embed=embed)

@client.command(aliases=["gay"])
async def gayrate(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% gay")

@client.command(aliases=["overwatch"])
async def ice(ctx):
  embed=discord.Embed(color=0xd7fffe)
  embed.set_image(url="https://media1.tenor.com/images/31e9558485e1c445420b81096d7c9f12/tenor.gif?itemid=7349756")
  await ctx.send(embed=embed)

@client.command(aliases=["loli"])
async def lolirate(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% loli")

@client.command(aliases=["chii"])
async def champii(ctx):
 embed=discord.Embed()
 embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613906967/peach%20bot/afpUzr5_kz3eon.jpg")
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

@client.command()
async def help(ctx):
 embed=discord.Embed(title="Bot's code: https://github.com/champiix/bot", description="IMPORTANT\n``petition``\nFun\n``8ball``, ``coinflip|cf``, ``copypasta``, ``dice|roll``, ``horny|hornyrate``, ``gay|gayrate``, ``hug``, ``hackerman``, ``kill``,  ``kiss``,  ``lolirate``,  ``simp|simprate``,  ``slap``,``pat``, ``pedo|pedorate``,``sus``,``avatar``,``server``, ``liability``, ``lesbian``, ``filipino``\nModeration\n ``ban``,  ``mute``,  ``clear``,  ``kick``,  ``unmute``\nCustom Commands\n``alike``,  ``braindamage``,  ``champii``,  ``culprits``,  ``eesti``,  ``ice``, ``manifesto``,  ``mochi``,  ``miku``,  ``pravda``,  ``t``, ``snowy``,``zen``,``reece``,``xeno``,``unimech``\nVPN \n``pia``,  ``nordvpn``,  ``tunnelbear``\nBot Stuff\n``repo``,  ``ping``,  ``info``,  ``help (shows this message)``", color=0xF2AD7E)
 embed.set_author(name="Command list",icon_url="https://cdn.discordapp.com/avatars/692360784268754964/b82e34765cbeb04b2566e297b93197b0.png?size=2048")
 await ctx.send(embed=embed)

@client.command()
async def pat(ctx, member : discord.Member):
  pats = ["https://media1.tenor.com/images/da8f0e8dd1a7f7db5298bda9cc648a9a/tenor.gif?itemid=12018819", "https://media1.tenor.com/images/266e5f9bcb3f3aa87ba39526ee202476/tenor.gif?itemid=5518317", "https://media1.tenor.com/images/d3c117054fb924d66c75169ff158c811/tenor.gif?itemid=15471762", "https://media1.tenor.com/images/116fe7ede5b7976920fac3bf8067d42b/tenor.gif?itemid=9200932", "https://media1.tenor.com/images/01a97fee428982b325269207ca22866b/tenor.gif?itemid=16085328", "https://media1.tenor.com/images/291ea37382e1d6cd33349c50a398b6b9/tenor.gif?itemid=10204936", "https://media1.tenor.com/images/5466adf348239fba04c838639525c28a/tenor.gif?itemid=13284057", "https://media1.tenor.com/images/61187dd8c7985c443bf9cd39bc310c02/tenor.gif?itemid=12018805", "https://media1.tenor.com/images/143a887b46092bd880997119ecf09681/tenor.gif?itemid=15177421"]
  embed=discord.Embed(color=0xf4c2c2)
  embed.set_image(url=f"{random.choice(pats)}")
  await ctx.send(f"{member.mention} got a headpat from "+ctx.message.author.mention, embed=embed)

@client.command(aliases=["pedo"])
async def pedorate(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% a pedo")

@client.command()
async def anthem(ctx):
  anthems = ["Расцветали яблони и груши, Поплыли туманы над рекой; Выходила на берег Катюша, На высокий берег, на крутой. Выходила, песню заводила Про степного, сизого орла, Про того, которого любила, Про того, чьи письма берегла. Ой, ты песня, песенка девичья, Ты лети за ясным солнцем вслед, И бойцу на дальнем пограничье От Катюши передай привет. Пусть он вспомнит девушку простую, Пусть услышить, как она поет, Пусть он землю бережет родную, А любовь Катюша сбережет. Расщветали яблони и груши, Поплыли туманы над рекой; Выходила на берег Катюша, На высокий берег, на крутой", "Apples and pears were blossoming Mist on the river floating On the bank Katyusha stepped out On the high steep bank Stepped out, started a song About one grey steppe eagle About her loved one Whose letters she cherished Oh song, maiden's song Fly towards the clear sun And to the warrior on a far away border Bring Katyusha's greeting May he remember this simple maiden And hear her singing May he save our motherland And love, Katyusha will save."]
  embed=discord.Embed(title="the national anthem", description=f"{random.choice(anthems)}", color=0xda0a0a)
  await ctx.send(embed=embed)

@client.command(aliases=["8bal", "9ball"])
async def _9ball(ctx):
  h = ["its 8ball you donut", "learn to spell its 8ball", "are you retarded, its 8ball"]
  await ctx.send(f"{random.choice(h)}")

@client.command()
async def ship(ctx, member : discord.Member):
  await ctx.send(f"{member.mention} loves {ctx.message.author.mention} {random.randint(1,100)}%")

@client.command()
async def snowy(ctx):
  embed=discord.Embed(colour=0x3498DB)
  embed.set_image(url="https://cdn.discordapp.com/attachments/684090883158573109/736150065852317746/unknown.png")
  await ctx.send(embed=embed)

@client.command()
async def zen(ctx):
  embed=discord.Embed()
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907441/peach%20bot/jzjlhz4_m3xbcz.png")
  await ctx.send(embed=embed)
  embed=discord.Embed()
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907492/peach%20bot/RUOWQcY_dyzyp7.png")
  await ctx.send(embed=embed)
  embed=discord.Embed()
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907559/peach%20bot/Jefvl1j_kzbm1p.png")
  await ctx.send(embed=embed)
  embed=discord.Embed()
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907617/peach%20bot/p1OeCRY_gwdthf.png")
  await ctx.send(embed=embed)
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907659/peach%20bot/afZsnyH_jolvxn.png")
  await ctx.send(embed=embed)

@client.command()
async def reece(ctx):
  embed=discord.Embed()
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907121/peach%20bot/aJ2sccg_erd13r.png")
  await ctx.send(embed=embed)
  
@client.command()
async def petition(ctx):
  await ctx.send("https://www.change.org/removeMarfromStylis")

@client.command()
@commands.has_permissions(ban_members=True)
async def prules(ctx):
  embed=discord.Embed(color=0xda0a0a)
  embed.add_field(name="To promote a healthy and organized server, we do require that all of our members abide by the rules. If caught breaking the rules, you can be; a muted from text chats and voice calls, kicked,permanently banned, or in more severe cases, reported to Discord.", value="\n**Rule #1: Respect the community and its members**\nThere is no reason to be outright rude or disrespectful to anyone in this server. Please act civilly and use good judgement.\n\n**Rule #2: No harmful acts to the server or its members**\nHarassment, discriminating other members, and/or threatening the well-being and privacy of other members is strictly prohibited. We want this server to be a clean, friendly environment for all. Phishing, scamming, bullying, spamming, and raiding are also not permitted.\n\n**Rule #3: No NSFW Content**\nAll NSFW content (nudity, intense sexuality, excessive profanity, violence, gore, and any disturbing subject matter) is strictly prohibited on all grounds.\n\n**Rule #4: Use the Discord and its channels accordingly**\nBe sure to utilize each channel for its intended purpose. Don't post anything where it shouldn't be.")
  await ctx.send(embed=embed)
  embed=discord.Embed(color=0xda0a0a)
  embed.add_field(name="Rule #5: No abusing permissions", value="Whether a team member or a fan, please do not abuse your role or admin powers. Doing so will result in instant loss of mod and a potential kick/ban from the server. This also applies to abusing channels and bot commands.\n\n**Note: This server is also in accordance with the Discord Terms of Service and enforces them thoroughly. Anyone caught in violation of the Discord ToS can and will be removed from the server accordingly.**\n\nDiscord Terms of Service: https://discordapp.com/terms\n\nIf you happen to run into any issues while in this server, whether it be a glitch or a server member, please get in contact with a server admin. Thank you!\n\nPermanent Server Invite: https://discord.gg/swnW5GY")
  await ctx.send(embed=embed)

@client.command()
async def xeno(ctx):
  await ctx.send("Officially left competitive Lego Battlefield scene due to how most of people are resentful towards me. Pessimism and hopelessness are the only things I have been involved the last couple months.\nthanks to the people who supported me, a lot.\nEnough, moving to GFX! 🙂")
  embed=discord.Embed()
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907321/peach%20bot/z0bdHZm_y3afly.png")
  await ctx.send(embed=embed)
  embed=discord.Embed()
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907350/peach%20bot/CGG8tDx_pnxrnc.png")
  await ctx.send(embed=embed)

@client.command()
async def sus(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% sus")
  
@client.command()
async def s(ctx):
  embed=discord.Embed()
  embed.add_field(name="hi", value="fuck off пидар 병신")
  await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, *, member: discord.Member=None): # set the member object to None
    if not member: # if member is no mentioned
        member = ctx.message.author # set member as the author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@client.command(aliases=["anonDM"])
async def send_anonymous_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(content) # send whatever in the content to the mentioned user.
    await ctx.send("Message sent.")
# Usage: !send_anonymous_dm @mention_user <your message here>

@client.command(name='server')
async def fetchServerInfo(context):
	guild = context.guild
	
	await context.send(f'Server Name: {guild.name}\nServer Size: {guild.member_count}')

@client.command()
async def sendDM(ctx, member: discord.Member, *, content):
    channel = await member.create_dm() # creates a DM channel for mentioned user
    await channel.send(f"**{ctx.message.author} said:** {content}")
    await ctx.send("Message sent.")
    
@client.command()
async def unimech(ctx):
  await ctx.send("It's sad to see the best aim in PF go, but all good things come to an end right? I guess this is my end, I havne't even hit my prime and my career was over so quick. So sad how much of apussy the mods are. They have the power to ban others, so they ban me because of one fishy fucking clip. I hope every stylis member gets harassed and mocked for being such shit. If I do ever play again, it wont be PF. Unless these shit mods unban me. Which won't happen because I refuse to appeal")

@client.command()
async def women(ctx, member: discord.Member):
  channel = await member.create_dm()
  await channel.send("https://media1.tenor.com/images/17274440b818d32e273ab5aadb88a954/tenor.gif?itemid=18526153")
  await ctx.send("woman moment xd")

@client.command()
async def minecraft(ctx, * role: discord.Role):
  user = ctx.message.author
  role = discord.utils.get(ctx.guild.roles, name="minecraft")
  await user.add_roles(role)
  await ctx.send("you're now minecrafting")
  
@client.command()
async def trouble (ctx):
  embed=discord.Embed()
  embed.set_image(url="https://res.cloudinary.com/du3fxrdqu/image/upload/v1613907283/peach%20bot/gzL8lZY_xm3zry.png")
  await ctx.send(embed=embed)

@client.command()
async def lesbian(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% lesbian.")

@client.command()
async def liability(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% liable")

@client.command()
async def filipino(ctx,member : discord.Member):
  await ctx.send(f"{member.mention} is {random.randint(1,100)}% filipino")
keep_alive()
client.run("token")
