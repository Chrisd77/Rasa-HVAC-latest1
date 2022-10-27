import logging
import json
from datetime import datetime
from typing import Any, Dict, List, Text, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
)

from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from neo4j import GraphDatabase


class ActionMyKB(ActionQueryKnowledgeBase):
    def __init__(self):
        # load knowledge base with data from the given file
        knowledge_base = InMemoryKnowledgeBase("knowledge_base_data.json")

        # overwrite the representation function of the hotel object
        # by default the representation function is just the name of the object
        knowledge_base.set_representation_function_of_object(
            "transmitter", lambda obj: obj["name"] + " (" + obj["category"] + ")"
        )

        super().__init__(knowledge_base)

#
# Neo4j connection credentials
#

graphdb=GraphDatabase.driver(uri="neo4j+s://20ff2f08.databases.neo4j.io",auth=("neo4j","fX7LJJMb7GwCTktE9_3CtihWnX589OYNlYl78OiQwtI"))

session=graphdb.session()

class Neo4jConnection:

    def __init__(self, uri, user, pwd):
        self.__uri = "class Neo4jConnection:"

    def __init__(self, uri, user, pwd):
        self.__uri = "neo4j+s://20ff2f08.databases.neo4j.io"
        self.__user = "neo4j"
        self.__pwd = "fX7LJJMb7GwCTktE9_3CtihWnX589OYNlYl78OiQwtI"
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response

        self.__user = "neo4j"
        self.__pwd = "fX7LJJMb7GwCTktE9_3CtihWnX589OYNlYl78OiQwtI"
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response


uri = "neo4j+s://20ff2f08.databases.neo4j.io"
user = "neo4j"
pwd = "fX7LJJMb7GwCTktE9_3CtihWnX589OYNlYl78OiQwtI"

conn = Neo4jConnection(uri=uri, user=user, pwd=pwd)

entity_type=str('Filter')

#query =  """MATCH (n {label: ('%s')}) RETURN n.definition""" % (entity_type)

#result = conn.query(query)
#print(result)


class ActionsNeo4j(Action):
    def name(self) -> Text:
        return "action_neo4_actions"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> List[EventType]:
        ##Once we have an email, attempt to add it to the database

        entity_type = tracker.get_slot("restaurant")
query =  """MATCH (n {label: ('%s')}) RETURN n.definition""" % (entity_type)

#a =  ActionsNeo4j("equipment")
a = query
a.name()       
        
#result = conn.query(query)

#dispatcher.utter_message(template="utter_confirm_salesrequest")
 #   return []
