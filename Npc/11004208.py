""" 11004208: Tumtum """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0806045807010658$
        # - What is it?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0806045807010659$
        # - The mush before you is merely a facsimile of his mushyness. The real $npc:11004213[gender:1]$ is actually luxuriating inside the castle.
        if pick == 0:
            # $script:0806045807010660$
            # - A facsimile?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0806045807010661$
        # - Fake. A fraud. A phony. See the way he bounces around? It's really just an inflatable balloon rigged up to make noises.
        if pick == 0:
            # $script:0806045807010662$
            # - That's a pretty lifelike balloon.
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0806045807010663$
        # - I know, right? You can touch him, if you want. Just don't pop him. These things are expensive.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
