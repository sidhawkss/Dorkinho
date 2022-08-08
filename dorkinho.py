#!/usr/bin/env python3
# By sidhawks
import json
import webbrowser
import sys
import requests

chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe %s'

def list_dorks():
   with open("./dorks.json","r") as file:
      counter = 0
      file = json.load(file)
      names = (list(file.keys()))
      for name in names:
         print(name) 

def select_dork(name_dork, url):
   print(f"Name: {name_dork} \nURL:  {url}")
   with open("./dorks.json","r") as file:
      counter = 0
      file = json.load(file)
      names = (list(file.keys()))
      while counter < len(names):
         if (name_dork == list(file.keys())[counter]): 
            print(str(file[names[counter]]).format(url))
         counter += 1

def all_requests(url):
   with open("./dorks.json","r") as file:
      counter = 0
      file = json.load(file)
      names = (list(file.keys()))
      while counter < len(names):
         req = str(file[names[counter]]).format(url)
         req_vrfy = requests.get(req)
         if(len(req_vrfy.text) > 4000):
            print(req)
            webbrowser.open(req)
         req_vrfy.close()
         counter += 1

if __name__ == "__main__":
   try:
      if str(sys.argv[1]) == "list_dorks":
         list_dorks()
      if str(sys.argv[1]) == "all_requests":
         all_requests(str(sys.argv[2]))
      if str(sys.argv[1]) == "select_dork":
         select_dork(str(sys.argv[2]), str(sys.argv[3]))
   except:
      
      print(r"""
     ____      U  ___ u   ____      _  __                _   _     _   _     U  ___ u 
    |  _"\      \/"_ \/U |  _"\ u  |"|/ /       ___     | \ |"|   |'| |'|     \/"_ \/ 
   /| | | |     | | | | \| |_) |/  | ' /       |_"_|   <|  \| |> /| |_| |\    | | | | 
   U| |_| |\.-,_| |_| |  |  _ <  U/| . \\u      | |    U| |\  |u U|  _  |u.-,_| |_| | 
    |____/ u \_)-\___/   |_| \_\   |_|\_\     U/| |\u   |_| \_|   |_| |_|  \_)-\___/  
     |||_         \\     //   \\_,-,>> \\,-.-,_|___|_,-.||   \\,-.//   \\       \\    
    (__)_)       (__)   (__)  (__)\.)   (_/ \_)-' '-(_/ (_")  (_/(_") ("_)     (__)   
      
   [*] The usage of the program is: python dorkinho.py OPTION
   
   Options:
            list_dorks                           #List all dorks names. 
            all_dorks_request URL                #Open the browser with all dorks.
            select_dork NAME URL_PARAMETER       #Create one dork.
      """)
