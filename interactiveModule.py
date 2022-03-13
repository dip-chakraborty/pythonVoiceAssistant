# =====================================================================================================================#
# script   : main.py                                                                                                   #
# function : main script to run voice assistant                                                                        #
# date     : 6th March 2022                                                                                            #
# version  : v1.0                                                                                                      #
# =====================================================================================================================#
# modification history                                                                                                 #
# ---------------------------------------------------------------------------------------------------------------------#
# change date |  version  |    changed by    |    change description                                                   #
# ---------------------------------------------------------------------------------------------------------------------#
#             |           |                  |                                                                         #
#             |           |                  |                                                                         #
# =====================================================================================================================#

# =====================================================================================================================#
# import dependencies (packages) ======================================================================================#
# =====================================================================================================================#
import pyttsx3 as tts

# =====================================================================================================================#
# instantiating task related runtime objects ==========================================================================#
# =====================================================================================================================#
ttsengine = tts.init()  # initialize text to speech engine
voices = ttsengine.getProperty('voices')  # check for the types of voices property
ttsengine.setProperty('voice', voices[2].id)  # make a female voice as supported for the assistant
ttsengine.setProperty("rate", 160)  # set the voice playback speed of the assistant


# =====================================================================================================================#
# This interactiveClass is the root of the initial interaction of the voice assistant to the user =====================#
# =====================================================================================================================#
class interactiveClass:

    # =================================================================================================================#
    # If the user is interacting with the voice assistant for the very first time, then only below welcomeMessege func-#
    # tion gets executed as a welcome interaction =====================================================================#
    # =================================================================================================================#
    def welcomeMessege(self, bossname, bossGender, assistantName):
        ttsengine.say(
            'hi {}! My name is {} and i am your digital assistant from now on'.format(bossname, assistantName))
        ttsengine.say('i can help you out automating many tasks {}'.format(bossGender))
        ttsengine.say('so, just order me! I am listening you')
        ttsengine.say('just call me {} from the next time you need any help'.format(assistantName))
        ttsengine.runAndWait()

    # =================================================================================================================#
    # If the user is interacting with the voice assistant not for the first time, then only below interactiveTalk func-#
    # tion gets executed to let the user understand that the voice assistant is ready to take the commands to perform  #
    # any sort of dedicated tasks =====================================================================================#
    # =================================================================================================================#
    def interactiveTalk(self, text):
        ttsengine.say(text)
        ttsengine.runAndWait()
