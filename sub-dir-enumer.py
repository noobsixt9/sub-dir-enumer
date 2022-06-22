import pyfiglet
import sys
import requests
from printy import printy

ascii_banner = pyfiglet.figlet_format("SUB-DIR \n ENUMER.py")
printy(ascii_banner,'n')

if len(sys.argv) > 1:
 opt = int(sys.argv[1])
 wordlist = sys.argv[2]
 target = sys.argv[3]
else:
 opt = False
 wordlist = False
 target = False
if opt != 1 and opt != 2 or  wordlist == False or target == False:
  print("Usage: python3 script.py <1 -direnumer or 2 -subdomain-enumer> <wordlist_path> <taget_url>")
  print("   eg: python3 script.py 1 /usr/share/wordlist/wordlist2.txt tryhackme.com")
elif len(sys.argv) > 4:
    print("Usage: python3 script.py <1 -direnumer or 2 -subdomain-enumer> <wordlist_path> <taget_url>")
    print("   eg: python3 script.py 1 /usr/share/wordlist/wordlist2.txt tryhackme.com")

elif opt == 1 and wordlist != False and target != False:
 print("\nstarted directory enumeration on",target,"with",wordlist,"wordlist...")
 print("\n\n")
 f = open(wordlist,"r")
 dir_list = list(f.read().split("\n"))
 
 for dir in dir_list:
  url = f"http://{target}/{dir}"
  r = requests.get(url)
  if r.status_code != 404:
   print("valid dir: ",url)
  else:
   pass
    
 f.close()
elif opt == 2 and wordlist != False and target != False:
 print("\nstarted subdomain enumeration on",target,"with",wordlist,"wordlist...")
 print("\n\n")
 f = open(wordlist,"r")
 sub_list = list(f.read().split("\n"))
 
 for sub in sub_list:
  url = f"https://{sub}.{target}"
  try:
   r = requests.get(url)
  except requests.ConnectionError:
    pass
  else:
   print("valid domain: ",url)
 
 f.close()


