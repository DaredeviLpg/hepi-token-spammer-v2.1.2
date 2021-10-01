import threading, os, time, sys, asyncio, json #epik packages
try:
  import requests
except:
  os.system("pip install requests")
  import requests

try:
  import discord
except:
  os.system("pip install discord")
  import discord

try:
  from colorama import Fore, Style
except:
  os.system("pip install colorama")
  from colorama import Fore, Style

try:
  import youtube_dl
except:
  os.system("pip install youtube-dl")
  import youtube_dl

from discord.utils import get
from config import * # star import, if you see a green line just ignore it

os.system("pip install PyNaCl") # only required for vc stuff

with open("tokens.txt", "r") as f:
  tokens = f.read().split("\n")

def clear():
  os.system("cls" if os.name == "nt" else "clear")

clear()

validTokens = []

with open("tokeninfo.json", "r") as f:
  g = json.load(f)

def checkTokens(x):
    r = requests.post('https://discord.com/api/v7/channels/1826/messages', headers={'Authorization':x}, json={'content':x} )
    res= requests.get('https://canary.discordapp.com/api/v6/users/@me', headers={'Authorization':x, 'Content-Type': 'application/json'})
    if res.status_code != 200:
      print(f"{Fore.RED}[- Invalid token] {Fore.RESET}{x}")
    else:
      if 'need to verify' in r.text:
        print(f"{Fore.YELLOW}[* token needs verification] {Fore.RESET}{x}, {res.json()['username']}#{res.json()['discriminator']}")
      else:
        print(f"{Fore.GREEN}[+ Valid token] {Fore.RESET}{x}, {res.json()['username']}#{res.json()['discriminator']}")
        validTokens.append(x)
        data = res.json()
        g[x] = {"user":data["username"]+"#"+data["discriminator"], "email":data["email"]}

epik = f'''
                        {Fore.RED}   ▀▀█▀▀ █▀▀█ █░█ █▀▀ █▀▀▄ 　 █▀▀ █▀▀█ █▀▀█ █▀▄▀█ █▀▄▀█ █▀▀ █▀▀█ 　 ▀█░█▀ █▀█ ░ ▄█░ ░ █▀█ 
                        {Fore.LIGHTRED_EX}   ░░█░░ █░░█ █▀▄ █▀▀ █░░█ 　 ▀▀█ █░░█ █▄▄█ █░▀░█ █░▀░█ █▀▀ █▄▄▀ 　 ░█▄█░ ░▄▀ ▄ ░█░ ▄ ░▄▀ 
                        {Fore.BLUE}   ░░▀░░ ▀▀▀▀ ▀░▀ ▀▀▀ ▀░░▀ 　 ▀▀▀ █▀▀▀ ▀░░▀ ▀░░░▀ ▀░░░▀ ▀▀▀ ▀░▀▀ 　 ░░▀░░ █▄▄ █ ▄█▄ █ █▄▄
{Fore.RESET}'''

options = f'''
{Fore.RED}{Style.BRIGHT}[1]{Fore.RESET} Join/leave servers{Style.RESET_ALL}
  {Fore.LIGHTRED_EX}[1 a]{Fore.RESET} invite all tokens to a guild
  {Fore.LIGHTRED_EX}[1 b]{Fore.RESET} Bypass membership screening
  {Fore.LIGHTRED_EX}[1 c]{Fore.RESET} leave a guild
{Fore.RED}[2]{Fore.RESET} spam
{Fore.RED}[3]{Fore.RESET} mass message reactor
{Fore.RED}[4]{Fore.RESET} nickname changer
{Fore.RED}{Style.BRIGHT}[5]{Fore.RESET} Vc{Style.RESET_ALL}
  {Fore.LIGHTRED_EX}[5 a]{Fore.RESET} join vc
  {Fore.LIGHTRED_EX}[5 b]{Fore.RESET} play in vc
{Fore.RED}{Style.BRIGHT}[6]{Fore.RESET} Downloads{Style.RESET_ALL}
  {Fore.LIGHTRED_EX}[6 a]{Fore.RESET} Download music from yt url
  {Fore.LIGHTRED_EX}[6 b]{Fore.RESET} Download file from url
>'''

