#!/usr/bin/env python
import urllib
import re
import threading


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def fetchpage(link):
    return urllib.urlopen(link).read()

def check1(link):
    url = 'http://downorisitjustme.com/res.php?url=' + link
    rsp = parse('appears to be .+\<b\>(.+\!)\<\/b\>\<\/font\>', fetchpage(url), 'DownOrIsItJustMe')
    
def check2(link):
    url = "http://is-it-down.com/" + link
    rsp = parse('.+\<\/a\> seems (.+) \! \<\/div\>',fetchpage(url), 'Is-It-Down')

def check3(link):
    url = "http://www.downforeveryoneorjustme.com/" + link 
    rsp = parse('\<\/a\>\[\<\/span\> is|looks]? (.+) from', fetchpage(url), 'DownForEveryoneOrJustMe')

def report(site, status):
    ''' Site for website name, status for online or offline '''
    if status == 'online':
        print bcolors.WARNING + "[+] %s = " % site + bcolors.ENDC + bcolors.OKBLUE + "ONLINE!" + bcolors.ENDC 
    elif status == 'offline':
        print bcolors.WARNING + "[-] %s = " % site + bcolors.ENDC + bcolors.FAIL + "OFFLINE!" + bcolors.ENDC

def parse(pattern,text,site):
    ''' To Find with RegEx (pattern) within the (text) '''
    pat = re.compile(pattern)
    rsp = str(pat.findall(text)).strip("[']!").lower()
    ''' Verbose mode, uncomment the following line '''
    #print '%s => %s' % (site, rsp)
    if rsp == 'up' or rsp == 'online':
        report(site, 'online')
    elif rsp == 'down' or rsp == 'offline':
        report(site, 'offline')

def main(cmdarg):
    threads = []
    threads.append(threading.Thread(target=check1, args=(cmdarg,)))
    threads.append(threading.Thread(target=check2, args=(cmdarg,)))
    #threads.append(threading.Thread(target=check3, args=(cmdarg,)))
    
    for i in threads:
        i.start()
    # check1(cmdarg)
    # check2(cmdarg)
    # check3(cmdarg)

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and '.' in sys.argv[1]:
        print"[+] " + bcolors.OKBLUE + "Up " + bcolors.ENDC + "or " + bcolors.FAIL + "Down?" + bcolors.ENDC
        print"[+] Checking" + bcolors.OKGREEN + " %s" % sys.argv[1] + bcolors.ENDC + " on multiple websites"
        main(sys.argv[1])
        
    elif len(sys.argv) == 1:
        print"[+] Up or Down?"
        print"[+] Check online or offline status of a website"
    elif len(sys.argv) == 2 and 'h' or 'help' in sys.argv[1]:
        print"[+] " + bcolors.OKBLUE + "Up " + bcolors.ENDC + "or " + bcolors.FAIL + "Down?" + bcolors.ENDC
        print"[ Usage ] uod site.com"
        print"[+] Check Online or Offline Status of a website"