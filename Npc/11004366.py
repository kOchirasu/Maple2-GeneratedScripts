""" 11004366: Mia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109213607011777$
        # - I doubt you understand the joys of a freshly-baked cake. And the holidays are the perfect time for perfect cakes!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109213607011778$
        # - I do love baking, you know. It's one of my little personal joys. And there's nothing like baking for your family over the holidays.
        if pick == 0:
            # $script:1120173007011852$
            # - Do you like cake?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1120173007011853$
        # - What a ridiculous question. I <i>love</i> cake. And I love it so much that I cannot tolerate cakes that disappoint me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        return Option.NONE
