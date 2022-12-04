""" 11004088: Rainsong Fairy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0622133907010301$
        # - A cold and rainy day, like when we met.
        #   His eyes, his love, I never will forget...
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010302$
            # - A cold and rainy day, like when we met.
            #   His eyes, his love, I never will forget...
            return 10
        elif self.index == 1:
            # $script:0622133907010303$
            # - I see a wand'rer, hail! Be welcome here.
            #   This is Ellosylva, the Fairy's Tear.
            if pick == 0:
                # $script:0622133907010304$
                # - That's a sad name.
                return 31
            return 10
        elif self.index == 2:
            # $script:0625134307010363$
            # - Once a fairy falls in love, she never forgets her lover, even after they've gone to the place where we cannot follow...
            return 10
        elif self.index == 3:
            # $script:0625134307010364$
            # - I broke the rules and fell in love. I first met him here in $map:02000042$. It still smells like him...
            return 10
        elif self.index == 4:
            # $script:0625134307010365$
            # - We were happy together, but it couldn't last. And now, I can never see him again...
            return 10
        elif self.index == 5:
            # $script:0622133907010309$
            # - He told me that my song made him think of the rain. That is why I sing here—to remember him. But, no matter how cheerfully I try to sing, it always comes out sad...
            if pick == 0:
                # $script:0625134307010366$
                # - It's a beautiful song.
                return 37
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0622133907010305$
        # - We fairies oft wear smiles bright and hale,
        #   but in this rain, I share my pain, my tale.
        if pick == 0:
            # $script:0622133907010306$
            # - What's your story?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0622133907010308$
        # - A human's heart I held in hand, and mine
        #   in his. But human lives are short and I
        #   was left behind when it came to be his time.
        return -1

    def __37(self, pick: int) -> int:
        # $script:0625134307010367$
        # - Thank you, traveler. I like to think that he's out there, somewhere, still listening to me. Come see me again whenever you want to hear me sing.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.NEXT
        elif (self.state, self.index) == (10, 4):
            return Option.NEXT
        elif (self.state, self.index) == (10, 5):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (37, 0):
            return Option.CLOSE
        return Option.NONE
