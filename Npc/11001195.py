""" 11001195: Pat """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1016202007004194$
        # - This place is dry, hot, and unbearably loud. It is absolutely <i>the worst</i>. 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1016202007004197$
        # - I must've been out of my mind when I agreed to come here. Hmm? And just who are you supposed to be? Wait, did my wise little owl send here?
        if pick == 0:
            # $script:1016202007004198$
            # - Your what?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1016202007004200$
        # - I'm talking about my beautiful muse! The brains behind our Educational programming, Joanna, of course. <i>Whooo</i>~ else?
        if pick == 0:
            # $script:1016210507004215$
            # - But what was that with the owl thing?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1016202007004201$
        # - Owls are smart. It's just a cute nickname, honey. Get over yourself. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        return Option.NONE
