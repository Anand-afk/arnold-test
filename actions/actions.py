# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

# import rasa.core.tracker_store
# from rasa.shared.core.trackers import DialogueStateTracker
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# import pandas as pd


class ActionSaveConversation(Action):

    def name(self) -> Text:
        return "action_save_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # conversation=tracker.events
        # print(conversation)
        # data = []
        # bot=""
        # user=""
        # for i in range(1,len(conversation)-1):
        #     if conversation[i]['event'] == 'bot':
        #         bot = conversation[i]['text']
        #     elif conversation[i+1]['event'] == 'user':
        #         user = conversation[i+1]['parse_data']['intent']['name']
        #         data.append([bot,user])
        #         bot=""
        #         user=""
        #     else:
        #         continue
        # df = pd.DataFrame(data, columns = ['Bot', 'User'])   
        # df.to_csv('chat.csv',index=False)

        #  import os
        # if not os.path.isfile('chats.csv'):

        #     with open('chats.csv','w') as file:
        #         file.write("intent, bot_reply\n")
        # chat_data=''
        # for i in conversation:
        #     if i['event'] == 'user':
        #         chat_data+=i['parse_data']['intent']['name']+','+i['text']+','
        #         print('user: {}'.format(i['text']))
        #         if len(i['parse_data']['entities']) > 0:
        #             chat_data+=i['parse_data']['entities'][0]['entity']+','+i['parse_data']['entities'][0]['value']+','
        #             print('extra data:', i['parse_data']['entities'][0]['entity'], '=',
        #                   i['parse_data']['entities'][0]['value'])
        #         else:
        #             chat_data+=",,"
        #     elif i['event'] == 'bot':
        #         print('Bot: {}'.format(i['text']))
        #         try:
        #             chat_data+=i['metadata']['utter_action']+','+i['text']+'\n'
        #         except KeyError:
        #             pass
        # else:
        #     with open('chats.csv','a') as file:
        #         file.write(chat_data)
        dispatcher.utter_message("hello anand from Action server")
        return []

