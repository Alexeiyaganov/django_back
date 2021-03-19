import sys
import time
import argparse
import datetime as dt
import matplotlib.pyplot as plt
from graph import Grafiki
from datetime import datetime
from base import MiBand2
from constants import ALERT_TYPES
import csv 
from bluepy.btle import BTLEException
import os

os.system("rfkill block bluetooth")
os.system("rfkill unblock bluetooth")
time.sleep(3)

MAC = "F2:E5:49:29:DA:D0"

band = MiBand2(MAC, debug=True)
band.setSecurityLevel(level="medium")

graph = Grafiki()


band.authenticate()

print('Print previews recorded data')
band._auth_previews_data_notif(True)
    
start_time = datetime.strptime('01.02.2021 10:59', '%d.%m.%Y %H:%M')
band.start_get_previews_data(start_time)
while band.active:
    band.waitForNotifications(0.1)
recorded_date_time=band.array_date_time    
recorded_steps=band.array_steps
print(recorded_date_time)
print(recorded_steps)
#time.sleep(61)
#graph.set_data_and_date_array(band.array_steps, band.array_date_time)
while 1:
    time.sleep(61)
    try:
        band.disconnect()
        os.system("rfkill block bluetooth")
        os.system("rfkill unblock bluetooth")
        time.sleep(3)
        band = MiBand2(MAC, debug=True)
        band.setSecurityLevel(level="medium")
        band.authenticate()
        band.pkg=0
        band._auth_previews_data_notif(True)
        start_time = datetime.strptime(recorded_date_time[-45], "%d.%m.%Y %H:%M")
        band.start_get_previews_data(start_time)
        while band.active:
            band.waitForNotifications(0.1)
        for i in range(len(band.array_date_time)):
            recorded_date_time.append(band.array_date_time[i])    
            recorded_steps.append(band.array_steps[i])
        print(recorded_date_time)
        print(recorded_steps)
        print("22222222222")

    except BTLEException:
        print("retrying connections")
        #self._debug_print("retrying connections", 10)
        #band.disconnect()
        #os.system("rfkill block bluetooth")
        #os.system("rfkill unblock bluetooth")
        #time.sleep(3)
        #band = MiBand2(MAC, debug=True)
        #band.setSecurityLevel(level="medium")
        #band.authenticate()
        
    
        # вызываем рисовку графиков
    graph.set_data_and_date_array(recorded_steps, recorded_date_time)
    
    



band.disconnect()
