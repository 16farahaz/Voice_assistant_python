from playsound import playsound
import eel
#  play the assitante sound function 
@eel.expose
def playAssistantSound():
    music_dir="www\\assets\\audio\\sound.mp3"
    playsound(music_dir)