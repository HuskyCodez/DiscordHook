import requests, threading, os, time, ctypes
from random import randint

lock = threading.Lock()
sent = 1

def Spammer(webhook):
    rcolor = randint(1, 16777215)
    global sent
    if ping == 'y':
        content={
                "content": "@everyone",
                "embeds": [
                    {
                    "title": "GET NUKED LOL",
                    "description": spammsg,
                    "color": 15746887
                    }
                ],
                "username": user
                }
    elif ping == 'n':
        content={
            "embeds": [
                {
                "title": "GET NUKED LOL",
                "description": spammsg,
                "color": 15746887
                }
            ],
            "username": user
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
    ctypes.windll.kernel32.SetConsoleTitleW("Webhook spammer - HuskyCodez :)")
    webhook = input('Webhook URL?: ')
    ping = input('Ping everyone? (y/n): ')
    user = input("Webhook username?: ")
    spammsg = input("Text to spam?: ")
    print()
    while True:
        for i in range(10):
            threads = threading.Thread(target=Spammer, args=(webhook,))
            threads.start()