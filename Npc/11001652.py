""" 11001652: Suspicious Man """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0519143707006208$
        # - ... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0630142807006512$
        # - What's taking him so long...? Huh? What do you want?!
        if pick == 0:
            # $script:0630142807006513$
            # - What are you up to?
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0630142807006514$
        # - Wh-what do you think? I'm sorting junk, that's what!
        if pick == 0:
            # $script:0630142807006515$
            # - (Stare at him.)
            return 32
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0630142807006516$
            # - I-I'm not up to anything bad. Really. I'm just...
            return 32
        elif self.index == 1:
            # $script:0630142807006517$
            # - Wait. You're...
            if pick == 0:
                # $script:0630142807006518$
                # - You know me?
                return 33
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:0630142807006519$
        # - You're the Gray Wolf! I was there when you took down those Blackstar goons in $map:02000138$.
        if pick == 0:
            # $script:0630142807006520$
            # - You're thinking of someone else.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        # $script:0630142807006521$
        # - No, I'm not. You trying to stay off the radar? I would, too, if I had as many enemies as you. But your face has been burned into my brain ever since that day.
        if pick == 0:
            # $script:0630142807006522$
            # - ...
            return 35
        return -1

    def __35(self, pick: int) -> int:
        # $script:0630142807006523$
        # - Anyway, what are you doing here?
        if pick == 0:
            # $script:0630142807006524$
            # - I have business here.
            return 36
        return -1

    def __36(self, pick: int) -> int:
        # $script:0630142807006525$
        # - Here? You and the Blackstars are mortal enemies now, right? Wait... you didn't come here to take them on at their headquarters, did you?
        if pick == 0:
            # $script:0630142807006526$
            # - Things... got a little out of control.
            return 37
        return -1

    def __37(self, pick: int) -> int:
        if self.index == 0:
            # $script:0630142807006527$
            # - Y-you really are the terror of $map:02000138$! The equal of a hundred warriors! Y'know, I used to think you were just another thug... Since you're here, maybe there's a question you can answer for me. 
            return 37
        elif self.index == 1:
            # $script:0630142807006528$
            # - I have a, uh, "friend" who went inside their headquarters. He should have been able to sneak out while you kept the gangsters busy, but he's still missing. You didn't see anyone... suspicious when you were there, did you?
            if pick == 0:
                # $script:0630142807006529$
                # - Everyone in there looked suspicious.
                return 38
            return -1
        return -1

    def __38(self, pick: int) -> int:
        # $script:0630142807006530$
        # - Yeah, yeah, good point. Ha, I almost feel sorry for the Blackstars, having an enemy like you. Hahaha!
        if pick == 0:
            # $script:0630142807006531$
            # - (Say nothing.)
            return 39
        return -1

    def __39(self, pick: int) -> int:
        # $script:0630142807006532$
        # - Ha... Ha ha... Ahem. You're a pretty intense $male:guy,female:gal$, you know that? I hope we meet again.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (37, 0):
            return Option.NEXT
        elif (self.state, self.index) == (37, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (38, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (39, 0):
            return Option.CLOSE
        return Option.NONE
