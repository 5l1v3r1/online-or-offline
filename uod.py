#!/usr/bin/env python
import urllib
import re

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check(link):
    # Base link
    url = 'http://downorisitjustme.com/res.php?url='+link
    # Open url and read the HTML content
    x = urllib.urlopen(url).read()
    # Assign regular expression pattern 
    pat = re.compile('appears to be .+\<b\>(.+\!)\<\/b\>\<\/font\>')
    # Find the matching string
    rsp = str(pat.findall(x))
    if rsp == "['Online!']":
        print bcolors.OKBLUE + "[+] ONLINE!" + bcolors.ENDC
    elif rsp == "['Offline!']":
        print bcolors.FAIL + "[-] OFFLINE!" + bcolors.ENDC
    else:
        print"[?] UNKNOWN"

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and '.' in sys.argv[1]:
        print"[+] " + bcolors.OKBLUE + "Up " + bcolors.ENDC + "or " + bcolors.FAIL + "Down?" + bcolors.ENDC
        print"[+] Checking" + bcolors.OKGREEN + " %s" % sys.argv[1] + bcolors.ENDC
        check(sys.argv[1])
        
    elif len(sys.argv) == 1:
        print"[+] Up or Down?"
        print"[+] downorisitjustme.com"
        print"[+] Check online or offline status of a website"
    elif len(sys.argv) == 2 and 'h' or 'help' in sys.argv[1]:
        print"[+] " + bcolors.OKBLUE + "Up " + bcolors.ENDC + "or " + bcolors.FAIL + "Down?" + bcolors.ENDC
        print"[ Usage ] uod site.com"
        print"[+] Check Online or Offline Status of a website"
