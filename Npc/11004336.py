""" 11004336: Aisha """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1010140307011595$
        # - These readings are off the chart!
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1010140307011596$
        # - Is this for real?!
        if pick == 0:
            # $script:1010153807011618$
            # - Huh? What happened?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010140307011597$
            # - Nothing <i>happened.</i> It's just... this place! I've never seen magic and science mashed together like this!
            return 11
        elif self.index == 1:
            # $script:1010140307011598$
            # - I need to get my hands on some of this aetherine stuff. If my calculations are right, the energy content of each of these little stones is... Well, it's explosive!
            return 11
        elif self.index == 2:
            # $script:1010140307011599$
            # - This could totally change how we think about energy!
            if pick == 0:
                # $script:1010140307011600$
                # - A bit of an energy nut, aren't you?
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:1010140307011601$
        # - Why wouldn't I be? This gives me an idea for a new reactor design...
        return -1

    def __40(self, pick: int) -> int:
        # $script:1010151207011604$
        # - You—?!
        if pick == 0:
            # $script:1010151207011605$
            # - $npcName:11004336[gender:1]$?!
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010153807011619$
            # - Boss! I was starting to think you didn't see me. Heh!
            return 41
        elif self.index == 1:
            # $script:1010151207011606$
            # - Keep your voice down, Boss! $npcName:11004334[gender:1]$ is right around the corner.
            if pick == 0:
                # $script:1010151207011607$
                # - Is that why you're here? To spy on the Resistance?
                return 42
            return -1
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010151207011608$
            # - No way! I'm here for critical research. At least, that's what I told $npcName:11000264[gender:0]$...
            return 42
        elif self.index == 1:
            # $script:1010151207011609$
            # - Boss, there's something you need to know. I've spotted the Resistance going in and out of $npcName:11000264[gender:0]$'s office.
            return 42
        elif self.index == 2:
            # $script:1010151207011610$
            # - They're up to something. Since I didn't know when you'd come visit me again, I decided I'd check it out for myself!
            if pick == 0:
                # $script:1010151207011611$
                # - This place is way too dangerous for you. Let's get you ba—
                return 43
            return -1
        return -1

    def __43(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010151207011612$
            # - Uh, heck no! Even if I lied to my fake boss, there really <i>is</i> a ton of stuff for me to research here.
            return 43
        elif self.index == 1:
            # $script:1010151207011613$
            # - Anyway, you're too busy to save the world <i>and</i> spy on the Resistance. You need my help!
            if pick == 0:
                # $script:1010151207011614$
                # - $npcName:11004336[gender:1]$... By any chance, do you... have a <b>huge travel budget</b>?
                return 44
            return -1
        return -1

    def __44(self, pick: int) -> int:
        if self.index == 0:
            # $script:1010151207011615$
            # - ...
            return 44
        elif self.index == 1:
            # $script:1010151207011616$
            # - ...
            if pick == 0:
                # $script:1010151207011617$
                # - Say something, $npcName:11004336[gender:1]$.
                return 45
            return -1
        return -1

    def __45(self, pick: int) -> int:
        # $script:1010174007011620$
        # - ...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.NEXT
        elif (self.state, self.index) == (42, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.NEXT
        elif (self.state, self.index) == (43, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (44, 0):
            return Option.NEXT
        elif (self.state, self.index) == (44, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (45, 0):
            return Option.CLOSE
        return Option.NONE
