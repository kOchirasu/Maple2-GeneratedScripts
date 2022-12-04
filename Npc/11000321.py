""" 11000321: Irena """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407001258$
        # - What is it?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407001263$
        # - Can I talk to you about something?
        if pick == 0:
            # $script:0831180407001264$
            # - Sure.
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:0831180407001265$
        # - One of the guys in my neighborhood keeps making fun of my face. He says I'm ugly. Am I... really that ugly? Please be honest with me.
        if pick == 0:
            # $script:0831180407001266$
            # - Nope!
            return 52
        elif pick == 1:
            # $script:0831180407001267$
            # - Yep!
            return 53
        return -1

    def __52(self, pick: int) -> int:
        # $script:0831180407001268$
        # - Really? You really don't think I'm ugly? Then... do you think he'll think I'm pretty?
        if pick == 0:
            # $script:0831180407001269$
            # - Well, I didn't say you're pretty, either.
            return 53
        elif pick == 1:
            # $script:0831180407001270$
            # - Who is he?
            return 54
        return -1

    def __53(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001271$
            # - Oh, I see... Then maybe I should really think about getting cosmetic surgery. Thank you... for depressing me further...
            return 53
        elif self.index == 1:
            # $script:0831180407001272$
            # - Then do you think I'll look pretty if I get cosmetic surgery? I really want to look pretty for him.
            if pick == 0:
                # $script:0831180407001273$
                # - Who is he?
                return 54
            elif pick == 1:
                # $script:0831180407001274$
                # - Yeah, I mean... maybe that'll work.
                return 57
            return -1
        return -1

    def __54(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001275$
            # - I don't know his name. He's one of the travelers who came to $map:02000001$ because of the court.
            return 54
        elif self.index == 1:
            # $script:0831180407001276$
            # - Big blue eyes. Beautiful golden hair. He looks so dashing with the sword on his belt! And his polka-dot scarf... it's so cute! Have you ever seen anyone so amazing before?
            if pick == 0:
                # $script:0831180407001277$
                # - No.
                return 55
            elif pick == 1:
                # $script:0831180407001278$
                # - Yes.
                return 55
            return -1
        return -1

    def __55(self, pick: int) -> int:
        # $script:0831180407001279$
        # - You know, sometimes he looks around as if he's waiting for someone. Do you think he has a girlfriend? What if he has a girlfriend?
        if pick == 0:
            # $script:0831180407001280$
            # - I don't know.
            return 56
        elif pick == 1:
            # $script:0831180407001281$
            # - I don't think he has a girlfriend.
            return 56
        return -1

    def __56(self, pick: int) -> int:
        # $script:0831180407001282$
        # - So, you don't know. Three times a day, in the morning, at noon, and in the evening, I go out to the main road. I pretend to take a stroll, just to steal a few glances at him. Ah, I want to see him again! Do you think I'm in love?
        return -1

    def __57(self, pick: int) -> int:
        # $script:0831180407001283$
        # - Do you think so? Okay, then I really need to go to $map:02000107$...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.NEXT
        elif (self.state, self.index) == (53, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (54, 0):
            return Option.NEXT
        elif (self.state, self.index) == (54, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (55, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (56, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (57, 0):
            return Option.CLOSE
        return Option.NONE
