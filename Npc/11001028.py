""" 11001028: Mett """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 51, 52])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003507$
        # - Welcome.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003510$
        # - You look healthy. I wish I could be as free as you. 
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003511$
            # - I wasn't always like this. I had... an accident. 
            return 40
        elif self.index == 1:
            # $script:0831180407003512$
            # - Ah well, no point in regrets. I just wish there was a way to turn back time. 
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003513$
            # - Eh? You've brought the $item:30000320$! With $npcName:24000615$ gone and $item:30000320$ in hand, I can finally complete my research! 
            return 50
        elif self.index == 1:
            # $script:0831180407003514$
            # - Please add the $item:30000320$ back to the alpha chrono-controller over there to reactivate it.
            return -1
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003515$
            # - Eh? You've brought the $item:30000321$! With $npcName:24000615$ gone and $item:30000321$ in hand, I can finally complete my research! 
            return 51
        elif self.index == 1:
            # $script:0831180407003516$
            # - Please add the $item:30000321$ back to the beta chrono-controller over there to reactivate it.
            return -1
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003517$
            # - Eh? You've brought the $item:30000322$! With $npcName:24000615$ gone and $item:30000322$ in hand, I can finally complete my research! 
            return 52
        elif self.index == 1:
            # $script:0831180407003518$
            # - Please add the $item:30000322$ back to the delta chrono-controller over there to reactivate it.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.CLOSE
        return Option.NONE
