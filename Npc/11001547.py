""" 11001547: Vasara Chen """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 20

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0516130207006115$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0531170907006247$
        # - What do <i>you</i> want?
        if pick == 0:
            # $script:0531170907006248$
            # - I've heard stories about you.
            return 30
        return -1

    def __30(self, pick: int) -> int:
        # $script:0531170907006249$
        # - The idiots here have big mouths. Well go on, what did they tell you?
        if pick == 0:
            # $script:0531170907006250$
            # - They say you're impossibly strong.
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0531170907006251$
        # - Strength is relative. If these idiots think I'm strong, it's only because they've never faced true power.
        if pick == 0:
            # $script:0531170907006252$
            # - I know a thing or two about strength.
            return 50
        return -1

    def __50(self, pick: int) -> int:
        # $script:0531170907006253$
        # - I see. If you're that confident, maybe you'll present an actual challenge.
        if pick == 0:
            # $script:0531170907006254$
            # - Not everyone is so quick to believe me.
            return 60
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:0531170907006255$
            # - This one time, I had a match against this bird-man who was on a journey to test his strength. He didn't look much—heck, he looked weaker than most. Nobody took him seriously.
            return 60
        elif self.index == 1:
            # $script:0531170907006256$
            # - But when he stepped into that ring, he tore through his opponents like they were made of paper. Even I couldn't do better than draw against him. He taught me not to judge a book by its cover.
            if pick == 0:
                # $script:0531170907006257$
                # - You think I'm like that bird guy?
                return 70
            return -1
        return -1

    def __70(self, pick: int) -> int:
        if self.index == 0:
            # $script:0531170907006258$
            # - Hah! No, if anything, you're more like <i>me</i>. There's a certain electricity in the air around fighters like you and I. Most people can't even sense it. But the strong can always recognize each other.
            return 70
        elif self.index == 1:
            # $script:0531170907006260$
            # - Of course, you can also be strong without knowing how to fight. The only way to <i>really</i> know someone is to face them in the ring. I don't know about you, but I'm looking forward to our fight.
            #   <font color="#909090">(The air around him grows heavy and terrifying.)</font>
            if pick == 0:
                # $script:0607145407006337$
                # - Face me in the ring.
                return 80
            return -1
        return -1

    def __80(self, pick: int) -> int:
        # $script:0531170907006263$
        # - That's the plan... Can't wait.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.NEXT
        elif (self.state, self.index) == (70, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (80, 0):
            return Option.CLOSE
        return Option.NONE