print(epik)

print("checking tokens...")

for x in tokens:
  t = threading.Thread(target=checkTokens, args=(x,)).start()

validTokens = validTokens

time.sleep(1)

print("filtering valid tokens...")

time.sleep(1)

def spam(channel,spam_msg,amoun):
  for x in range(int(amoun)):
    for x in validTokens:
      if not embed_spam:
        json = {'content':spam_msg}
      else:
        json = {'content':spam_msg, 'embeds':[embed]}
      res = requests.post(f"https://discord.com/api/v8/channels/{channel}/messages", headers={"authorization":x}, json=json)
      if res.status_code != 200:
        if "are being rate limited" in str(res.json()):
          if len(validTokens) == 1:
            print(f"{Fore.YELLOW}You are being ratelimited{Fore.RESET}, retrying again in: {res.json()['retry_after']}. token: {x}")
            time.sleep(res.json()['retry_after'])
          else:
            print(f"{Fore.YELLOW}the token {x} was ratelimited{Fore.RESET}, messages will be sent with this token when the ratelimit ends. duration: {res.json()['retry_after']}.")
        else:
          print(f"{Fore.RED}couldnt send message{Fore.RESET}, token: {x}")
          print(res.json())
      else:
        print(f"{Fore.GREEN}spam message sent{Fore.RESET}, token: {x}")

def qspam(x,channel,spam_msg,amoun):
      if not embed_spam:
        json = {'content':spam_msg}
      else:
        json = {'content':spam_msg, 'embeds':[embed]}
      res = requests.post(f"https://discord.com/api/v8/channels/{channel}/messages", headers={"authorization":x}, json=json)
      if res.status_code != 200:
        if "are being rate limited" in str(res.json()):
          if len(validTokens) == 1:
            print(f"{Fore.YELLOW}You are being ratelimited{Fore.RESET}, retrying again in: {res.json()['retry_after']}. token: {x}")
            time.sleep(res.json()['retry_after'])
          else:
            print(f"{Fore.YELLOW}the token {x} was ratelimited{Fore.RESET}, messages will be sent with this token when the ratelimit ends. duration: {res.json()['retry_after']}.")
        else:
          print(f"{Fore.RED}couldnt send message{Fore.RESET}, token: {x}")
          print(res.json())
      else:
        print(f"{Fore.GREEN}spam message sent{Fore.RESET}, token: {x}")

def addreaction(channel, mid, reaction):
    for x in validTokens:
      headers={'authorization': x}
      res = requests.put(f"https://discord.com/api/v9/channels/{channel}/messages/{mid}/reactions/{reaction}/@me", headers=headers)
      if res.status_code != 204:
        if "are being rate limited" in res.text:
          print(f"{Fore.YELLOW}You are being ratelimited{Fore.RESET}, retrying again in: {res.json()['retry_after']}. token: {x}")
        else:
          print(f"{Fore.RED}couldnt react to message{Fore.RESET}, token: {x}")
      else:
        print(f"{Fore.GREEN}message reacted{Fore.RESET}, token: {x}")

def changenick(guild, nick):
    for x in validTokens:
      headers = {'authorization':x}
      res = requests.patch(f"https://discord.com/api/v8/guilds/{guild}/members/@me/nick", headers=headers, json={"nick":nick})
      if res.status_code != 200:
        if "are being rate limited" in res.text:
          print(f"{Fore.YELLOW}You are being ratelimited{Fore.RESET}, retrying again in: {res.json()['retry_after']}. token: {x}")
        else:
          print(f"{Fore.RED}couldnt change nickname{Fore.RESET}, token: {x}")
      else:
        print(f"{Fore.GREEN}nickname changed{Fore.RESET}, token: {x}")

if len(validTokens) == 0:
  print("all tokens were invalid.")
  sys.exit()

print(f"{len(validTokens)}/{len(tokens)} were valid.")


for x in validTokens:
  v = validTokens.count(x)
  if v > 1:
    validTokens.remove(x)

with open("filteredtokens.txt", "w") as f:
  f.write("\n".join(validTokens))

bots = []

