""" 11000633: Caron """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002562$
        # - How may I help you?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002566$
        # - You're touring $map:02000124$, are you? Stick to the route, then. You wouldn't want to mess with some of these prisoners.
        if pick == 0:
            # $script:0831180407002567$
            # - What kinds of offenses have these prisoners committed?
            return 41
        elif pick == 1:
            # $script:0831180407002568$
            # - Can they get their sentences reduced?
            return 42
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002569$
            # - They've spoken lies or slander about certain people or places, publicly supported or attacked public groups, or used chat, displays, UGC, or character names to offend others.
            return 41
        elif self.index == 1:
            # $script:0831180407002570$
            # - Of course, one doesn't get thrown into prison for committing these offenses just once. They're given multiple chances to redeem themselves first. If they still refuse to see the error of their ways and keep making the same mistakes, then they will receive punishment from $npcTitle:11000514[gender:1]$ and Judge $npcName:11000514[gender:1]$.
            return -1
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002571$
            # - $npcName:11000514[gender:1]$'s punishment can make their life in Maple World very difficult. But if they prove how sorry they are, they can have their sentence reduced.
            return 42
        elif self.index == 1:
            # $script:0831180407002572$
            # - Pulling weeds in the prison yard is one way of proving that, but so far I haven't seen any prisoner pull weeds long enough to have their sentence reduced. It just proves that some people don't change.
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180407002573$
        # - For more information about the prison, please refer to this brochure. Enjoy your tour.
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407002574$
        # - You already have a $item:39000009$. I hope it'll help guide you around $map:02000124$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
