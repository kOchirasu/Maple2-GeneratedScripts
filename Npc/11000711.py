""" 11000711: Mint """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002847$
        # - Hello.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407002848$
        # - Woo-hoo! Have a great day today!
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407002849$
        # - Yoo-hoo! Yet another beautiful day has dawned. Isn't it great?
        if pick == 0:
            # $script:0831180407002850$
            # - Yep!
            return 21
        elif pick == 1:
            # $script:0831180407002851$
            # - It's not worth it.
            return 22
        return -1

    def __21(self, pick: int) -> int:
        # $script:0831180407002852$
        # - Since I became a Bunny Gal, every day has been like a dream. I never thought my life could be this fun!
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407002853$
        # - Oh, you don't think so? Why not? It's all a matter of perspective. You should try to think positive. Like me! Hee hee hee!
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407002854$
        # - Hm? Where are you staring at?
        if pick == 0:
            # $script:0831180407002855$
            # - I can't help it... you're so pretty!
            return 31
        elif pick == 1:
            # $script:0831180407002856$
            # - I... wasn't staring at you!
            return 32
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407002857$
        # - Oh, really? Do you think I'm pretty? I wasn't always so pretty, you know. Hee hee hee! I'd like it if you'd come visit me more often. I think I like you!
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002858$
            # - Oh, y-you weren't? Hmph, for a moment I thought you had the hots for me.
            return 32
        elif self.index == 1:
            # $script:0831180407002859$
            # - But... are you SURE you weren't staring at me?
            if pick == 0:
                # $script:0831180407002860$
                # - Nope!
                return 33
            elif pick == 1:
                # $script:0831180407002861$
                # - Okay... you caught me.
                return 34
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407002862$
        # - No? Well... All right then. If you say you weren't, then you weren't. Oh well!
        return -1

    def __34(self, pick: int) -> int:
        # $script:0831180407002863$
        # - You were, right? I knew it. Hee hee! Don't be embarrassed. You aren't the only one who likes to stare at me.
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407002864$
        # - Wow, $MyPCName$, don't you just love the weather today? Back when I had to stay inside, I could hardly tell what the weather was.
        if pick == 0:
            # $script:0831180407002865$
            # - What happened to you back then?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002866$
            # - Huh? W-well... I don't... I don't want to talk about my past. 
            return 41
        elif self.index == 1:
            # $script:0831180407002867$
            # - Let's talk about something else, shall we? Keep your head in the present, I always say! Eyes on the prize!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.CLOSE
        return Option.NONE
