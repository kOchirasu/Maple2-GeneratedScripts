""" 11004447: Beri Ring """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217160307011984$
        # - Hello, $MyPCName$!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1217160307012011$
            # - You must be here about this fancy chest, yes? It's enchanted to provide you with the materials you need to upgrade your gemstones.
            return 30
        elif self.index == 1:
            # $script:1217160307012012$
            # - Go ahead and give it a try. You'll need the proper reagents to open it, of course.
            if pick == 0:
                # $script:1217160307012013$
                # - What reagents do I need?
                return 31
            elif pick == 1:
                # $script:1217160307012014$
                # - I'm curious about the science behind this.
                return 33
            return -1
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:1217160307012015$
            # - You'll want some $itemPlural:30001187$, which you can get by hunting monsters. That's the raw material that you will turn into gemstones.
            return 31
        elif self.index == 1:
            # $script:1217160307012016$
            # - To trigger the reaction, just use some $item:30001188$, and viola!
            if pick == 0:
                # $script:1217160307012017$
                # - How do I get those?
                return 32
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:1217160307012018$
        # - Fortunately for you, I just so happen to sell them! I should warn you, though, that my supply is pretty limited. It's not easy to make, you know.
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:1217160307012019$
            # - $npc:11000601[gender:1]$ discovered this chest while taking inventory of the royal reliquary. We think it was a gift to the empress from a faraway place. Anyway, it seems to turn the energy of monsters into something useful.
            return 33
        elif self.index == 1:
            # $script:1217160307012020$
            # - The $npc:11004215$, as we've taken to calling it, can convert all kinds of energy. As soon as she found it, $npcName:11000601[gender:1]$ set herself to researching the device.
            return 33
        elif self.index == 2:
            # $script:1217160307012021$
            # - To her surprise, the chest was even able to take the $item:30001187$ taken from monsters and turn it into gem dust. We agreed that it would be in everyone's best interest to make this device freely available to adventurer's like you!
            return 33
        elif self.index == 3:
            # $script:1217160307012022$
            # - Now, you will need $item:30001188$ to stabilize the process. It's simple physics, as I'm sure you know.
            if pick == 0:
                # $script:1217160307012023$
                # - What materials do I need?
                return 31
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:1217160307012026$
        # - The empress has declared that all experienced adventurers shall have access to this enchanted chest here! Not you, though. I'm afraid you're not quite experienced enough. Would you be so kind as to come back when you're level 50?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.NEXT
        elif (self.state, self.index) == (33, 2):
            return Option.NEXT
        elif (self.state, self.index) == (33, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
