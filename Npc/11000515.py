""" 11000515: Jayce """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002209$
        # - Can I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407002210$
        # - If you're looking for the $map:2000216$, you came to the right place.
        if pick == 0:
            # $script:0831180407002211$
            # - What's the $map:02000216$?
            return 51
        elif pick == 1:
            # $script:0831180407002212$
            # - I'm curious about Blackstar.
            return 52
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002213$
            # - I'm not surprised you haven't heard of it. This is a place that services people with extraordinary taste.
            return 51
        elif self.index == 1:
            # $script:0831180407002214$
            # - Looking for items to invest in? Have rare items to sell? This is the place to do it.
            return 51
        elif self.index == 2:
            # $script:0831180407002215$
            # - Whatever your business, you'll find that the goods we broker here are a far cry from those you find in $map:2000100$.
            return 51
        elif self.index == 3:
            # $script:0831180407002216$
            # - Talk to one of my brokers below to browse or sell items.
            return 51
        elif self.index == 4:
            # $script:0831180407002217$
            # - Note that epic and above items can only be brokered through the $map:2000216$. We'll <i>know</i> if you try to move them without us, and trust me, we will not be pleased.
            return 51
        elif self.index == 5:
            # $script:0831180407002218$
            # - Now, if you'll excuse me...
            return -1
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002219$
            # - Well, aren't you the joker. If you're smart, you won't repeat that question to anyone else.
            return 52
        elif self.index == 1:
            # $script:0831180407002220$
            # - For the record, we aren't doing anything illegal here.
            return 52
        elif self.index == 2:
            # $script:0831180407002221$
            # - The $map:2000216$ attracts adventurers and tourists from all over Maple World, and that's advantageous to $map:2000100$.
            return 52
        elif self.index == 3:
            # $script:0831180407002222$
            # - In fact, the majority of $map:2000100$'s residents support us. The polls all say so.
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0711184007006708$
        # - Ah, Gray Wolf. You have business with me? If you're looking for the $map:2000216$, you've come to the right place.
        if pick == 0:
            # $script:0711184007006709$
            # - What's the $map:02000216$?
            return 61
        elif pick == 1:
            # $script:0711184007006710$
            # - I'm curious about Blackstar.
            return 62
        return -1

    def __61(self, pick: int) -> int:
        if self.index == 0:
            # $script:0711184007006711$
            # - I'm not surprised you haven't heard of it. This is a place that services people with extraordinary taste. Our clientèle does not typically mix with rough-and-tumble fighter types.
            return 61
        elif self.index == 1:
            # $script:0711184007006712$
            # - I'll have to check what items I have that are suitable for your skills. Are you looking for something in particular? Or do you have a rare item that you'd like to sell?
            return 61
        elif self.index == 2:
            # $script:0711184007006713$
            # - I don't care either way. The products here are incomparable to those available in $map:2000100$. Heh.
            return 61
        elif self.index == 3:
            # $script:0711184007006714$
            # - Simply talk to the traders here to browse their wares or sell your items on the $map:2000216$. They'll do their best to help you. Probably.
            return 61
        elif self.index == 4:
            # $script:0711184007006715$
            # - Keep in mind that the only place to trade epic and better items is the $map:2000216$. And if you try to secretly trade such items without us, we'll know. You may be the famous Gray Wolf, but this is our field of expertise.
            return 61
        elif self.index == 5:
            # $script:0711184007006716$
            # - Now, if you'll excuse me...
            return -1
        return -1

    def __62(self, pick: int) -> int:
        if self.index == 0:
            # $script:0711184007006717$
            # - I'm telling you this for your own good. A place like this draws a lot of attention. Even now, agents from many organizations are watching us.
            return 62
        elif self.index == 1:
            # $script:0711184007006718$
            # - Not many people recognize you as a threat. But if you keep asking questions like that, they'll start to take notice. You don't want that. Understand?
            return 62
        elif self.index == 2:
            # $script:0711184007006719$
            # - You may not be Blackstar's biggest fan, but not everything it does is bad. The $map:2000216$ has drawn adventurers and traders from all over Maple World. I'd say that it's single-handedly put $map:2000100$ and $map:2000135$ on the map.
            return 62
        elif self.index == 3:
            # $script:0711184007006720$
            # - The people of $map:2000100$ are thankful for what we've done for the community. So I suggest you keep your opinions about Blackstar to yourself while you're here.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.NEXT
        elif (self.state, self.index) == (51, 2):
            return Option.NEXT
        elif (self.state, self.index) == (51, 3):
            return Option.NEXT
        elif (self.state, self.index) == (51, 4):
            return Option.NEXT
        elif (self.state, self.index) == (51, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.NEXT
        elif (self.state, self.index) == (52, 2):
            return Option.NEXT
        elif (self.state, self.index) == (52, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.NEXT
        elif (self.state, self.index) == (61, 1):
            return Option.NEXT
        elif (self.state, self.index) == (61, 2):
            return Option.NEXT
        elif (self.state, self.index) == (61, 3):
            return Option.NEXT
        elif (self.state, self.index) == (61, 4):
            return Option.NEXT
        elif (self.state, self.index) == (61, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (62, 0):
            return Option.NEXT
        elif (self.state, self.index) == (62, 1):
            return Option.NEXT
        elif (self.state, self.index) == (62, 2):
            return Option.NEXT
        elif (self.state, self.index) == (62, 3):
            return Option.CLOSE
        return Option.NONE
