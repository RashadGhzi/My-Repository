from tuts50drink_water_file import music_loop
from tuts50drink_water_file import water_log
from time import time
from datetime import datetime

water_time_start = time()
water_sec = time()
i = 0
start_time = datetime(2020,12,30, 10,00,00).time()
end_time = datetime(2020,12,30, 20,00,00).time()

if (datetime.now().time() >= start_time) & (datetime.now().time() <= end_time):
    print("Your drinking water target is 2.5 litre per day. Your water drink time will start at 10am to 8pm")
    music_loop("Lay Lay Joker Song😈 In Free Fire Version.mp3", "done")
    water_log()
    while True:
        if time() - water_sec > (2*(60*60)):
            music_loop("Lay Lay Joker Song😈 In Free Fire Version.mp3", "done")
            water_log()
            water_sec = time()
            i = i + 1
            if i == 5:
                break