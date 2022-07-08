# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import  datetime 
import datetime as dt


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []
        
class ActionGreet(Action):
    def name(self) -> Text:
        return "action_greet"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
        now = dt.datetime.now()
        today00am = now.replace(hour=00, minute=0, second=0, microsecond=0)
        today12pm = now.replace(hour=12, minute=0, second=0, microsecond=0)
        today04pm = now.replace(hour=16, minute=0, second=0, microsecond=0)
        if today00am < now < today12pm:
          message = 'Good Morning,  I am Reliable - your virtual assistant. How are you today?'
        elif today12pm < now < today04pm:
          message = 'Good Afternoon, I am Reliable - your  virtual assistant. How are you today?'
        else:
          message = 'Good Evening, I am Reliable - your virtual assistant. How are you today?'
        dispatcher.utter_message(message)
        return []
class ActionPolicyDeu(Action):

    def name(self) -> Text:
        return "action_policy_deu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if tracker.slots.get("agent_type", None) == "agent":
            dispatcher.utter_message(
            response="utter_agent"
        )
        else:
            dispatcher.utter_message(
            response="utter_policy_holder"
      )

        return []