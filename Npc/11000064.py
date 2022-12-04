""" 11000064: Lennon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000315$
        # - It's good to see you.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000318$
            # -  I couldn't have returned to my old life if it weren't for the people who believed in me. 
            return 30
        elif self.index == 1:
            # $script:0831180407000319$
            # -  $MyPCName$, you've helped me so much. Thank you.
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407000320$
        # - When I was a fugitive, you gave me a run for my money a few times.
        if pick == 0:
            # $script:0831180407000321$
            # - Really? That's not how I remember it.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000322$
            # - You have no idea. There were a few times that you were only a few feet away from me. If you'd looked around the wrong corner...
            return 41
        elif self.index == 1:
            # $script:0831180407000323$
            # - Luckily, in the end, you decided to trust $npcName:11000529[gender:0]$ instead of $npcName:11000044[gender:0]$. If you'd gone the other way, who knows how things would have turned out?
            if pick == 0:
                # $script:0831180407000324$
                # - You were doing pretty well on your own.
                return 42
            return -1
        return -1

    def __42(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000325$
            # - Maybe it looked like that from the outside, but I was backed into a corner. Bella forced my hand at Katramus. Without you and Blackeye, I'd probably be dead now.
            return 42
        elif self.index == 1:
            # $script:0831180407000326$
            # - In those early days, I didn't think much of you. But no matter how many false leads I planted, you were always back on my tail within a matter of hours.
            return 42
        elif self.index == 2:
            # $script:0831180407000327$
            # - I was sure you'd give up after our fight in that abandoned townhouse. But you kept on growing stronger after that. If I had to fight you now...
            return 42
        elif self.index == 3:
            # $script:0831180407000328$
            # - Let's just say that I'm glad we're on the same side.
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000329$
            # - We used to be best friends, Katvan, Eve, and I. We got into all kinds of mischief when we were kids...
            return 50
        elif self.index == 1:
            # $script:0831180407000330$
            # - But that just makes me hate him more. We had bonds that were thicker than blood, and he betrayed us. For what? A fancy title and a little bit of power?
            return 50
        elif self.index == 2:
            # $script:0831180407000331$
            # - Eve thinks that he might come around again. But I know better. I know Katvan's true colors.
            if pick == 0:
                # $script:0831180407000332$
                # - Surely there's more to the story.
                return 51
            return -1
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000333$
            # - Of course there's more to the story. There's the part that's still coming up. The part where I put Katvan in the ground once and for all.
            return 51
        elif self.index == 1:
            # $script:0831180407000334$
            # - He killed my mentor–Eve's father! There's nothing left to talk about.
            return 51
        elif self.index == 2:
            # $script:0831180407000335$
            # - He had me on the ropes before, but things are different now. And I know I can count on you to help me take him out.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.NEXT
        elif (self.state, self.index) == (42, 1):
            return Option.NEXT
        elif (self.state, self.index) == (42, 2):
            return Option.NEXT
        elif (self.state, self.index) == (42, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.NEXT
        elif (self.state, self.index) == (51, 2):
            return Option.CLOSE
        return Option.NONE
