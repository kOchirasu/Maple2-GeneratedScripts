""" 11000005: Anne """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([80, 90])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000020$
        # - Let's see... So, this book goes... 
        return None # TODO

    def __80(self, pick: int) -> int:
        if self.index == 0:
            # $script:0116174407009791$
            # - Is there anything that you can't learn in a book?
            return 80
        elif self.index == 1:
            # $script:0116174407009792$
            # - Here's a familiar face. Have you finally decided to focus on higher education? I knew you'd come around eventually.
            if pick == 0:
                # $script:0116174407009793$
                # - Actually, I'm here to do some research on Orbis.
                return 81
            return -1
        return -1

    def __81(self, pick: int) -> int:
        if self.index == 0:
            # $script:0116174407009794$
            # - Ah, the floating city. It was world-famous for its astonishing vistas. Unfortunately, it was destroyed in the war.
            return 81
        elif self.index == 1:
            # $script:0116174407009795$
            # - Even though the city is in ruins, the city center still burns to this day. Not a very pleasant place to live these days.
            if pick == 0:
                # $script:0116174407009796$
                # - What else can you tell me about it?
                return 82
            return -1
        return -1

    def __82(self, pick: int) -> int:
        # $script:0116174407009797$
        # - That depends. What, specifically, do you want to know?
        if pick == 0:
            # $script:0116174407009798$
            # - If Orbis is still on fire, where is the heat coming from?
            return 83
        return -1

    def __83(self, pick: int) -> int:
        if self.index == 0:
            # $script:0116174407009799$
            # - Ah, now that is a curious question! I think I read something about that once...
            return 83
        elif self.index == 1:
            # $script:0116174407009800$
            # - In Orbis, the floating city, a very special cave exists. A cave where magma flows endlessly.
            if pick == 0:
                # $script:0116174407009801$
                # - Do you know where the cave is?
                return 84
            return -1
        return -1

    def __84(self, pick: int) -> int:
        # $script:0116174407009802$
        # - No, but it shouldn't be too hard for me to find out. Actually getting to Orbis, however, is a fool's errand. I doubt anybody could survive there for long.
        if pick == 0:
            # $script:0116174407009803$
            # - It's a good thing I'm not just anybody.
            return 85
        return -1

    def __85(self, pick: int) -> int:
        # $script:0116174407009804$
        # - Hopelessly reckless, as usual. I'll tell you where to go, but that's it. I'll have nothing more to do with this.
        if pick == 0:
            # $script:0116174407009805$
            # - Thank you for your time.
            return 86
        return -1

    def __86(self, pick: int) -> int:
        # $script:0116174407009806$
        # - Don't mention it. Please. You'll forgive me for not seeing you off...
        return -1

    def __90(self, pick: int) -> int:
        # $script:0504174607009860$
        # - Is there nothing you can't learn from a book?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (80, 0):
            return Option.NEXT
        elif (self.state, self.index) == (80, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (81, 0):
            return Option.NEXT
        elif (self.state, self.index) == (81, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (82, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (83, 0):
            return Option.NEXT
        elif (self.state, self.index) == (83, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (84, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (85, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (86, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (90, 0):
            return Option.CLOSE
        return Option.NONE
