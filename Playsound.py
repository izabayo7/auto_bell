#
# Mongo.java This is a class for playing an audio
# @author Cedric & Souvede
#

from playsound import playsound

class Playsound:
    def __init__(self,path):
        self.path = path
    
    def playSound(self):
       sound_player = playsound(self.path)
        

# #Main execution 
# def main():
#     test_sound = Playsound("./audio/sample.mp3")

#     test_sound.playSound()
    
# main()