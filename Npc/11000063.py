""" 11000063: Kanna """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000294$
        # - How may I help you?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407000298$
        # - I want to become a great Heavy Gunner like $npcName:11000046[gender:1]$ when I grow up! Pew pew!
        if pick == 0:
            # $script:0831180407000299$
            # - Why's that?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000300$
            # - Well, yesterday I was out playing by the castle and I tripped on a stone. It really hurt and I cried a whole lot! Then $npcName:11000046[gender:1]$ saw me crying and asked why, because she's a HERO.
            return 31
        elif self.index == 1:
            # $script:0831180407000301$
            # - I told her all about tripping over the stone, and how I hate stones now! So $npcName:11000046[gender:1]$ took her giant gun... and BLEW UP the stone! Ka-BOOOOSH!
            return 31
        elif self.index == 2:
            # $script:0831180407000302$
            # - $npcName:11000046[gender:1]$ said that if something hurts her, she'll hurt it ten times worse! Now those are words to live by, right? Right?
            if pick == 0:
                # $script:0831180407000303$
                # - Yes.
                return 32
            elif pick == 1:
                # $script:0831180407000304$
                # - No.
                return 36
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407000305$
        # - Hooray, you get it! You know, $npcName:11000046[gender:1]$ and I have a secret now.
        if pick == 0:
            # $script:0831180407000306$
            # - What's the secret?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407000307$
        # - Well, it's a secret... Can you keep it secret?
        if pick == 0:
            # $script:0831180407000308$
            # - Of course.
            return 34
        elif pick == 1:
            # $script:0831180407000309$
            # - I'll decide after you tell me.
            return 35
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000310$
            # - This really is a secret... Alright, I'll tell you because you're $MyPCName$.
            return 34
        elif self.index == 1:
            # $script:0831180407000311$
            # - When $npcName:11000046[gender:1]$ blew up the stone, she also blew up a bunch of hay and firewood that was lying around.
            return 34
        elif self.index == 2:
            # $script:0831180407000312$
            # - No one knows she did it except me. And her. And now you! So $MyPCName$, you'll keep this a secret, right? $npc:11000046[gender:1]$ made me pinky-swear not to tell, so you have to pinky-swear to me.
            return -1
        return -1

    def __35(self, pick: int) -> int:
        # $script:0831180407000313$
        # - No! Then I'm not going to tell you! Hmph!
        return -1

    def __36(self, pick: int) -> int:
        # $script:0831180407000314$
        # - Oh $MyPCName$, you don't understand me.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.NEXT
        elif (self.state, self.index) == (34, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (35, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (36, 0):
            return Option.CLOSE
        return Option.NONE
