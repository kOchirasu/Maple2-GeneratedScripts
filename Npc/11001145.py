""" 11001145: Juko """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0915220707003959$
        # - I'm confused... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0915220707003962$
        # - Mmm... Do you like candy?
        if pick == 0:
            # $script:0915220707003963$
            # - No. I hate candy, because I am a monster.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0915220707003964$
        # - Whaaaat? I'm sure you'd change your mind if you tried my Mom's $item:30000395$. It's awesome!
        if pick == 0:
            # $script:0915220707003965$
            # - That's nice.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0915220707003966$
        # - <font color="#909090">(He whines pitifully)</font>
        #   Just try a piece! I promise you'll love it. My mom also bakes cakes and pies that are crazy good. She's like a <i>witch</i>!
        if pick == 0:
            # $script:0915220707003967$
            # - Anyone can bake.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0915220707003968$
        # - Not like my mom! When I grow up, I'm going to be a culinary wizard, and make snacks just as good as hers. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
