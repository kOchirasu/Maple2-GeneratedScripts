""" 11001180: Mayar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1110150406000967$
        # - Ooh... Everything here is so interesting!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1110150406000970$
            # - This place seems so peaceful. And everyone has such strange clothes! What's that person eating? I have so many questions!
            return 30
        elif self.index == 1:
            # $script:1110150406000971$
            # - ...Ah! Yalario! Are you from around here? It is nice to meet you.
            if pick == 0:
                # $script:1110150406000972$
                # - Yala-what-io?
                return 31
            elif pick == 1:
                # $script:1110150406000973$
                # - You sure have a lot of questions.
                return 32
            elif pick == 2:
                # $script:1110150406000974$
                # - Where exactly are you from?
                return 33
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1110150406000975$
        # - Hehe... Yalario is a greeting in my language. It means <b>awaited stranger</b>! Although, the literal translation is more like "well-groomed beard."
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1110150406000976$
            # - How could I not? Visiting a new place is so exciting! I can't wait to learn more about this land and its people.
            return 32
        elif self.index == 1:
            # $script:1110150406000977$
            # - There are so many different types of people here! You must have lots of festivals and holidays of your own. I can't wait to see them!
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:1110150406000978$
        # - Mm... It is a distant land. You probably haven't heard of it. We traveled a great distance by ship to get here. Our village was not at all like this Town of Queens.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        return Option.NONE
