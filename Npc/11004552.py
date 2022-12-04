""" 11004552: Chocola """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([90, 100, 110])

    def select(self) -> int:
        return 30

    def __30(self, pick: int) -> int:
        # $script:0116132907012728$
        # - Hey, do you need a Valentine chocolate box and some sprinkles? I've got some that I can give you. If you keep making chocolate every day, you'll get a special gift!
        return None # TODO

    def __90(self, pick: int) -> int:
        # $script:0116132907012729$
        # - Hey, do you need a Valentine chocolate box and some sprinkles? I've got some that I can give you. If you keep making chocolate every day, you'll get a special gift!
        if pick == 0:
            # $script:0116132907012730$
            # - Give me a $item:30001287$ and $item:30001288$!
            # TODO: goto 91
            # TODO: gotoFail 92
            return 92
        return -1

    def __91(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0116132907012731$
        # - Here you go! I hope you save some chocolate for me!
        return -1

    def __92(self, pick: int) -> int:
        # $script:0116132907012732$
        # - Oh! Your bag is full. Try again after you make some space in your bag.
        return -1

    def __100(self, pick: int) -> int:
        # $script:0116132907012733$
        # - The best chocolate tastes like a little nugget of love! You've still got some ingredients, so you're good to make more on your own for now. I'll give you more if you need them, of course, but keep in mind that you can only make 3 chocolates a day.
        return -1

    def __110(self, pick: int) -> int:
        # $script:0203161007015990$
        # - $MyPCName$! Do you feel it? Love is in the air!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (90, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (91, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (92, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (100, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (110, 0):
            return Option.CLOSE
        return Option.NONE
