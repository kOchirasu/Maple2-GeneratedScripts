""" 11000324: Cantata """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001308$
        # - Hey, man! What's happening?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0910105907003794$
        # - It's not difficult to express your feelings in a tasteful way. Do it like the cool person you are!
        if pick == 0:
            # $script:0910105907003795$
            # - I have questions about emotes.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:0910105907003796$
        # - Sure, fire away!
        if pick == 0:
            # $script:0910105907003797$
            # - What are emotes?
            return 32
        elif pick == 1:
            # $script:0910105907003798$
            # - Where can I get emotes?
            return 33
        elif pick == 2:
            # $script:0910105907003799$
            # - How can I use emotes?
            return 34
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0910105907003800$
            # - How do you express yourself when you're happy or sad? Just typing in chat? No, no, that's not how we do it here. That's why you've got emotes, yo.
            return 32
        elif self.index == 1:
            # $script:0910105907003801$
            # - When you're happy, laugh! Excited? Dance! Sad? Cry! There are tons of actions you can perform to express yourself to those around you, even without words. Make good use of them!
            if pick == 0:
                # $script:0910105907003802$
                # - I need to ask something else.
                return 35
            return -1
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0910105907003803$
            # - Some emotes are placed on your F1 - F12 keys by default. When you meet your friends, press F1 or F2 to greet them. If your friends are as sensible as you are, they'd greet you back in the same way!
            return 33
        elif self.index == 1:
            # $script:0910105907003804$
            # - Aside from the 12 default actions, you can buy more actions at the Meret Market. Take a look at the Expression tab in the Premium Shop for all the available actions you can buy!
            if pick == 0:
                # $script:0910105907003805$
                # - I need to ask something else.
                return 35
            return -1
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:0910105907003806$
            # - Take a look at the right side of the Chat window for the smiley face icon. Click it to open the emote window. If you buy emotes from the Meret Market, don't forget to learn the Emotes from the Inventory window.
            return 34
        elif self.index == 1:
            # $script:0910105907003807$
            # - Got so many emotes that it's difficult to remember the hotkeys? Don't worry, I'll fill you in! You can use them by typing their commands into the Chat window. For example, if you want to use the Hello action, you can type /hello in the Chat window instead of pressing F1.
            return 34
        elif self.index == 2:
            # $script:0910105907003808$
            # - Each emote has multiple commands, so check them in the emote window and use the ones you can remember easily.
            if pick == 0:
                # $script:0910105907003809$
                # - I need to ask something else.
                return 35
            return -1
        return -1

    def __35(self, pick: int) -> int:
        # $script:0910105907003810$
        # - Is there anything else you want to ask about emotes?
        if pick == 0:
            # $script:0910105907003811$
            # - What are emotes?
            return 32
        elif pick == 1:
            # $script:0910105907003812$
            # - Where can I get emotes?
            return 33
        elif pick == 2:
            # $script:0910105907003813$
            # - How can I use emotes?
            return 34
        elif pick == 3:
            # $script:0910105907003814$
            # - I need to be going.
            return 36
        return -1

    def __36(self, pick: int) -> int:
        # $script:0910105907003815$
        # - Don't think too hard, dawg. Just express yourself!
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
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.NEXT
        elif (self.state, self.index) == (34, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.CLOSE
        return Option.NONE
