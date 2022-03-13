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
import speech_recognition as sr

# =====================================================================================================================#
# import dependencies (internal files) ================================================================================#
# =====================================================================================================================#
from assistantLoader import assistantLoaderClass
from runAndSplitTasks import runAndSplitTasksClass

# =====================================================================================================================#
# instantiating task related runtime objects ==========================================================================#
# =====================================================================================================================#
runAndSplitTasksClassObj = runAndSplitTasksClass()
listener = sr.Recognizer()

assistantLoaderClassObj = assistantLoaderClass()
bossName, bossGender, assistantName = assistantLoaderClassObj.assistantLoaderFunction()


# =====================================================================================================================#
# This orderTheAssistant function is the trigger point of the whole voice assistant. this loop gets executed until and #
# unless the user stops the code.                                                                                      #
# Future aspect - stop the voice assistant using voice command is in scope                                             #
# =====================================================================================================================#
def orderTheAssistant():
    try:
        with sr.Microphone() as source:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if assistantName in command:
                print(command)
                command = command.replace(assistantName, '')
                runAndSplitTasksClassObj.runAssistant(command)
    except:
        pass


# =====================================================================================================================#
# This loop keeps the above  orderTheAssistant function always online so that the voice assistant is always at user's  #
# service                                                                                                              #
# Future aspect - stop the voice assistant using voice command is in scope                                             #
# =====================================================================================================================#
while True:
    orderTheAssistant()
