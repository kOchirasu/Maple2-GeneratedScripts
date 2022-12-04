""" 11004266: Nine """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011207$
        # - Breathe in. Breathe out. Stare at the sea. Yes, yes, it's coming back to me now. You've taught me a valuable lesson again today, ocean.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011208$
            # - Breathe in. Breathe out. Stare at the sea. Yes, yes, it's coming back to me now. You've taught me a valuable lesson again today, ocean.
            return 10
        elif self.index == 1:
            # $script:0911203207011209$
            # - Yes, ocean, you're right. I must start over with a heart of gratitude. I must devote myself to my training!
            if pick == 0:
                # $script:0911203207011210$
                # - Hiiiii! What are you doing?
                return 11
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:0911203207011211$
        # - I am gazing upon the great ocean and filling my heart with peace. I thought the spirit of rock had died within me, but after discussing it with the sea, I realize it had just gone on a little break.
        if pick == 0:
            # $script:0911203207011212$
            # - What happened?
            return 12
        return -1

    def __12(self, pick: int) -> int:
        # $script:0911203207011213$
        # - My hands still tremble when I think back upon that day... It was the Maple rock festival, and thousands watched as I made a terrible mistake in the middle of my song. Since then, I've never been able to play that part right.
        if pick == 0:
            # $script:0911203207011214$
            # - And the ocean is helping you with that...
            return 13
        return -1

    def __13(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011215$
            # - Yes! Thanks to the ocean's wise advice, I am once again filled with the spirit of rock. Can't you see it shining in my eyes?
            return 13
        elif self.index == 1:
            # $script:0911203207011216$
            # - Come to my next concert, and you'll see for yourself that I've been transformed by the sea.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.NEXT
        elif (self.state, self.index) == (13, 1):
            return Option.CLOSE
        return Option.NONE
