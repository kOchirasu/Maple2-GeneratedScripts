""" 11001555: Valen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0415104107006021$
        # - How may I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0421104907006047$
            # - Tsk. If people keep taking pebbles home as souvenirs, soon the beach will be completely bare.
            return 40
        elif self.index == 1:
            # $script:0421104907006048$
            # - This one time, somebody climbed the hill in the middle of the night to get up close to the whale. Or he tried to, but he lost his grip halfway up and fell. It was a total disaster.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        return Option.NONE
