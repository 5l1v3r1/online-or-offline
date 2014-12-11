import urllib
import re

def check(link):
    url = 'http://downorisitjustme.com/res.php?url='+link
    x = urllib.urlopen(url).read()
    pat = re.compile('appears to be .+\<b\>(.+\!)\<\/b\>\<\/font\>')
    rsp = str(pat.findall(x))
    if rsp == "['Online!']":
        print"[+] ONLINE!"
    elif rsp == "['Offline!']":
        print"[-] OFFLINE!"
    else:
        print"[?] UNKNOWN"
    
    

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and '.' in sys.argv[1]:
        print"[+] Up or Down?"
        print"[+] Checking %s" % sys.argv[1]
        check(sys.argv[1])
        
    elif len(sys.argv) == 1:
        print"[+] Up or Down?"
        print"[+] downorisitjustme.com"
        print"[+] Check online or offline status of a website"
    elif len(sys.argv) == 2 and 'h' or 'help' in sys.argv[1]:
        print"[+] Up or Down?"
        print"[ Usage ] uod site.com"
        print"[+] Check Online or Offline Status of a website"
