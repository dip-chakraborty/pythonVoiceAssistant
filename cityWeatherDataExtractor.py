# =====================================================================================================================#
# script   : cityWeatherDataExtractor.py                                                                                      #
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
# nltk and spacy libraries are required for this transfer learning ====================================================#
# =====================================================================================================================#
import locationtagger
import requests


# =====================================================================================================================#
# this class (along with inside functions is to search the user desired city's weather ================================#
# =====================================================================================================================#
class cityWeatherDataExtractorClass:

    def cityNameExtractorFunction(self, command):
        sample_text = command.title()
        place_entity = locationtagger.find_locations(text=sample_text)

        # getting all countries place_entity.countries
        # getting all states place_entity.regions
        # getting all cities place_entity.cities

        city = str(place_entity.cities[0])
        return city

    def weatherDataExtractorFunction(self, city):
        api_key = "fd77db0f736b568a0d15177938b1fe5e"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"] - 273
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            return current_temperature, current_pressure, current_humidity, weather_description
        else:
            print("City Not Found ")
