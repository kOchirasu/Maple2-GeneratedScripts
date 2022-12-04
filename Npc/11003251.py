""" 11003251: Einos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0403155707008169$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0403155707008170$
        # - We must uncover the secret of darkness before it claims any more lives.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0526174607008529$
        # - In search of $itemPlural:20000045$, are you?
        if pick == 0:
            # $script:0526174607008530$
            # - Do you have any $itemPlural:20000045$ for me?
            return 41
        elif pick == 1:
            # $script:0526174607008531$
            # - How do I make the crystal react?
            return 42
        return -1

    def __41(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0526174607008532$
        # - Here you go. The crystal should react to this.
        return -1

    def __42(self, pick: int) -> int:
        # $script:0530154407008539$
        # - Take the $item:20000045$ to the crystal, then press space.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0530154407008540$
        # - One $item:20000045$ is enough, I think. You don't need any more.
        return -1

    def __60(self, pick: int) -> int:
        # $script:0530154407008541$
        # - We must uncover the secret of darkness before it claims any more lives.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
