import time
import threading
from threading import Thread, RLock
import asyncio
import requests
from flask import Blueprint

print("line 5")



views = Blueprint(__name__, "main")



def the_thing():

    time3 = time.gmtime()
    time4 = [time3[3], time3[4], time3[5]]


    the_time = time4
    the_time_in_secs = (the_time[0] * 60 * 60) + (the_time[1] * 60) + (the_time[2])
    how_long_sleep =  25200 - the_time_in_secs


    if how_long_sleep < 0:
        how_long_sleep = 86400 + how_long_sleep


    
    print(f"gmt time - {time4[0]}:{time4[1]}:{time4[2]}     line 24")
    print(f"the time in seconds - {the_time_in_secs}    line 25")


    for i in range(int(how_long_sleep/5)):
        request_ = requests.get("https://bwstats.net")
        print("made request so no sleep (line 855)")
        time.sleep(5)
        print("after time.sleep(line 888)")





    #async def main():
    #    while True:
    #        for i in range(int(how_long_sleep/30)):
    #            #request_ = requests.get("https://tinyurl.com/4mbea2xy")
    #            print("made request so no sleep (line 855)")
    #            await asyncio.sleep(30)
    #            print("after asyncio.sleep(line 888)")



    #loop = asyncio.new_event_loop()
    #asyncio.set_event_loop(loop)
    #loop.run_until_complete(main())





while True:
    the_thing()