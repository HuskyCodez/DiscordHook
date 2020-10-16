import requests, threading, os, time, ctypes
from random import randint

lock = threading.Lock()
sent = 1
rcolor = randint(1, 16777215)

def Spammer(webhook):
    global sent
    content={
       "username": user,
       "avatar_url": "https://toppng.com/uploads/preview/nuke-png-11553998200wx5xfo50cx.png",
       "embeds": [
           {
                "author": {
                    "username": "NUKED LOL",
                    "url": None,
                    "icon_url": "https://toppng.com/uploads/preview/nuke-png-11553998200wx5xfo50cx.png"
             },
             "title": "FAT NOOB",
             "description": spammsg,
             "color": rcolor
            }
        ]
    }
    r = requests.post(webhook, json=content)
    if r.status_code == 204:
        lock.acquire()
        print (f'Sent count: {sent}')
        sent += 1
        lock.release()
    else:
        pass

if __name__ == "__main__":
    ctypes.windll.kernel32.SetConsoleTitleW("Webhook spammer -HuskyCodez :)")
    webhook = input('Webhook URL?: ')
    user = input("Webhook username?: ")
    spammsg = input("Text to spam?: ")
    print()
    while True:
        for i in range(10):
            threads = threading.Thread(target=Spammer, args=(webhook,))
            threads.start()