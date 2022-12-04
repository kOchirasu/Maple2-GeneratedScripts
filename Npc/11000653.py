""" 11000653: Prisoner 170125 """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002684$
        # - When can I get out of here?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407002688$
        # - I'm busy. Scram!
        if pick == 0:
            # $script:0831180407002689$
            # - What are you doing?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002690$
        # - Can't you see? I'm working! If I were you, I would've stayed home napping instead of coming to see a horrible place like this.
        return -1

    def __50(self, pick: int) -> int:
        # $script:1210061907004929$
        # - I'm busy. Scram!
        if pick == 0:
            # $script:1210061907004930$
            # - Do you know someone named $npcName:11001231[gender:0]$?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:1210061907004931$
        # - Keep your voice down. We're being watched. You're in the know?
        if pick == 0:
            # $script:1210061907004932$
            # - Uh... Sure I am. $npcName:11001231[gender:0]$ sent me.
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1214232707004989$
        # - We call $npcName:11000651[gender:0]$ the supervisor. He's the one you oughtta be talking to, not me. But good luck getting a peep outta him without the password...
        if pick == 0:
            # $script:1214232707004990$
            # - What's the password?
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:1214232707004991$
        # - Haw! Like I'm gonna trust <i>you</i> with that info! If you don't even know the password, how can I trust you? Stoopid!
        if pick == 0:
            # $script:1214232707004992$
            # - I'll be sure to mention you when I see $npcName:11001231[gender:0]$.
            return 54
        return -1

    def __54(self, pick: int) -> int:
        # $script:1214232707004993$
        # - Bah! <b>Fine!</b> The password is... I forget. They change the dang thing every three days, y'know?
        if pick == 0:
            # $script:1214232707004994$
            # - Do you remember any part of it?
            return 55
        return -1

    def __55(self, pick: int) -> int:
        if self.index == 0:
            # $script:1214232707004995$
            # - How'd it go? Um... "Enlighten the light," I think. That's all I remember, honest!
            return 55
        elif self.index == 1:
            # $script:1214232707004996$
            # - Now get outta here, before the warden notices we been talking.
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
