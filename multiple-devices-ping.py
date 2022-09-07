#!/usr/bin/env python3

'''
This is script is able to ping two devices and only if both of these devices are not responding, then the system command is executed.
'''

import os
import time

start_over_count = 0

address1 = "2001:db8:cafe::10"
address2 = "2001:db8:cafe::20"

fail1 = 0
fail2 = 0

while True:
    start_over_count += 1
    print("start over count " + str(start_over_count))
    time.sleep(60)
    if fail1 >= 10 & fail2 >= 10:
        os.system("shutdown /s /t 20")
        #os.system("dir")
        break

    #ping_comm1 = os.system('("ping -c1 " + address1) > /dev/null 2>&1')
    #ping_comm2 = os.system('("ping -c1 " + address2) > /dev/null 2>&1')
    ping_comm1 = os.system("ping -n 1 " + address1)
    ping_comm2 = os.system("ping -n 1 " + address2)

    if ping_comm1 != 0:
        fail1 += 1
        #print("fail1 count is: " + str(fail1))
    else:
        #print("ping1 is OK")
        fail1 = 0

    if ping_comm2 != 0:
        fail2 += 1
        #print("fail2 count is: " + str(fail2))
    else:
        #print("ping2 is OK")
        fail2 = 0