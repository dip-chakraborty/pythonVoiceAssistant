# =====================================================================================================================#
# script   : runAndSplitTasks.py                                                                                       #
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
import datetime

import pyjokes
import speech_recognition as sr
import wikipedia

from cityWeatherDataExtractor import cityWeatherDataExtractorClass
# =====================================================================================================================#
# import dependencies (internal files) ================================================================================#
# =====================================================================================================================#
from interactiveModule import interactiveClass
from openSoftware import openSoftwareClass
from playOnYoutube import playOnYoutubeClass
from searchInternet import searchInternetClass
from sendEmail import sendEmailClass

# =====================================================================================================================#
# instantiating task related runtime objects ==========================================================================#
# =====================================================================================================================#
interactiveClassObj = interactiveClass()
playOnYoutubeClassObj = playOnYoutubeClass()
searchInternetClassObj = searchInternetClass()
openSoftwareObj = openSoftwareClass()
cityWeatherDataExtractorObj = cityWeatherDataExtractorClass()
sendEmailObj = sendEmailClass()
listener = sr.Recognizer()


# =====================================================================================================================#
# main class to understand the voice command and split tasks accordingly ==============================================#
# =====================================================================================================================#
class runAndSplitTasksClass:

    def runAssistant(self, command):

        # =============================================================================================================#
        # browser based assistance ====================================================================================#
        # =============================================================================================================#

        # play the command on youtube.com
        if 'play' in command:
            interactiveClassObj.interactiveTalk('Okay! trying to play it on youtube')
            playOnYoutubeClassObj.playOnYoutubeFunction(command)

        # do a google search on command
        elif 'search' in command:
            interactiveClassObj.interactiveTalk('Okay! searching..')
            searchInternetClassObj.searchInternetFunction(command)

        # recite from wikipedia
        elif 'who' in command:
            person = command
            person = person.replace('who', '')
            person = person.replace('is', '')
            person = person.replace('are', '')
            info = wikipedia.summary(person, 1)
            interactiveClassObj.interactiveTalk(info)

        # =============================================================================================================#
        # general interaction =========================================================================================#
        # =============================================================================================================#
        elif 'i love you' in command:
            interactiveClassObj.interactiveTalk('Hmmmm..I will think about it')
        elif 'joke' in command:
            interactiveClassObj.interactiveTalk('Sure!' + pyjokes.get_joke())

        # =============================================================================================================#
        # software handling interaction ===============================================================================#
        # =============================================================================================================#
        elif 'open software' in command:
            command = command.replace('open', '')
            command = command.replace('software', '')
            interactiveClassObj.interactiveTalk('Okay, trying to open' + command)
            openSoftwareObj.openSoftwareFunction(command)

        # =============================================================================================================#
        # date/time/weather interaction ===============================================================================#
        # =============================================================================================================#
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            interactiveClassObj.interactiveTalk('It is now ' + time)

        elif 'date' in command:
            date = datetime.datetime.now().strftime('%d %B %Y %A')
            interactiveClassObj.interactiveTalk('It is now ' + date)

        elif 'weather' in command:
            city = cityWeatherDataExtractorObj.cityNameExtractorFunction(command)
            temperature, pressure, humidity, weather = cityWeatherDataExtractorObj.weatherDataExtractorFunction(city)
            interactiveClassObj.interactiveTalk(
                'current temperature in {} is {:.2f} degree celcius'.format(city, temperature))
            interactiveClassObj.interactiveTalk('atmospheric pressure is {} mercury scale'.format(pressure))
            interactiveClassObj.interactiveTalk('humidity is {} percentage'.format(humidity))
            interactiveClassObj.interactiveTalk('I can say the average weather is {}'.format(weather))

        elif 'temperature' in command:
            city = cityWeatherDataExtractorObj.cityNameExtractorFunction(command)
            temperature, pressure, humidity, weather = cityWeatherDataExtractorObj.weatherDataExtractorFunction(city)
            interactiveClassObj.interactiveTalk(
                'current temperature in {} is {:.2f} degree celcius'.format(city, temperature))
            interactiveClassObj.interactiveTalk('atmospheric pressure is {} mercury scale'.format(pressure))
            interactiveClassObj.interactiveTalk('humidity is {} percentage'.format(humidity))
            interactiveClassObj.interactiveTalk('I can say the average weather is {}'.format(weather))

        # =============================================================================================================#
        # email automator =============================================================================================#
        # =============================================================================================================#
        elif 'email' in command:
            if 'send' in command:
                interactiveClassObj.interactiveTalk('Okay, please type the recipient email address for me')
                recipient = input('recipient email address:')
                interactiveClassObj.interactiveTalk('Thanks! tell me the subject line of the email?')
                try:
                    with sr.Microphone() as source:
                        voice = listener.listen(source)
                        subject = listener.recognize_google(voice)
                        print(subject)
                except:
                    pass
                interactiveClassObj.interactiveTalk('Great! Now tell me short email body?')
                try:
                    with sr.Microphone() as source:
                        voice = listener.listen(source)
                        message = listener.recognize_google(voice)
                        print(message)
                except:
                    pass
                sendEmailObj.sendEmailFunction(recipient, subject, message)
                interactiveClassObj.interactiveTalk('Congrats, your email is sent now!')
