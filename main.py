#https://github.com/BOlaerts/ESP32-2432s028
from machine import SPI, Pin
import ili934xnew
from JPEGdecoder import jpeg
import requests
import time
import json
import gc
import ustruct

spi=SPI(1, baudrate=32000000, mosi=Pin(13, Pin.OUT), sck=Pin(14, Pin.OUT), miso=Pin(12, Pin.IN))
display = ili934xnew.ILI9341(spi=spi, cs=Pin(15), dc=Pin(2), rst=Pin(0), w=320, h=240, r=0)
display.init()
backlight = Pin(21, Pin.OUT)
backlight.value(1)

from JPEGdecoder import jpeg

TG_CHAT_ID = "391279145"
TG_BOT_TOKEN = "6641369508:AAFaHZuCqeXc0ctMC4T_U9XL4I6J6nYgU6M"

BASE_URL = f"https://api.telegram.org/bot{TG_BOT_TOKEN}"
BASE_FILE_URL = f"https://api.telegram.org/file/bot{TG_BOT_TOKEN}"

QUALITY = 90

class Update:
    id: int
    text: str
    photo: bytes

def download_photo(file_id: str):
    resp = requests.get(f"{BASE_URL}/getFile?file_id={file_id}")
    file_meta = json.loads(resp.text)
    file_path = file_meta["result"]["file_path"]
    resp.close()
    gc.collect()
    resp = requests.get(f"{BASE_FILE_URL}/{file_path}")
    res = resp.content
    resp.close()
    del resp
    gc.collect()
    return res

def get_last_update(offset: int) -> Update:
    # resp = requests.get(f'{BASE_URL}/getUpdates?chat_id={TG_CHAT_ID}&limit=1&offset={offset + 1}&allowed_updates=["message"]')
    # result = json.loads(resp.text)["result"]
    # resp.close()
    # if len(result) == 0:
    #     return None
    # obj = result[0]
    # TODO delete
    obj = {
         "update_id":843720807,
         "message":{
            "message_id":3,
            "from":{
               "id":391279145,
               "is_bot": False,
               "first_name":"Raphael",
               "last_name":"K",
               "username":"TheGarkine",
               "language_code":"en"
            },
            "chat":{
               "id":391279145,
               "first_name":"Raphael",
               "last_name":"K",
               "username":"TheGarkine",
               "type":"private"
            },
            "date":1706607297,
            "photo":[
               {
                  "file_id":"AgACAgIAAxkBAAMDZbjCwTAznJsPOm6Sj8hrJl3A0jYAAl_RMRvjhshJkonYElcHz6kBAAMCAANzAAM0BA",
                  "file_unique_id":"AQADX9ExG-OGyEl4",
                  "file_size":976,
                  "width":51,
                  "height":90
               },
               {
                  "file_id":"AgACAgIAAxkBAAMDZbjCwTAznJsPOm6Sj8hrJl3A0jYAAl_RMRvjhshJkonYElcHz6kBAAMCAANtAAM0BA",
                  "file_unique_id":"AQADX9ExG-OGyEly",
                  "file_size":12827,
                  "width":180,
                  "height":320
               },
               {
                  "file_id":"AgACAgIAAxkBAAMDZbjCwTAznJsPOm6Sj8hrJl3A0jYAAl_RMRvjhshJkonYElcHz6kBAAMCAAN4AAM0BA",
                  "file_unique_id":"AQADX9ExG-OGyEl9",
                  "file_size":60076,
                  "width":450,
                  "height":800
               },
               {
                  "file_id":"AgACAgIAAxkBAAMDZbjCwTAznJsPOm6Sj8hrJl3A0jYAAl_RMRvjhshJkonYElcHz6kBAAMCAAN5AAM0BA",
                  "file_unique_id":"AQADX9ExG-OGyEl-",
                  "file_size":78830,
                  "width":720,
                  "height":1280
               }
            ]
         }
      }
    u = Update()
    u.id = obj["update_id"]
    message = obj["message"]
    if "text" in message:
        u.text = message["text"]
    if "photo" in message:
        for p in message["photo"]:
            if p["height"] == QUALITY:
                u.photo = download_photo(p["file_id"])
                break
    return u

gc.collect()
# r = requests.get("http://thegarkine.github.io")
u = get_last_update(1)
with open("image.jpg", "wb") as f:
    f.write(u.photo)

import math

def rendering_callback(x, y, color):
    b = color & 0xFF
    g = color>>8 & 0xFF
    r = color>>16 & 0xFF
    ratio = display.height / QUALITY
    start_x = math.floor(x*ratio)
    start_y = math.floor(y*ratio)
    display.fill_rectangle(start_x, start_y, math.ceil(ratio), math.ceil(ratio),ili934xnew.color565(r,g,b))
    #display.pixel(x,y,ili934xnew.color565(r,g,b))

def df():
  s = os.statvfs('//')
  return ('{0} MB'.format((s[0]*s[3])/1048576))

# jpeg("image.jpg", callback=rendering_callback, quality = 1).render()


# jpeg(u.photo, callback=callback).render()

# latest_update_id = 0

# while True:
#     update = get_last_update(latest_update_id)
#     print(update.id)
#     latest_update_id = update.id
#     time.sleep(1)
#     break