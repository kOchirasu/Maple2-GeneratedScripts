""" 11000782: Lavor """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002948$
        # - I can see a light shining in your eyes. What can I do for you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002951$
        # - Hey there, young $male:fellow,female:lady$. You look like a traveler. I hope you're making the most of your youth and seeing the world. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
