""" 11000003: Growlie """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000015$
        # - What?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000018$
        # - I don't care why the court was canceled anymore. I've heard every rumor under the sun, and now they're saying it was an earthquake? Ridiculous! All I want now is to kick back.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407000019$
        # - Bah, everyone acts like they're the busiest person in the world. Everyone here in $map:02000001$ spends their day rushing around like fools. Seriously!
        return -1

    def __60(self, pick: int) -> int:
        # $script:1215102407009687$
        # - What do you want?
        if pick == 0:
            # $script:1215102407009688$
            # - Have you heard the rumors going around?
            return 61
        return -1

    def __61(self, pick: int) -> int:
        # $script:1215102407009689$
        # - For the last time, I'm not adopted! Mom says its normal for babies to come out giant and furry sometimes. If you want a real rumor, you should hear about the giant demons zipping around the sky.
        if pick == 0:
            # $script:1215102407009690$
            # - Giant demons?
            return 62
        return -1

    def __62(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215102407009691$
            # - You didn't know? It's all anyone's talking about lately. I've heard talk that they've been kidnapping people.
            if pick == 0:
                # $script:1215102407009692$
                # - Do you actually know of any victims?
                return 63
            return 62
        elif self.index == 1:
            # $script:1215102407009693$
            # - Yeah, the appear like a flash of lightning. In the blink of an eye, the person next to you is gone. Just like that!
            return -1
        return -1

    def __63(self, pick: int) -> int:
        # $script:1215102407009694$
        # - Err... No. I'm just telling you what I heard!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (63, 0):
            return Option.CLOSE
        return Option.NONE
