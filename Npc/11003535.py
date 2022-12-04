""" 11003535: Schatten """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1126150707011924$
        # - I am the shadow that evil fears.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:1126150707011925$
        # - Something on your mind, sweet stuff?
        if pick == 0:
            # $script:1126150707011926$
            # - Who are the Shadow Walkers, exactly?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1126150707011927$
        # - Tsk, tsk. You should be careful about sticking your nose in Shadow Walker business. I'd hate for something to happen to it.
        if pick == 0:
            # $script:1126150707011928$
            # - Well, that's a scary thing to say.
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1126150707011929$
        # - It's for your own good. If you really want to know about us, I'll tell you... when we're a bit <i>closer</i>.
        if pick == 0:
            # $script:1126150707011930$
            # - Uh... If you say so...
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:1126150707011931$
        # - Cheer up, hon. In fact, c'mere and I'll give you a kiss on the cheek!
        if pick == 0:
            # $script:1126150707011932$
            # - That's okay! I just remembered I have to... go... away.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:1126150707011933$
        # - Ha! No need to be shy!
        return -1

    def __40(self, pick: int) -> int:
        # $script:1126150707011934$
        # - Hey there, kitten. Looking to run missions for Dark Wind? I don't think you're ready to handle my business <i>just</i> yet. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        return Option.NONE
