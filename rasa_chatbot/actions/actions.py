# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from hmac import trans_5C
from typing import Any, Text, Dict, List
from matplotlib.style import available

from rasa_sdk.types import DomainDict
from rasa_sdk.events import (
    SlotSet,
    EventType,
)

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import UserUtteranceReverted

from actions.rooms_manager import RoomsManager


class ActionSetCheckIn(Action):

    def name(self) -> Text:
        return "action_set_check_in"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
    
        date = next(tracker.get_latest_entity_values("date"), None)

        return [SlotSet("check_in", date)]


class ActionSetCheckOut(Action):

    def name(self) -> Text:
        return "action_set_check_out"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
    
        date = next(tracker.get_latest_entity_values("date"), None)

        return [SlotSet("check_out", date)]


class ActionSetAdults(Action):

    def name(self) -> Text:
        return "action_set_adults"
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
    
        number = int(next(tracker.get_latest_entity_values("number"), None))

        if number > 0 and number <= 4:
            return [SlotSet("n_adults", number)]
        else:
            dispatcher.utter_message(template="utter_number_invalid")
            dispatcher.utter_message(template="utter_adults")
            return [UserUtteranceReverted()]


class ActionSetChildren(Action):

    def name(self) -> Text:
        return "action_set_children"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
    
        number = int(next(tracker.get_latest_entity_values("number"), None))

        if number >= 0 and number <= 6:
            return [SlotSet("n_children", number)]
        else:
            dispatcher.utter_message(template="utter_number_invalid")
            dispatcher.utter_message(template="utter_children")
            return [UserUtteranceReverted()]


class ActionSetRooms(Action):

    def name(self) -> Text:
        return "action_set_rooms"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
    
        number = int(next(tracker.get_latest_entity_values("number"), None))

        if number > 0 and number <= 4:
            return [SlotSet("n_rooms", number)]
        else:
            dispatcher.utter_message(template="utter_number_invalid")
            dispatcher.utter_message(template="utter_rooms")
            return [UserUtteranceReverted()]


class ActionCallManager(Action):

    def name(self) -> Text:
        return "action_call_manager"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        n_rooms = tracker.get_slot("n_rooms")

        n_adults = tracker.get_slot("n_adults")
        n_children = tracker.get_slot("n_children")
        print("(DEBUG) Calling manager\n")
        print(f"(SLOTS) adults={n_adults} children={n_children} rooms={n_rooms}\n")
    
        manager = RoomsManager()
        vacancy = manager.find_rooms(n_rooms)
        
        return [SlotSet("vacancy", vacancy)]


class ValidateGuestsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_guests_form"

    async def required_slots(self, domain_slots: List[Text], dispatcher: "CollectingDispatcher",
        tracker: "Tracker", domain: "DomainDict",
    ) -> List[Text]:

        updated_slots = domain_slots.copy()

        a_read = tracker.get_slot("a_read")
        n_adults = tracker.get_slot("n_adults")

        if a_read<n_adults:
            updated_slots.remove("guest_age")
        
        return updated_slots


class ActionCheckGuests(Action):

    def name(self) -> Text:
        return "action_check_guests"

    def get_slots_to_update(self, tracker):
        a_read = tracker.get_slot("a_read")
        c_read = tracker.get_slot("c_read")
        
        n_adults = tracker.get_slot("n_adults")
        n_children = tracker.get_slot("n_children")
        
        guest_type = "adult"
        guest_number = tracker.get_slot("guest_number") 

        if a_read<n_adults: 
            a_read += 1
        else:    
            c_read += 1
            

        if a_read<n_adults: # adult will be read
            continue_guests = True
            guest_number += 1
            
        elif a_read==n_adults and n_children>0 and c_read<n_children: # child will be read
            continue_guests = True
            guest_type = "child"

            if c_read == 0: # reading first child, reset counter
                guest_number = 1
            else:
                guest_number +=1
            
        else: # all adults read and 0 children / all adults read and all children read
            continue_guests = False


        print("(DEBUG) Update\n")
        print(f"(SLOTS) continue={continue_guests} a_read={a_read} c_read={c_read} number={guest_number}\n")
        
        return [SlotSet("continue_guests", continue_guests), SlotSet("a_read", a_read), SlotSet("c_read", c_read),
                    SlotSet("guest_number", guest_number), SlotSet("guest_type", guest_type)]

    def get_slots_to_append(self, tracker):
        names_list = tracker.get_slot("names_list")
        ids_list = tracker.get_slot("ids_list")
        ages_list = tracker.get_slot("ages_list")

        names_list.append(tracker.get_slot("guest_name"))
        ids_list.append(tracker.get_slot("guest_id"))
        ages_list.append(tracker.get_slot("guest_age"))

        print("(DEBUG) Append\n")

        return [SlotSet("names_list", names_list), SlotSet("ids_list", ids_list), SlotSet("ages_list", ages_list)]    


    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        slots_to_update = self.get_slots_to_update(tracker)
        slots_to_append = self.get_slots_to_append(tracker)
        slots_to_reset = [SlotSet("guest_name", None), SlotSet("guest_age", None), SlotSet("guest_id", None)]

        return slots_to_update + slots_to_append + slots_to_reset
      

class ActionUtterReservationInfo(Action):
    def name(self):
        return 'action_utter_reservation_info'

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:

        check_in = tracker.get_slot("check_in")
        check_out = tracker.get_slot("check_out")
        n_rooms = tracker.get_slot("n_rooms")
        
        names_list = tracker.get_slot("names_list")
        ids_list = tracker.get_slot("ids_list")
        ages_list = tracker.get_slot("ages_list")

        message = f"Check-in: {check_in}\nCheck-out: {check_out}\nRooms: {n_rooms}\n\n"

        for i in range(len(names_list)):
            message += f"Guest {i+1}\n"
            message += f"Name: {names_list[i]}\n"
            message += f"ID: {ids_list[i]}\n"
            if ages_list[i]:
                message += f"Age: {ages_list[i]}\n\n"

        dispatcher.utter_message(text=message)
        dispatcher.utter_message(template="utter_goodbye")

        return []