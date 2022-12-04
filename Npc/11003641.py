""" 11003641: Ain """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009124$
        # - Hey hey hey!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009125$
        # - You here to jam, my friend? Let your inner songbird free!
        if pick == 0:
            # $script:1109121007009126$
            # - ♬There's someone that I seek! And I don't have all week! ♬
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009127$
        # - Ow ow ow, my ears! Did someone hit your songbird with a hammer?
        if pick == 0:
            # $script:1109121007009128$
            # - I... I think I'm gonna cry...
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009129$
        # - Don't be like that, $male:man,female:lady$. Here, I know something what'll cheer you right up.
        if pick == 0:
            # $script:1109121007009130$
            # - Oh?
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009131$
        # - I've got a message for our fabulous friend, $npcName:11003535[gender:1]$. "The unbreakable link between heart and song!"
        if pick == 0:
            # $script:1109121007009132$
            # - Okay...
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009133$
        # - Cheer up. You probably just had a frog in your throat, friend.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.CLOSE
        return Option.NONE
