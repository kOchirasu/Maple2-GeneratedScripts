""" 11000492: Nelph """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002158$
        # - Can I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002161$
        # - I've spoken with many people who are frustrated that the court will not be held.
        if pick == 0:
            # $script:0831180407002162$
            # - It must be difficult to explain it to every single person.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002163$
            # - It certainly is, but I understand their frustration. They came all the way here to attend the court, only to have their plans ruined. They're upset and disappointed.
            return 31
        elif self.index == 1:
            # $script:0831180407002164$
            # - Whatever the reason, I still feel personally responsible since I was the one charged with the preparations.
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407002165$
        # - My job is to make sure $npcName:11000075[gender:1]$ and the other members of the royal family have everything they need for their day. I'm always busy, but I take pride in my position and my service to $map:02000025$.
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002166$
            # - Have you been to $map:02000076$? My mother lives there. I really should visit her, but I've been so busy that I haven't had the time since preparations began. 
            return 50
        elif self.index == 1:
            # $script:0831180407002167$
            # - Once my work here is done and I've sorted out all the issues, I'll go and visit her first thing! I've been sending her letters, it's just... she can't see. A disease took her eyesight. Sigh... 
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.CLOSE
        return Option.NONE
