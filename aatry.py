from win32com.client import Dispatch

voice = Dispatch("SAPI.SpVoice")

voice.speak("You are luckiest boy in the world")