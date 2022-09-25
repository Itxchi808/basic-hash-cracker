
from hashlib import md5
import colorama
from colorama import Fore
import datetime
colorama.init()

numbr=1

def main(numbr):
    furdiefam = input("Wordlist: ")
    crack = input("MD5 Hash: ")

    f = open(furdiefam,'r')
    list = f.read()
    list = list.split('\n')
    for word in list:
        hashedword = md5(word.encode())
        if hashedword.hexdigest() == crack:
            print(Fore.GREEN+'cracked:'+Fore.WHITE,word)
            print("Tried:",numbr)
            print('End At:',datetime.datetime.utcnow())
            exit()
        else:
            numbr = numbr+1
            print(Fore.RED+'incorrect',numbr,':'+Fore.WHITE,word)
            
        
        
        
        
banner = Fore.RED+"""
 ██░ ██  ▄▄▄        ██████  ██░ ██     ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒   ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██    ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓   ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
 ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒   ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░     ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
 ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   ░          ░░   ░   ░   ▒   ░        ░ ░░ ░ 
 ░  ░  ░      ░  ░      ░   ░  ░  ░   ░ ░         ░           ░  ░░ ░      ░  ░   
                                      ░                           ░               
                                                                   
"""


print(banner+Fore.WHITE)
print('Started At:',datetime.datetime.utcnow())

main(numbr)