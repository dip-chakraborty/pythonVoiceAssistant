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
import json

# =====================================================================================================================#
# import dependencies (internal files) ================================================================================#
# =====================================================================================================================#
from interactiveModule import interactiveClass

# =====================================================================================================================#
# instantiating task related runtime objects ==========================================================================#
# =====================================================================================================================#
initialRun = False
interactiveClassObj = interactiveClass()


# =====================================================================================================================#
# main class to load the voice assistant and to understand if she has met the user before or this is the first time ===#
# =====================================================================================================================#
class assistantLoaderClass:

    # =================================================================================================================#
    # below function assistantLoaderFunction checks for the assistanceLoader.json file in the same directory where ====#
    # this scripts exists. ============================================================================================#
    # If the file is not present, voice assistant assumes that she is interacting to the user for the very first time =#
    # and asks for boss name, gender and a name to call herself. As per the name or gender of the boss, the assistant =#
    # calls the user accordingly al-through the lifecycle. If the file is present, it means the user has interacted ===#
    # before and calls the user accordingly al-through the lifecycle ==================================================#
    # =================================================================================================================#
    def assistantLoaderFunction(self):
        try:
            initialRun = False
            with open("assistanceLoader.json", mode='r', encoding='utf-8') as f:
                data = json.load(f)
                bossName = data['bossName']
                bossGender = data['bossGender']
                assistantName = data['assistantName']
        except:
            initialRun = True
            interactiveClassObj.interactiveTalk(
                'hi! seems we are meeting for the first time! please answer these following questions')

            interactiveClassObj.interactiveTalk('What should I call you? ')
            bossName = input('What should I call you? ')

            interactiveClassObj.interactiveTalk('If you won\'t mind, what is your gender? ')
            bossGender = input('If you won\'t mind, what is your gender? ')

            interactiveClassObj.interactiveTalk('What would you like to call me? ')
            assistantName = input('What would you like to call me? ')

            if bossGender.lower() == 'male':  # if boss is male, assistant calls him as 'sir'
                bossGender = 'sir'
            elif bossGender.lower() == 'female':  # if boss is female, assistant calls him as 'mam'
                bossGender = 'mam'

            interactiveClassObj.interactiveTalk('Thank you {}'.format(bossGender))

            with open("assistanceLoader.json", mode='w', encoding='utf-8') as outfile:
                dictionary = {
                    "bossName": bossName,
                    "bossGender": bossGender,
                    "assistantName": assistantName
                }
                json_object = json.dumps(dictionary, indent=4)
                outfile.write(json_object)

        if initialRun == True:
            interactiveClassObj.welcomeMessege(bossName, bossGender, assistantName)
        elif initialRun == False:
            interactiveClassObj.interactiveTalk('{} is online again {}'.format(assistantName, bossGender))

        return bossName, bossGender, assistantName
