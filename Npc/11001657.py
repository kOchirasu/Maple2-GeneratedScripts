""" 11001657: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617105607006367$
        # - More questions?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006865$
        # - Halo Mountain...
        if pick == 0:
            # $script:0727223007006866$
            # - Is the master really gone?
            return 40
        elif pick == 1:
            # $script:0727223007006867$
            # - What do we do now?
            return 50
        elif pick == 2:
            # $script:0727223007006868$
            # - Who was that?
            return 60
        return -1

    def __40(self, pick: int) -> int:
        # $script:0727223007006869$
        # - I doubt we've seen the last of him. His command of animus is unlike anything I've ever seen. And until he returns, I will do everything I can to protect Guidance.
        if pick == 0:
            # $script:0727233607006921$
            # - Let's talk about something else.
            return 30
        return -1

    def __50(self, pick: int) -> int:
        # $script:0727223007006870$
        # - I know that we need to evaluate our options carefully... But all I want to do right now is destroy something. I will be deferring to $npcName:11001656[gender:1]$ for now.
        if pick == 0:
            # $script:0727233607006922$
            # - Let's talk about something else.
            return 30
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006871$
            # - I've never seen or heard of him before. Strange that the master never mentioned him, but it sounds like this Kandura lost the title of Munakra to him and has held a grudge ever since.
            return 60
        elif self.index == 1:
            # $script:0727223007006872$
            # - The power he wields wasn't pure animus. The darkness tainting it was potent.
            if pick == 0:
                # $script:0727223007006873$
                # - If I could control my power, I could have...
                return 61
            return -1
        return -1

    def __61(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006874$
            # - ...saved him? Perhaps. The animus you possess was honed over centuries of training by one of the greatest masters Guidance had ever known.
            return 61
        elif self.index == 1:
            # $script:0727223007006875$
            # - And if the master hadn't given you that animus, he may have had the power to stop this. I always feared something like this would happen...
            return 61
        elif self.index == 2:
            # $script:0727223007006876$
            # - But... I suppose I can no longer humor such thoughts. It is just the three of us now.
            return 61
        elif self.index == 3:
            # $script:0727223007006877$
            # - Losing him is... I don't...
            return 61
        elif self.index == 4:
            # $script:0727223007006878$
            # - ...Well, you're his legacy now. Conduct yourself accordingly.
            if pick == 0:
                # $script:0727223007006879$
                # - I'll do my best.
                return 62
            return -1
        return -1

    def __62(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006880$
            # - Don't misunderstand me. I'm not trying to cheer you up.
            return 62
        elif self.index == 1:
            # $script:0727223007006881$
            # - I don't like you, and I doubt I ever will. But, like it or not, you are my $male:brother,female:sister$ in Guidance. We must work together if we are to overcome our trials.
            if pick == 0:
                # $script:0727233607006923$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.NEXT
        elif (self.state, self.index) == (61, 1):
            return Option.NEXT
        elif (self.state, self.index) == (61, 2):
            return Option.NEXT
        elif (self.state, self.index) == (61, 3):
            return Option.NEXT
        elif (self.state, self.index) == (61, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.NEXT
        elif (self.state, self.index) == (62, 1):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
