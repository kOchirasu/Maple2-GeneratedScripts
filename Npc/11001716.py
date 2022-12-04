""" 11001716: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0728022507006967$
        # - What?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0728024507007007$
        # - If you have something to say, just say it.
        if pick == 0:
            # $script:0804030507007029$
            # - How are your injuries?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        # $script:0804030507007030$
        # - They are... instructive.
        if pick == 0:
            # $script:0804030507007031$
            # - What does that mean?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0804030507007032$
        # - The best victory is a half-victory. The second best is an easy victory. The worst is a complete victory. Do you know why?
        if pick == 0:
            # $script:0804030507007033$
            # - No.
            return 42
        elif pick == 1:
            # $script:0804030507007034$
            # - Victory and defeat are meaningless concepts.
            return 50
        elif pick == 2:
            # $script:0804030507007035$
            # - I like the victories where I crush my foes.
            return 60
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007036$
            # - An easy victory makes you lazy. A complete victory makes you arrogant, and is almost always followed by a crushing defeat. A half-victory, on the other hand, is only half of a defeat. You have a chance to get up and try again.
            return 42
        elif self.index == 1:
            # $script:0804030507007037$
            # - I may have been defeated on Halo Mountain, but my small victories gave me the courage—no, a reason—to try again.
            return 42
        elif self.index == 2:
            # $script:0804030507007038$
            # - Defeat is just another part of training. The master said that every mistake is a chance to better yourself. Do you understand now?
            #   <font color="#909090">(Junta grins at you.)</font>
            if pick == 0:
                # $script:0804030507007039$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007040$
            # - Don't get philosophical on me. A <i>real</i> philosopher once said, "Do not let what you think you know get in the way of what you have yet to learn."
            return 50
        elif self.index == 1:
            # $script:0804030507007041$
            # - Every concept, no matter how insignificant, has some value. I suggest you listen carefully. 
            return 50
        elif self.index == 2:
            # $script:0804030507007042$
            # - An easy victory makes you lazy. A complete victory makes you arrogant, and is almost always followed by a crushing defeat. A half-victory, on the other hand, is only half of a defeat. You have a chance to get up and try again.
            return 50
        elif self.index == 3:
            # $script:0804030507007043$
            # - Defeat is just another part of training. The master said that every mistake is a chance to better yourself. Do you understand now?
            #   <font color="#909090">(Junta watches you closely.)</font>
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0804030507007044$
        # - A victory like that makes you arrogant, and is almost always followed by a crushing defeat. A half-victory, on the other hand, is only half of a defeat. You have a chance to get up and try again.
        if pick == 0:
            # $script:0804030507007045$
            # - Was Halo Mountain your first half-victory?
            return 61
        return -1

    def __61(self, pick: int) -> int:
        # $script:0804030507007046$
        # - The world is larger than you think. Even outside of Guidance, there are great warriors to rival my own abilities. There is one in particular that I remember to this day... a champion of a place called $map:02000100$.
        if pick == 0:
            # $script:0804030507007047$
            # - An outsider beat you? They must have been a great beast.
            return 62
        return -1

    def __62(self, pick: int) -> int:
        # $script:0804030507007048$
        # - Not a beast... a man. And who said I lost?! I'm insulted that you'd think I would lose to a human... Still, this one was my match.
        if pick == 0:
            # $script:0804030507007049$
            # - Who was he?
            return 63
        return -1

    def __63(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007050$
            # - It doesn't matter. I don't even remember his name. All I recall is his long red hair, and the scars that covered his body.
            return 63
        elif self.index == 1:
            # $script:0804030507007051$
            # - He was too fast and strong to be a normal human. His punches... It was as if he somehow had command of animus. I wonder what sort of training makes a man like that...
            return 63
        elif self.index == 2:
            # $script:0804030507007052$
            # - Well? Do you have anything to say?
            if pick == 0:
                # $script:0804030507007053$
                # - It sounds like he had real strength.
                return 64
            return -1
        return -1

    def __64(self, pick: int) -> int:
        # $script:0804030507007054$
        # - He did. And he got that strength on his own, through hard work. You, on the other hand, are only strong because of the master's animus, and you still faint from time to time! So you'd better train just as hard, understand?
        if pick == 0:
            # $script:0804030507007055$
            # - Yes.
            return 65
        return -1

    def __65(self, pick: int) -> int:
        if self.index == 0:
            # $script:0804030507007056$
            # - We're threatened by the strongest enemy we've ever met. We can lay low for now, but eventually we will need to unite our power and take him down. Will you be strong enough to do your part when the time comes?
            return 65
        elif self.index == 1:
            # $script:0804030507007057$
            # - You're dismissed.
            if pick == 0:
                # $script:0804030507007058$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.NEXT
        elif (self.state, self.index) == (42, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.NEXT
        elif (self.state, self.index) == (50, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (63, 0):
            return Option.NEXT
        elif (self.state, self.index) == (63, 1):
            return Option.NEXT
        elif (self.state, self.index) == (63, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (64, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (65, 0):
            return Option.NEXT
        elif (self.state, self.index) == (65, 1):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
