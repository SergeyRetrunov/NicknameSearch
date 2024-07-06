from colorama import Fore, Style, init
import os
import time

init()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    nickname = input(Fore.GREEN + "Nickname: " + Style.RESET_ALL)
    clear_console()

    sites = [
        "https://youtube.com/",
        "https://vk.com/",
        "https://github.com/",
        "https://m.ok.ru/",
        "https://www.tiktok.com/",
        "https://yappy.media/n/",
        "https://www.instagram.com/",
        "https://twitter.com/",
        "https://www.facebook.com/"
    ]

    for site in sites:
        print(Fore.RED + "[+] " + Fore.GREEN + site + Fore.YELLOW + f"{nickname}")
        time.sleep(0.1)
    
    print("")
    input(Fore.RED + "Нажмите ENTER чтобы продолжить...")

if __name__ == "__main__":
    while True:
        main()
        clear_console()
