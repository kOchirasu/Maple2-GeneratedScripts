""" 11000323: Tony """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60, 70])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001300$
        # - How may I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407001303$
        # - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot warrior? 
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407001304$
        # - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot mage? 
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407001305$
        # - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot archer? 
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180407001306$
        # - I hate history the most. There are too many things to remember, heroes and names and... What was the name of that big-shot thief? 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        return Option.NONE
