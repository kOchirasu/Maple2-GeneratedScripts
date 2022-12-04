""" 11004258: Casto """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010976$
        # - It's soooo hot. And I've made no progress on my research. Ugh...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0829171107010977$
        # - It's soooo hot. And I've made no progress on my research. Ugh...
        if pick == 0:
            # $script:0831140807011028$
            # - What are you researching?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0831140807011029$
        # - Oh, not much. Just, you know, the dragon that lives here in $map:02000011$.
        if pick == 0:
            # $script:0831140807011030$
            # - $npcName:23100011$?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0831140807011031$
        # - Maybe. That's what I'm researching. I personally believe that $npcName:23100011$, the legendary dragon, lives here, but I'm searching for proof. You've heard the legend, right?
        if pick == 0:
            # $script:0831140807011032$
            # - Nope! Tell me!
            return 13
        return -1

    def __13(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831140807011033$
            # - Once upon a time, not too far from here, there was a place called the Forest of Wisdom. One day, the fire dragon turned the place into a sea of flame. It was the greatest loss of life in the history of the world. Supposedly, the dragon slumbers somewhere here in $map:02000011$.
            return 13
        elif self.index == 1:
            # $script:0831140807011034$
            # - This area didn't used to be so hot... Not until after the fire dragon went into hiding here.
            return 13
        elif self.index == 2:
            # $script:0831140807011035$
            # - That's my theory, at least. Anyway, if you find anything, let me know. I kind of want to go home now.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.NEXT
        elif (self.state, self.index) == (13, 1):
            return Option.NEXT
        elif (self.state, self.index) == (13, 2):
            return Option.CLOSE
        return Option.NONE
