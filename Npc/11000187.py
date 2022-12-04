""" 11000187: Maneh """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000818$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000820$
            # - I want nothing to do with the empress or her army. They were supposed to protect us! Instead everyone was frozen by ice elementals.
            return 20
        elif self.index == 1:
            # $script:0831180407000821$
            # - My granddaughter was one of the victims. If... if the empire had just done something about the shadow gate the moment it opened, my son and his wife would still be here, safe and happy with me. 
            if pick == 0:
                # $script:0831180407000822$
                # - What's the story with the shadow gate?
                return 21
            return -1
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000823$
            # - The Shadow Gate is the entrance to a world of demons who serve the darkness. The empire is trying to keep their evil contained.
            return 21
        elif self.index == 1:
            # $script:0831180407000824$
            # - But I don't know... Closing the Shadow Gate at the cost of innocent lives... Is that really the right way to protect the world?
            return 21
        elif self.index == 2:
            # $script:0831180407000825$
            # - My son and his wife could be still alive somewhere on the other side of the Shadow Gate. If it is closed, I'll never see them again.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.NEXT
        elif (self.state, self.index) == (21, 1):
            return Option.NEXT
        elif (self.state, self.index) == (21, 2):
            return Option.CLOSE
        return Option.NONE
