import os 
import time
import webbrowser
from colorama import init, Fore, Back, Style
init()
os.system('cls')




banner = """                                                                       
 _   _ _____ _     ____  _____ ____    ____    _    _   _ ____    _   __  __
| | | | ____| |   |  _ \| ____|  _ \  / ___|  / \  | \ | |  _ \  / \  \ \/ /
| |_| |  _| | |   | |_) |  _| | |_) | \___ \ / _ \ |  \| | | | |/ _ \  \  / 
|  _  | |___| |___|  __/| |___|  _ <   ___) / ___ \| |\  | |_| / ___ \ /  \ 
|_| |_|_____|_____|_|   |_____|_| \_\ |____/_/   \_|_| \_|____/_/   \_/_/\_\ 
"""
print(Fore.GREEN+banner)
print(Fore.MAGENTA+'                         Developped by Sandax'+Fore.YELLOW+'\n                Github : https://github.com/Sandaxxx/ ')

print()
print(Fore.RED+"┌――――――┬―――――――――――――――――――┐")
print("| [1]  | ✶ "+Fore.YELLOW+"request"+Fore.RED+"         |")         
print("| [2]  | ✶ "+Fore.YELLOW+"colorama"+Fore.RED+"        |")         
print("| [3]  | ✶ "+Fore.YELLOW+"urllib3"+Fore.RED+"         |")         
print("| [4]  | ✶ "+Fore.YELLOW+"beautifulsoup4"+Fore.RED+"  |")
print("| [5]  | ✶ "+Fore.YELLOW+"discord-webhook"+Fore.RED+" |")
print("| [6]  | ✶ "+Fore.YELLOW+"pypresence"+Fore.RED+"      |")
print("| [7]  | ✶ "+Fore.YELLOW+"pandas"+Fore.RED+"          |")
print("| [8]  | ✶ "+Fore.YELLOW+"twitchio"+Fore.RED+"        |")
print("| [9]  | ✶ "+Fore.YELLOW+"pyinstaller"+Fore.RED+"     |")
print("| [10] | ✶ "+Fore.YELLOW+"pastebinapi"+Fore.RED+"     |")
print("| [11] | ✶ "+Fore.YELLOW+"tweepy"+Fore.RED+"          |")
print("| [12] | ✶ "+Fore.YELLOW+"flask"+Fore.RED+"           |")
print("| [13] | ✶ "+Fore.YELLOW+"tkinter"+Fore.RED+"         |") 
print("| [14] | ✶ "+Fore.YELLOW+"clipboard"+Fore.RED+"       |")
print("└――――――┴―――――――――――――――――――┘")
print()
print(Fore.YELLOW) 
choice = input("[?] Entrer choice >  ")
print()
os.system('cls')
print()
   

if (choice == "1"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://requests.readthedocs.io/en/latest/ '+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install requests')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "2"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://pypi.org/project/colorama/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install colorama')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "3"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://pypi.org/project/urllib3/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install urllib3')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "4"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://beautiful-soup-4.readthedocs.io/en/latest/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install beautifulsoup4')
        print(Fore.GREEN+'[V] Has Been Installed !')

if (choice == "5"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://pypi.org/project/discord-webhook/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install discord-webhook')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "6"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://qwertyquerty.github.io/pypresence/html/index.html'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install pypresence')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "7"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://pandas.pydata.org/docs/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install pandas')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "8"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://twitchio.dev/en/latest/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install twitchio')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "9"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://pyinstaller.org/en/stable/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install pyinstaller')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "10"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://pypi.org/project/Pastebin/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install pastebinapi')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "11"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://docs.tweepy.org/en/stable/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install tweepy')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "12"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://flask.palletsprojects.com/en/2.2.x/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install flask')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "13"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://docs.python.org/fr/3/library/tk.html'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install tkinter')
        print(Fore.GREEN+'[V] Has Been Installed !')


if (choice == "14"):
    print(Fore.MAGENTA+'[?] DOCUMENTATION > https://pypi.org/project/clipboard/'+Fore.GREEN)
    response = input("[+] INSTALL : Do you Want install ? (yes) ")
    if response == "yes":
        os.system('pip install clipboard')
        print(Fore.GREEN+'[V] Has Been Installed !')
















#else:
#    print('Option/Syntaxe Invalide!')


#################################