loop = asyncio.get_event_loop()
for token in validTokens:
  bot = discord.Client(status=discord.Status.idle, activity=discord.Streaming(name=status, url="https://twitch.tv/vissionlol"))
  loop.create_task(bot.start(token, bot=False))
  bots.append(bot)

threading.Thread(target=loop.run_forever).start()

time.sleep(1)
clear()

with open("tokeninfo.json", "w") as l:
  json.dump(g, l, indent=2)

while True:
    print(epik)
    opt = input(options)
    clear()
    if opt == "1 a":
      os.system("python joiner.py")
    if opt == "1 b":
      os.system("python ms_bypasser.py")
    if opt == "1 c":
      guilds = []
      g = input("Guild id\n>")
      for x in bots:
          guild = x.get_guild(int(g))
          guilds.append(guild)
      for guild in guilds:
          try:
            loop = asyncio.get_event_loop()
            loop.create_task(guild.leave())
            loop.run_until_complete("yes")
          except:
            pass
    elif opt == "2":
      speed = input("[1] regular spam\n[2] thread spam\n[3] multithread spam(fastest)\n>")
      clear()
      channel = input("channel id, type m to use multi channel mode.\n>")
      clear()
      ls = []
      if channel == "m":
        while True:
          clear()
          var = input("Channel id, type x to proceed\n>")
          if var != "x":
            ls.append(var)
          else:
            break
      else:
        ls = [channel]
      clear()
      amount = input("amount to spam\n>")
      if speed == '1':
        for channel in ls:
          spam(channel, spam_msg, amount,)
      if speed == '2':
       for xa in range(int(amount)):
        for channel in ls:
          for x in validTokens:
            threading.Thread(target=qspam, args=(x, channel,  spam_msg,amount,)).start()
      if speed == '3':
        threads = []
        rn = int(amount)
        for x in range(rn):
          for channel in ls:
            for g in validTokens:
              t = threading.Thread(target=qspam, args=(g,channel,spam_msg,amount,))
              t.daemon = multithred_daemon
              threads.append(t)
        for x in range(rn):
          threads[x].start()
        for x in range(rn):
          threads[x].join()
      time.sleep(2)
    if opt == "3":
      channel = input("Channel id\n>")
      clear()
      mid = input("Message id\n>")
      clear()
      reaction = input("Emoji, for default emojis use unicode, for custom emojis use name:id\n>")
      threading.Thread(target=addreaction, args=(channel,mid,reaction,)).start()
    if opt == "4":
      guild = input("Guild id\n>")
      clear()
      nick = input("nickname\n>")
      threading.Thread(target=changenick, args=(guild, nick,)).start()
    if opt == "5 a":
        channels = []
        g=int(input("vc channel id\n>")) 
        for x in bots:
          channel = x.get_channel(g)
          channels.append(channel)
        for channel in channels:
          try:
            loop = asyncio.get_event_loop()
            loop.create_task(channel.connect())
            loop.run_until_complete("yes")
            print("vc joined")
          except:
            pass
    if opt == "5 b":
      vcs = []
      gd = input("guild id\n>")
      clear()
      music_list = '\n'.join([f"[{os.listdir('music').index(x)+1}] {x}" for x in os.listdir('music')])
      fp = int(input(f"{music_list}\n>"))
      fp = os.listdir('music')[fp-1]
      for x in bots:
          try:
            vcs.append(get(x.voice_clients, guild=x.get_guild(int(gd))))
          except Exception as e:
            print(e)
            pass
      for vc in vcs:
          try:
            vc.play(discord.FFmpegPCMAudio("music/"+fp))
          except Exception as e:
            print(e)
            pass
    if opt == "6 a":
        clear()
        y = input("Video URL\n>")
        clear()
        ydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3'}], 'outtmpl':f"music/%(title)s.mp3"}
        print("downloading...")
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([y])
        clear()
        print("complete")
        time.sleep(1)
    if opt == "6 b":
      url = input("File URL\n>")
      clear()
      dir = input("directory\n>")
      clear()
      filename = input("File name\n>")
      clear()
      format = input("format\n>")
      f = open(dir+"/"+filename+"."+format, 'wb')
      f.write(requests.get(url).content)
      f.close()
      clear()
      print("complete")
    time.sleep(1)
    clear()
