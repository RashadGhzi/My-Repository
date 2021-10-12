from pygame import mixer
import datetime

def get_time():
    return datetime.datetime.now()

def music_loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    print("Water drinking time. 500ml water per glass. \nEnter 'done' to stop the alarm.")
    music_stop = input()
    if music_stop == stopper:
        mixer.music.stop()

def water_log():
    with open("rashad.txt","a") as item:
        item.write(f"You have dranked water at the time of : {str(get_time())}\n")
