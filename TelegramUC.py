from telethon import TelegramClient, sync
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.account import UpdateProfileRequest
import random, time, datetime
from colorama import Fore, init
init()
try:
	from art import *
except:
	pass
import json
with open("settings.json", "r") as file:
	data = json.load(file)
api_id = data["api_id"]
api_hash = data["api_hash"]
try:
	print(Fore.GREEN)
	tprint(f"TelegramUC")
	print(Fore.WHITE)
except:
	print("\nTelegramUC\n")
client = TelegramClient("TelegramUN", api_id, api_hash)
client.start()
print("Using settings.json as settings.")
chars = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(f"Settings: \n  Minutes to wait: {data['minutes']}\n  Max username length: {data['maxlength']} ({int(data['maxlength'])*60} Sec.)\n  api_id: {data['api_id']}\n  {data['api_hash']}\n")
def pickUsername(length):
    password =''""
    for i in range(int(length)):
        password += random.choice(chars)
    return password
def changeus(username):
	try:
		client(UpdateProfileRequest(first_name=username))
		client(UpdateUsernameRequest(username))
	except  Exception as f:
		print(f)
def Start(min):
	changeus(pickUsername(data["maxlength"]))
	print("Started!")
	while True:
		time.sleep(int(min)*60)
		changeus(pickUsername(data["maxlength"]))
		print(f"{Fore.YELLOW}[+]{Fore.WHITE} {datetime.datetime.now().time()} Username changed!")
Start(data["minutes"])