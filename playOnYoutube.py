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
import webbrowser as web

import requests


# =====================================================================================================================#
# this class (along with inside function is to search the user desired string value in youtube and plays it ===========#
# =====================================================================================================================#
class playOnYoutubeClass:

    def playOnYoutubeFunction(self, command):
        open_video = True
        url = f"https://www.youtube.com/results?q={command}"
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == "WEB_PAGE_TYPE_WATCH":
                break
        if lst[count - 5] == "/results":
            raise Exception("No Video Found for this Topic!")

        if open_video:
            web.open(f"https://www.youtube.com{lst[count - 5]}")
        return f"https://www.youtube.com{lst[count - 5]}"
