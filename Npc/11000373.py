""" 11000373: Denver """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 30])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001530$
        # - What is it?
        return None # TODO

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001532$
            # - I saw you watching me earlier. You're barking up the wrong tree.
            return 20
        elif self.index == 1:
            # $script:0831180407001533$
            # - Don't you believe me? I have nothing to hide. Have you always been this nosey?
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:1215105107009707$
        # - Today's such a beautiful day! Wouldn't you agree, friend?
        if pick == 0:
            # $script:1215105107009708$
            # - Um, "friend?"
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1215105107009709$
        # - We made eye contact just now, you can't deny it. That makes us pals! Nice to meet you, friend.
        if pick == 0:
            # $script:1215105107009710$
            # - Uh, hey buddy. Have you heard the rumors going around?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:1215105107009711$
        # - I sure have. Look, I wouldn't go around blabbing this to just anybody, but we're friends, right?
        if pick == 0:
            # $script:1215105107009712$
            # - Best friends.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:1215105107009713$
        # - So a while back, I was taking a walk. I like going on walks to clear my head. Of course it only works if I go alone. Anyway—
        if pick == 0:
            # $script:1215105107009714$
            # - Can you fast-forward to the part where stuff happens?
            return 34
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215105107009715$
            # - Right, so I was taking a nice leisurely stroll through Middleton when a giant shadow appeared in the sky!
            return 34
        elif self.index == 1:
            # $script:1215105107009716$
            # - I still can't get the image out of my head... giant wings, and these terrible muscly bodies... It was a whole flock of demons! I was terrified.
            if pick == 0:
                # $script:1215105107009717$
                # - Wait, then you're the one who started the rumor!
                return 35
            return -1
        return -1

    def __35(self, pick: int) -> int:
        # $script:1215105107009718$
        # - They're not rumors! It's all true! Would I lie to my best friend?! Besides, I took a picture. Look.
        if pick == 0:
            # $script:1215105107009719$
            # - Could I keep this photo? Since we're such good friends.
            return 36
        return -1

    def __36(self, pick: int) -> int:
        # $script:1215105107009720$
        # - Sure, if it means you believe me! Take it. I don't know what I'd do if my own friend didn't believe me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.CLOSE
        return Option.NONE
