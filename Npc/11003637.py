""" 11003637: Esther """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1109121007009072$
        # - ...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1109121007009073$
        # - ...
        if pick == 0:
            # $script:1109121007009074$
            # - That agent's got to be around here somewhere...
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:1109121007009075$
        # - Hmph. Where does the she get off, sending me a novice like you?
        if pick == 0:
            # $script:1109121007009076$
            # - Guh-whaaaah?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:1109121007009077$
        # - If you can't recognize one of your fellow agents in disguise, then you really are hopeless.
        if pick == 0:
            # $script:1109121007009078$
            # - But... you're a chess piece...
            return 13
        return -1

    def __13(self, pick: int) -> int:
        # $script:1109121007009079$
        # - I have nothing more to say to you, dullard. Go back to $npcName:11003535[gender:1]$ and tell her that you've failed.
        if pick == 0:
            # $script:1109121007009080$
            # - I can't go back empty-handed!
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:1109121007009081$
        # - No need to shout! I'll give you one more chance—let's call it a test. If you're really a bonafide agent, then you surely know where $map:02000153$ is.
        if pick == 0:
            # $script:1109121007009082$
            # - It's in $map:02000001$, the heart of the empire!
            return 15
        elif pick == 1:
            # $script:1109121007009083$
            # - $map:02000100$, of course.
            return 16
        elif pick == 2:
            # $script:1109121007009084$
            # - Dark Wind isn't a place. It's a feeling you carry in your heart.
            return 17
        return -1

    def __15(self, pick: int) -> int:
        # $script:1109121007009085$
        # - Wrong. Begone, dullard.
        if pick == 0:
            # $script:1109121007009086$
            # - Give me another chance!
            return 18
        return -1

    def __16(self, pick: int) -> int:
        # $script:1109121007009087$
        # - I suppose you aren't a <i>complete</i> fool. Very well. The message is "Apple, snake, dinosaur."
        if pick == 0:
            # $script:1109121007009088$
            # - Is that it?
            return 19
        return -1

    def __17(self, pick: int) -> int:
        # $script:1109121007009089$
        # - What nonsense!
        if pick == 0:
            # $script:1109121007009090$
            # - Give me another chance!
            return 18
        return -1

    def __18(self, pick: int) -> int:
        # $script:1109121007009091$
        # - Where is $map:02000153$?
        if pick == 0:
            # $script:1109121007009092$
            # - It's in $map:02000001$, the heart of the empire!
            return 15
        elif pick == 1:
            # $script:1109121007009093$
            # - $map:02000100$, of course.
            return 16
        elif pick == 2:
            # $script:1127144607009321$
            # - Dark Wind isn't a place. It's a feeling you carry in your heart.
            return 17
        return -1

    def __19(self, pick: int) -> int:
        # $script:1109121007009094$
        # - ...
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (15, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (16, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (17, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (18, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (19, 0):
            return Option.CLOSE
        return Option.NONE
