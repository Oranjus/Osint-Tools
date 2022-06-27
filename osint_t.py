#!/usr/bin/env python

import webbrowser
import socket
import os
import sys
sys.path.append('__init__')
import get_ip as ad
import colorama
from colorama import Back, Fore, Style

def main():
    print(f"{Fore.RED}+++++++++++++++++++++++++++++++++++")
    print(f"{Fore.RED}+  {Fore.CYAN}Most important tools to start  {Fore.RED}+")
    print(f"{Fore.RED}+++++++++++++++++++++++++++++++++++\n")
    print(f'{Fore.CYAN}[{Fore.RED}+{Fore.CYAN}] Your Ip Adress:{Fore.RED}',ad.ip())
    n = input(f"{Fore.CYAN}[{Fore.RED}01{Fore.CYAN}] {Fore.CYAN}✔ Tineye\n{Fore.CYAN}[{Fore.RED}02{Fore.CYAN}] {Fore.CYAN}✔ Epieos\n{Fore.CYAN}[{Fore.RED}03{Fore.CYAN}] {Fore.CYAN}✔ Whatsmyname\n{Fore.CYAN}[{Fore.RED}04{Fore.CYAN}] {Fore.CYAN}✔ Instantusername\n\nPlease enter a number: {Fore.RED}")
    if n == '01':
        webbrowser.open('https://tineye.com/')
    if n == '02':
        webbrowser.open('https://epieos.com/')
    if n == '03':
        webbrowser.open('https://whatsmyname.app/')
    if n == '04':
        webbrowser.open('https://instantusername.com/#/')
    elif n <'01' or n > '04':
        print("Please enter valid number")
        
if __name__ == "__main__":
    print(f'''{Fore.CYAN}
               d8b                             
               88P                        d8P  
              d88                      d888888P
  88bd88b d888888   {Fore.CYAN}.d888b, {Fore.RED}d8888b       {Fore.CYAN}?88'  
  {Fore.CYAN}88P'  `d8Ve {Fore.RED}rsi   on1   d8P' ?88      {Fore.CYAN}88P   
 {Fore.RED}d88     88b  ,88b    `?8b 88b  d88      88b   
d88'     `?88P'`88b`?888P' `?8888P'      `?8b                                                                                   
''')
    main()
