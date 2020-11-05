import json
import googlemaps
import pprint
import time

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

class Point_of_InterestSkill(MycroftSkill):
    def __init__(self):
        super(Point_of_Interest_Skill, self).__init__(name="Point_of_InterestSkill")
        
    def initialize(self):
       # self.load_data_files(dirname(__file__))
        
        point_of_interest_intent = IntentBuilder("Point_of_InterestIntent").require("Point_of_InterestKeyword").build()
        self.register_intent(point_of_interest_intent, self.handle_point_of_interest_intent)
        
        
    def handle_intent(self, message):
        api_key = 'AIzaSyBp25k9LqhGDh4nAIHeFnhu045jrWPnWkg'
        gmaps = googlemaps.Client(key = api_key)

        places_result = gmaps.places_nearby(location= '45.421532,-75.697189', radius = 10000, open_now = False, type = 'gas_station')
        
        for place in places_result['results']:
           my_place_id = place['place_id']
           my_fields = ['name', 'formatted_phone_number', 'type', 'formatted_address']
           place_details = gmaps.place(place_id = my_place_id, fields = my_fields)
           #print(place_details)
           self.speak_dialog("place_details")
           
           
    def stop(self):
        pass

def create_skill():
    return ISSLocationSkill()
