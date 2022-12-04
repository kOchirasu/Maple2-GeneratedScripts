""" 11004274: Cheche """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011259$
        # - What a wonderful, joyous day!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0911203207011260$
        # - What a wonderful, joyous day!
        if pick == 0:
            # $script:0911203207011261$
            # - What are you so happy about?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011262$
            # - Every day is a joy! I was sent up here because I was scared of the desert monsters, and at first, I was scared of being so high up, too... But I've adjusted!
            return 11
        elif self.index == 1:
            # $script:0911203207011263$
            # - I'm overjoyed to be in such a safe place. Now I have friends and don't need to be scared of any monsters!
            return 11
        elif self.index == 2:
            # $script:0913152507011309$
            # - Stay positive, and good fortune will follow! Never forget that, human!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.CLOSE
        return Option.NONE
