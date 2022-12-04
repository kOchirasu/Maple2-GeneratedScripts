""" 11001699: Tinchai """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0711210007006724$
        # - Mm? Yes?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006903$
        # - How can I help you?
        if pick == 0:
            # $script:0727223007006904$
            # - $npcName:11001557[gender:0]$ is a tough teacher.
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006905$
            # - You don't need to tell <i>me</i> that. He's the reason some of our old students left!
            return 40
        elif self.index == 1:
            # $script:0727223007006906$
            # - $npcName:11001557[gender:0]$ cares about only one thing, and that's training. He expects everyone to keep up with him, and the problem with that should be obvious.
            return 40
        elif self.index == 2:
            # $script:0727223007006907$
            # - I will say, he has a talent for crushing confidence, and that's important when you get arrogant students. His heart's in the right place, it's just... cold and unfeeling, you know?
            return 40
        elif self.index == 3:
            # $script:0727223007006908$
            # - If you ask him why all those students left, he'd tell you they were too soft. Even if he's right, he's not helping them by driving them away!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.CLOSE
        return Option.NONE
