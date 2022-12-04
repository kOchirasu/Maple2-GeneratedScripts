""" 11000523: Eve """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002234$
        # - Welcome.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002237$
            # - After my father passed away, I found his journal among his things. My father was the guardian of the Blue Lapenta, and he wanted $npcName:11000064[gender:0]$ to be his successor. So I knew.
            return 30
        elif self.index == 1:
            # $script:0831180407002238$
            # - I knew there was no way $npcName:11000064[gender:0]$ did what the others said he did.
            return 30
        elif self.index == 2:
            # $script:0831180407002239$
            # - I'm glad the truth finally came out and everything is back to normal, even though $npcName:11000044[gender:0]$ hasn't paid for his crimes.
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407002240$
        # - Being with $npcName:11000064[gender:0]$ reminds me of the gorilla pie that we used to bake together when we were young.
        if pick == 0:
            # $script:0831180407002241$
            # - What could gorilla pie possibly be...?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002242$
        # - It's one of those pies topped with walnuts, almonds, and blueberries. When $npcName:11000064[gender:0]$ and I first made it, it was so bumpy and ugly that it looked like a gorilla. Why? What did you <i>think</i> it was?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.NEXT
        elif (self.state, self.index) == (30, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
