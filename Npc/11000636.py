""" 11000636: Prisoner 140919 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002589$
        # - I'm innocent!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002593$
        # - Another tourist? Come to see all the animals in their cages?
        if pick == 0:
            # $script:0831180407002594$
            # - How did you end up in here?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002595$
        # - Argh, don't get me started. Why can't I change my own profile image to something I like? So what if the picture is a little bit... lewd?
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004895$
        # - Another tourist? Come to see all the animals in their cages?
        if pick == 0:
            # $script:1210061907004896$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1210061907004897$
        # - ...You're one of <i>them</i>, aren't you?
        if pick == 0:
            # $script:1210061907004898$
            # - Uh... Sure I am. $npcName:11001231[gender:0]$ sent me.
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1210061907004899$
        # - Quiet, or the warden will hear you! You came to see how things are coming along, is that it?
        if pick == 0:
            # $script:1210061907004900$
            # - That's right.
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:1210061907004901$
        # - Then talk to the supervisor. He's the one in charge here.
        if pick == 0:
            # $script:1210061907004902$
            # - Of course. And the supervisor is...?
            return 54
        return -1

    def __54(self, pick: int) -> int:
        # $script:1210061907004903$
        # - $npcName:11000651[gender:0]$. You'll need the password, of course. We change it every three days to keep the guards off our trail.
        if pick == 0:
            # $script:1210061907004904$
            # - What's the latest password?
            return 55
        return -1

    def __55(self, pick: int) -> int:
        # $script:1210061907004905$
        # - The latest password is... Shoot, what was it? Thick shadows... something. Ask one of the other guys.
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
            return Option.CLOSE
        return Option.NONE
