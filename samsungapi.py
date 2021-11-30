
import sys
import os
import logging
import wakeonlan

sys.path.append('../')

from samsungtvws import SamsungTVWS

class SamsungAPI():
    
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        self.samsung_ip = 'IP HERE' #2.4d
        self.samsung_mac = 'MAC ADDRESS HERE'
        self.samsung_token = 'TOKEN HERE'
        self.port = 8002
        
        
        
        self.tv = SamsungTVWS(self.samsung_ip, port= self.port, token = '26897790')
        
        wakeonlan.send_magic_packet(self.samsung_mac, ip_address= self.samsung_ip, port= 8002)


    def commandShortcut(self, shortcut, method):
        if (shortcut != '' and method != ""):
            wakeonlan.send_magic_packet(self.samsung_mac, ip_address= self.samsung_ip, port= 8002)
            mt = getattr(self.tv, method)()
            getattr(mt, shortcut)()
            shortcut = ''
            method = ''
            

    
 












