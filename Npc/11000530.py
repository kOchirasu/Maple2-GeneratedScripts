""" 11000530: Schwanda """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002276$
        # - Can I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002277$
            # - I mostly paint portraits. Would you like to know why?
            return 10
        elif self.index == 1:
            # $script:0831180407002278$
            # - Because the most beautiful thing in the world is people! That's why I like painting them. 
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002279$
            # - Would you like to know when I started painting?
            return 20
        elif self.index == 1:
            # $script:0831180407002280$
            # - Well, that's... I don't know. Do you remember when you started eating food on your own? Or when you spoke your first word?
            return 20
        elif self.index == 2:
            # $script:0831180407002281$
            # - Picking up a brush was as natural to me as picking up a spoon. I was born to paint. I don't need to know exactly when I started doing it.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.NEXT
        elif (self.state, self.index) == (20, 2):
            return Option.CLOSE
        return Option.NONE
