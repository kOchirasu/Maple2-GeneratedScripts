""" 11004332: Lanemone """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1102172107011635$
        # - Hm...
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1010140307011563$
        # - Mm?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1102172107011636$
        # - I sense something powerful. Something... wrong.
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011564$
            # - Hey, you!
            return 30
        elif self.index == 1:
            # $script:1010140307011565$
            # - Long time no see.
            return 30
        elif self.index == 2:
            # $script:1010140307011566$
            # - I wasn't expecting to run into you here.
            if pick == 0:
                # $script:1010140307011567$
                # - What brings you here?
                return 40
            return -1
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011568$
            # - Well, that geezer—erm, Mr. $npcName:11004233[gender:0]$ sent me here.
            return 40
        elif self.index == 1:
            # $script:1010140307011569$
            # - The Frontier Foundation caught wind of something quite unexpected here on this continent that warranted investigation.
            return 40
        elif self.index == 2:
            # $script:1010140307011570$
            # - Traces of lapenta energy!
            return 40
        elif self.index == 3:
            # $script:1010140307011571$
            # - But I suppose you already knew that.
            return 40
        elif self.index == 4:
            # $script:1010140307011572$
            # - You should be careful. There's no telling what kinds of dangers lurk in this land.
            if pick == 0:
                # $script:0111232407012699$
                # - You too. Take care of yourself.
                return 50
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0111232407012700$
        # - Oh, you don't have to worry about me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.NEXT
        elif (self.state, self.index) == (40, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
