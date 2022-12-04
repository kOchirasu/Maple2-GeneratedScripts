""" 11004284: Demdem """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911214707011299$
        # - Welcome! This is $map:02010002$, the heart of Karkar! On behalf of meerkats everywhere, I'd just like to say... Hiya!
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911214707011300$
            # - Welcome! This is $map:02010002$, the heart of Karkar! On behalf of meerkats everywhere, I'd just like to say... Hiya!
            return 10
        elif self.index == 1:
            # $script:0911214707011301$
            # - Karkar Island is hot and dry. Drink lots of water to stay hydrated, and don't forget to slather on that sunscreen!
            return 10
        elif self.index == 2:
            # $script:0913151207011310$
            # - Ah, doesn't that balance between the fierce desert and the cityscape here in $map:02010002$ revitalize you? Say, have you ever visited the $npcName:11004264$?
            if pick == 0:
                # $script:0913151207011311$
                # - I don't believe I've had the pleasure.
                return 11
            elif pick == 1:
                # $script:0913151207011312$
                # - I sure have!
                return 12
            return -1
        return -1

    def __11(self, pick: int) -> int:
        # $script:0913151207011313$
        # - That just won't do! The $npcName:11004264$ is <i>the</i> hottest shopping spot in the whole city! Go ahead, run along now!
        return -1

    def __12(self, pick: int) -> int:
        # $script:0913151207011314$
        # - Isn't it so cool? I was thinking of heading over there tonight and treating myself to a new hat!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        return Option.NONE
