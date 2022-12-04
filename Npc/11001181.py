""" 11001181: Godar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1014150507004129$
        # - Ah, I should update my travel journal!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1014150507004132$
            # - Ah, a local! <font color="#ffd200">Yalario!</font> It always been my dream to explore strange new worlds, and seek out new life and new civilizations! Traveling this land has been an awesome experience.
            return 30
        elif self.index == 1:
            # $script:1014150507004133$
            # - ...Ah, but I'm sure these sights seem so plain to you. Well, I hope I'll get to keep visiting new places and writing about them in my travel journal.
            if pick == 0:
                # $script:1014150507004134$
                # - Yala-what-io?
                return 31
            elif pick == 1:
                # $script:1014150507004135$
                # - I take it you like to travel?
                return 32
            elif pick == 2:
                # $script:1014150507004136$
                # - Where exactly are you from?
                return 33
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1014150507004137$
        # - New friend! This is how we greet strangers who we want to be our friends. $npcName:11001179[gender:0]$ shouted it out when we first arrived in $map:02000064$, so I guess it can also be used for villages. Well, at least it can be by our captain.
        return -1

    def __32(self, pick: int) -> int:
        # $script:1014150507004138$
        # - Of course! Setting foot in a new land, leaving proof of your journey... There's nothing more exciting! I bet everyone in the <b>Allicari Merchant Society</b> would agree.
        return -1

    def __33(self, pick: int) -> int:
        # $script:1014150507004139$
        # - I'm from a place far, far away! On the other side of the sea. To get there from here you have to go north... no wait, south... Err, east? We sort of stumbled upon this land by accident. My homeland is beautiful, although it's much different than here.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1026143107004294$
        # - Ah, yalario! What can I do for you?
        if pick == 0:
            # $script:1026143107004295$
            # - I'm looking for some $item:30000421$.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1026143107004296$
        # - Ah, those. The smuggler called $npcName:11001212[gender:0]$ sells them, but I wouldn't do business with him if I were you.
        if pick == 0:
            # $script:1026143107004297$
            # - Why do you say that?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:1026143107004298$
        # - He snuck onto our vessel because he did not want to pay a simple fare. No one who does such a thing could be considered trustworthy.
        if pick == 0:
            # $script:1026143107004299$
            # - Where can I find $npcName:11001212[gender:0]$ now?
            return 43
        return -1

    def __43(self, pick: int) -> int:
        # $script:1026143107004300$
        # - Captain $npcName:11001179[gender:0]$ kicked him off the ship. Last I saw, he was running off toward $map:03000014$.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        return Option.NONE
