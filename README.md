# Dorkinho 🔵
The author is not responsible for misuse of the tool, use it in good practices like Pentest and CTF OSINT challenges.

![](https://i.imgur.com/xi2UKOE.png)

Dorkinho is a script to list and open dorks in the browser in a fast way, the script open a lot of web pages with dork search, so pay attention in the hardware usage.

## Usage

Execute the `dorkinho.py` script. **If you use a browser different from google chrome, change the PATH in the script**

## Example commands
```bash
#List all dorks name
python dorkinho.py list_all

#Open in browser and list the dorks in the terminal
python dorkinho.py all_dorks_request somesite.com

#Create a dork. You must have use the list_all dork to lookup name of the dork.
python dorkinho.py select_dork newsdetail news.com
```

By SidHawks
