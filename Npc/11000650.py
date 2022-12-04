""" 11000650: Prisoner 170122 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002663$
        # - When can I get out of here?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002667$
        # - Huh? You don't look like an inmate.
        if pick == 0:
            # $script:0831180407002668$
            # - What are you doing?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002669$
        # - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Ugh, I'll grow old before I can pull that many weeds.
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004920$
        # - Huh? You don't look like an inmate.
        if pick == 0:
            # $script:1210061907004921$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1214232707004979$
        # - How do you know <i>that man</i>?
        if pick == 0:
            # $script:1214232707004980$
            # - I'm working with him.
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1214232707004981$
        # - Hm... Yes, there is something special about you. What brings you here, then?
        if pick == 0:
            # $script:1214232707004982$
            # - I'm here on $npcName:11001231[gender:0]$'s behalf.
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:1214232707004983$
        # - He's just as impatient as the supervisor, eh? Well, if you're here on business, you better talk to him.
        if pick == 0:
            # $script:1214232707004984$
            # - Who is this supervisor?
            return 54
        return -1

    def __54(self, pick: int) -> int:
        # $script:1214232707004985$
        # - $npcName:11000651[gender:0]$. But he doesn't talk to nobody without the password. That's the rule. And, to keep things nice and secure, we change it every three days.
        if pick == 0:
            # $script:1214232707004986$
            # - What's the password?
            return 55
        return -1

    def __55(self, pick: int) -> int:
        if self.index == 0:
            # $script:1214232707004987$
            # - I wrote it down somewhere. Ahem. "In the middle of the shadows..." Drat! The rest got erased.
            return 55
        elif self.index == 1:
            # $script:1214232707004988$
            # - Sorry, that's all I know. You'll have to ask someone else for the rest of the password.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (54, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (55, 0):
            return Option.NEXT
        elif (self.state, self.index) == (55, 1):
            return Option.CLOSE
        return Option.NONE
