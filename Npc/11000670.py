""" 11000670: Misplaced Book """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002728$
        # - <font color="#909090">(One of these books seems out of place.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002729$
        # - No, no! I don't want to go back in there!
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407002730$
        # - Hey! Did you just throw me on the ground? 
        if pick == 0:
            # $script:0831180407002731$
            # - How did you end up on the bookshelf?
            # TODO: goto 21
            # TODO: gotoFail 22
            return 22
        return -1

    def __21(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002732$
        # - A stupid monster brought me back here. Please, you've got to take me with you!
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407002733$
        # - Your bag is full! Make some room for me, will ya?
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407002734$
        # - <font color="#909090">(You always remember to put books back where you found them... right?)</font>
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        return Option.NONE
