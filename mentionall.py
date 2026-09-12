import os
import logging
import asyncio
import random
from telethon import Button, TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

try:
    api_id = int(os.environ.get("APP_ID", 0))
except ValueError:
    api_id = 0

api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")

if not api_id or not api_hash or not bot_token:
    LOGGER.error("Lütfen APP_ID, API_HASH ve TOKEN değişkenlerini eksiksiz ayarlayın!")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []
tekli_calisan = []

emj = ['😇','🥰','😎','🤩','😍','👾','🤡','🥳','😻','😼','😽','💋','👸','🤴','🎅🏻','🤶','🧞‍♀️','🧞','🧞‍♂️','🧜‍♀️','🧜','🧚‍♀️','🧚','👑','💍','🕶','🐶','🐱','🐭','🐹','🐰','🦊','🐻','🐼','🐨','🐯','🦁','🐮','🐷','🐽','🐸','🐵','🙈','🙉','🙊','🐒','🐣','🐥','🦅','🐝','🦋','🐞','💐','🌹','🥀','🌺','🌸','🌼','🌻','⭐️','🌟','✨','⚡️','🔥','🌈','☃️','🍫','💅','🐺','🍕','☕','🧸','👩‍🦰','🎮','☄️','🌙','🦕','👨🏻‍✈️','🥶','🍿','👀','💀','💟','♥️','💘','💝','💗','💙','💛','🖤','🤑','⚡','😈','🎊','💤','✊','👩‍🎨','🧕','🏵️','🍂','🍁','🌾','🌱','🌿','🍃','☘️','🍀','🌵','🌴','🌳','🌲','🏞️','🌪️','⛄','❄️','🏔️','🌋','🙋','👩‍💼','🧓','🧔','💃','🕺','🪐','🦄','🐢','🐁','🦉','🐓','🕊️','🦢','🦩','🦈','🐬','🐋','🐳','🐟','🐠','🦚','🐡','🦐','🦞','🦀','🦑','🐙','🦂','🕷️','🕸️','🐜','🦗','🦟','🍓','🍒','🍎','🍉','🍊','🥭','🍍','🍋','🍇','🥝','🍐','🥥','🌶️','🍄','🍔','🧆','🥙','🍧','🍨','🍦','🥧','🍰','🍮','🎂','🧁','🍭','🍬','🍩','🍺','🍻','🥂','🍾','🍷']

cumle = ['Üzümlü kekim ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu pandam 🐼', 'Ay parem ✨', 'Ballı lokmam ✨', 'Bebişim 🥰', 'Lale 🌷', 'Zambak ⚜', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare ✨', 'Reyhan 🌷', 'Kaktüs ⚜️', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği ✨', 'Tweety ⚜️', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨']

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan, tekli_calisan
  if event.chat_id in anlik_calisan:
      anlik_calisan.remove(event.chat_id)
  if event.chat_id in tekli_calisan:
      tekli_calisan.remove(event.chat_id)
  await event.respond("İşlem Başarılı Bir Şekilde Durduruldu ❌")

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Kedytagger**, Grup veya kanaldaki neredeyse tüm üyelerden bahsedebilirim ★\nDaha fazla bilgi için **/bilgi** komutunu kullanın.",
                    buttons=(
                      [
                         Button.url('➕ BENİ GRUBA EKLE ➕ ', 'http://t.me/KedytaggerBot?startgroup=a')
                      ],
                      [
                         Button.url('📣 Grubumuz', 'https://t.me/TansiyonRuhu_Tr'),
                         Button.url('👮 Sahip', 'https://t.me/thisonetete'),
                         Button.url('✨ Resmi Kanal', 'https://t.me/kedytagger'),
                      ]
                    ),
                    link_preview=False
                   )

@client.on(events.NewMessage(pattern="^/bilgi$"))
async def help(event):
  helptext = "**Kedytagger Yardım Menüsü**\n\nKomut: /utag \nBu komutu, başkalarına bahsetmek istediğiniz metinle birlikte kullanabilirsiniz.\n\n`/utag Günaydın!`\n\nDiğer komutlar:\n- `/etag`: Emoji ile etiketler.\n- `/itag`: Özel isimlerle etiketler.\n- `/tektag`: Üyeleri tek tek etiketler.\n- `/cancel`: Devam eden etiketlemeyi durdurur."
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('➕ BENİ GRUBA EKLE ➕', 'http://t.me/KedytaggerBot?startgroup=a')
                      ],
                      [
                         Button.url('📣 Grubumuz', 'https://t.me/TansiyonRuhu_Tr'),
                         Button.url('👮 Sahip', 'https://t.me/thisonetete'),
                         Button.url('✨ Resmi Kanal', 'https://t.me/kedytagger'),
                      ]
                    ),
                    link_preview=False
                   )

@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanılabilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if event.sender_id not in admins:
    return await event.respond("__Yalnızca yöneticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg is None:
        return await event.respond("__Eski mesajlar için üyelerden bahsedemem!__")
  else:
    return await event.respond("__Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir metin verin!__")
    
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      if event.chat_id not in anlik_calisan:
        return
      usrnum += 1
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      if event.chat_id not in anlik_calisan:
        return
      usrnum += 1
      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg.id)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/itag ?(.*)"))
async def etag(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanılabilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if event.sender_id not in admins:
    return await event.respond("__Yalnızca yöneticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg is None:
        return await event.respond("__Eski mesajlar için üyelerden bahsedemem!__")
  else:
    return await event.respond("__Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      if event.chat_id not in anlik_calisan:
        return
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      if event.chat_id not in anlik_calisan:
        return
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg.id)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def nick(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("__Bu komut gruplarda ve kanallarda kullanılabilir.!__")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if event.sender_id not in admins:
    return await event.respond("__Yalnızca yöneticiler hepsinden bahsedebilir!__")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg is None:
        return await event.respond("__Eski mesajlar için üyelerden bahsedemem!__")
  else:
    return await event.respond("__Bir mesajı yanıtlayın veya başkalarından bahsetmem için bana bir metin verin!__")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      if event.chat_id not in anlik_calisan:
        return
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      if event.chat_id not in anlik_calisan:
        return
      usrnum += 1
      usrtxt += f"[{random.choice(emj)}](tg://user?id={usr.id}) "
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg.id)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def tektag(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu komutu gruplar ve kanallar için geçerli❗️**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if event.sender_id not in admins:
    return await event.respond("**Bu komutu sadece yöneticiler kullanabilir 〽**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = await event.get_reply_message()
    if msg is None:
        return await event.respond("**Önceki mesajı etiketleyemem!**")
  else:
    return await event.respond("**İşleme başlamam için sebep yazın..**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      if event.chat_id not in tekli_calisan:
        return
      usrnum += 1
      usrtxt = f"**[{usr.first_name}](tg://user?id={usr.id})**"
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      if event.chat_id not in tekli_calisan:
        return
      usrnum += 1
      usrtxt = f"[{usr.first_name}](tg://user?id={usr.id})"
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg.id)
        await asyncio.sleep(2)
        usrnum = 0

print(">> Kedytagger çalışıyor 🚀 <<")
client.run_until_disconnected()
           
