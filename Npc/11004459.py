""" 11004459: Farennis """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1227192907012056$
        # - $male:Sir,female:Ma'am$! I'm $npcName:11004459[gender:0]$, in charge of logistics!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012057$
            # - $male:Sir,female:Ma'am$! I'm $npcName:11004459[gender:0]$, in charge of logistics!
            return 10
        elif self.index == 1:
            # $script:1227192907012058$
            # - We could never have put a base like this together so quickly without Sky Fortress.
            if pick == 0:
                # $script:1227192907012059$
                # - How did you manage this, anyway?
                return 20
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012060$
            # - As soon as this mission began, Cat Sith started sending me data on the base's construction plans and materials.
            return 20
        elif self.index == 1:
            # $script:1227192907012061$
            # - I'm happy to report that not a single brick went to waste in constructing this place!
            if pick == 0:
                # $script:1227192907012062$
                # - What's Cat Sith?
                return 21
            elif pick == 1:
                # $script:1227192907012063$
                # - What does Cat Sith mean?
                return 22
            return -1
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012064$
            # - I'm surprised you haven't been briefed. It's the new shipboard AI. It's able to scour data from the Sky Fortress's memory banks and learn on its own.
            return 21
        elif self.index == 1:
            # $script:1227192907012065$
            # - The captain came up with the AI design and the tactical officer did all of the programming. I admit, I'm a little intimidated by their genius.
            if pick == 0:
                # $script:0114160707012701$
                # - Amazing.
                return 23
            return -1
        return -1

    def __22(self, pick: int) -> int:
        # $script:1227192907012066$
        # - You'd have to ask the captain, since she's the one who named it. I imagine it has something to do with cats. Just a hunch.
        return -1

    def __23(self, pick: int) -> int:
        # $script:0114160707012702$
        # - Of course it is. Why, it's astonishing, even!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.NEXT
        elif (self.state, self.index) == (21, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.CLOSE
        return Option.NONE
