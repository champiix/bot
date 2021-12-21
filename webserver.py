from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "PEACH COMMANDS<br><br>Fun:<br>8ball, coinflip|cf, copypasta, woman, dice|roll, horny, gay, simp, loli, pedo, sus, liability, lesbian, filipino, hug, hackerman, pat, kiss, slap, kill<br><br>Moderation:<br>ban, clear, mute, kick, unmute, avatar, server<br><br>Custom commands:<br>alike, braindamage, champii, unimech, eesti, ice, manifesto, mochi, miku, pravda, t, snowy, zen, reece, xeno, unimech, trouble<br><br>VPN:<br>pia, nordvpn, tunnelbear<br><br>Bot info:<br>repo, ping, info, help(leads to this website)"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
