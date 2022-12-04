""" 11001391: Yadi """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005391$
        # - $npcName:11001392[gender:1]$, are you okay?
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1223165107005574$
            # - Our parents didn't want us, so why do <i>you</i> care?
            return 40
        elif self.index == 1:
            # $script:1223165107005575$
            # - They left us. Said we were cursed. I don't want to talk about it.
            return 40
        elif self.index == 2:
            # $script:1223165107005576$
            # - It's my job to keep $npcName:11001392[gender:1]$ safe now. She's all the family I've got.
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:1227015507005606$
        # - $npcName:11001392[gender:1]$! I'm sorry! Please... Please, say something!
        return -1

    def __60(self, pick: int) -> int:
        # $script:0201104007005864$
        # - $npcName:11001392[gender:1]$, I'm so glad! Sniff...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
