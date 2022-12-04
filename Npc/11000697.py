""" 11000697: Blind Rio """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002813$
        # - ...
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002816$
        # - Mm... Who's there? I can't see you, but I can sense your burning soul.
        if pick == 0:
            # $script:0831180407002817$
            # - What happened?
            return 51
        elif pick == 1:
            # $script:0831180407002818$
            # - What's the $map:65000002$?
            return 52
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002819$
            # - ...Do you mean my eyes? As you can see, I'm blind. I committed a sin so grave that I gave up my eyes in penance.
            return 51
        elif self.index == 1:
            # $script:0831180407002820$
            # - I can tell you want to hear my story. I assume $npcName:11000289[gender:0]$ told you about the arena. That is where you can always find a fair fight. No battles to the death, just competitions of strength.
            return 51
        elif self.index == 2:
            # $script:0831180407002821$
            # - But I killed someone there. It was an accident, and everyone who watched our fight agreed that it was unavoidable, but I couldn't forgive myself.
            return 51
        elif self.index == 3:
            # $script:0831180407002822$
            # - That's why I decided to hide in the darkness. That's all.
            return -1
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002823$
            # - You must be interested in the $map:65000002$. But as its name suggests, it's a dangerous place. Everyone in there is determined to hurt each other in a contest of strength. If you want to join in, you'd better prepare well.
            return 52
        elif self.index == 1:
            # $script:0831180407002824$
            # - The $map:65000002$ is a battleground in which up to 10 warriors battle each other for points, and whoever beats more competitors than the others wins. When you beat another warrior, you get points. When you are beaten, you lose them.
            return 52
        elif self.index == 2:
            # $script:0831180407002825$
            # - Since so many warriors fight each other at the same time, sometimes things get really chaotic. The winner might not be the strongest of them all, but the smartest.
            return 52
        elif self.index == 3:
            # $script:0831180407002826$
            # - It's always good to test your strength, but be careful not to let your excitement get the best of you. That's all I have to tell you. Be on your way.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.NEXT
        elif (self.state, self.index) == (51, 2):
            return Option.NEXT
        elif (self.state, self.index) == (51, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.NEXT
        elif (self.state, self.index) == (52, 2):
            return Option.NEXT
        elif (self.state, self.index) == (52, 3):
            return Option.CLOSE
        return Option.NONE
