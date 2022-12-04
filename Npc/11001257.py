""" 11001257: Moren """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        # TODO: RandomPick 30
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1203001410001288$
        # - How may I help you?
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:1203001410001290$
        # - You said you wanted me to send you where $npcName:11001229[gender:0]$ went, right? Well, that would be an inn on Victoria Island, in the city of Tria. Would you like to go there now?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1203001410001294$
        # - Ever wish you could get somewhere instantaneously? What would you say if I told you I could use a bit of rune magic to send you wherever you want in the blink of an eye?
        if pick == 0:
            # $script:1203001410001295$
            # - Please teleport me!
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:1203001410001296$
            # - You won't believe it 'til it happens! Oh. Um... just a moment. Uh, it seems I don't have enough rune energy on-hand for the teleportation spell.
            return 31
        elif self.index == 1:
            # $script:1203001410001297$
            # - Hmm. You still have things left to do here anyway, don't you? Maybe you should take care of those. I'm not stalling!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.TAKE_BOAT
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        return Option.NONE
