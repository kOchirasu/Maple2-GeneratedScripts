""" 11004333: Miel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011573$
        # - Hello.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011574$
            # - Hello.
            return 10
        elif self.index == 1:
            # $script:1010140307011575$
            # - My friend. It is pleasant to see your face.
            return 10
        elif self.index == 2:
            # $script:1010140307011576$
            # - This place is beautiful, is it not?
            return 10
        elif self.index == 3:
            # $script:1010140307011577$
            # - I have never before walked such a land, under such a sky... and yet it strikes me as familiar, all the same.
            return 10
        elif self.index == 4:
            # $script:1010140307011578$
            # - Perhaps I am drawing nearer to the answers I seek.
            if pick == 0:
                # $script:1010140307011579$
                # - I'm sure you are!
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        # $script:1010140307011580$
        # - Thank you. Your enthusiasm always lifts my spirits.
        if pick == 0:
            # $script:1010140307011581$
            # - Is $npcName:11001431[gender:0]$ with you?
            return 30
        return -1

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011582$
            # - I asked him to accompany me, but I fear our vulpine friend declined my invitation. Oh, what I might have learned if he was here to aid me...
            return 30
        elif self.index == 1:
            # $script:1010140307011583$
            # - A lack his cutting insight...
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.NEXT
        elif (self.state, self.index) == (10, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        return Option.NONE
