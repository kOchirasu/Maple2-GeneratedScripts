""" 11001690: Jayce """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006497$
        # - The sooner we get out of this dusty hole, the better.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0708220807006684$
        # - Was there something you wanted to ask me?
        if pick == 0:
            # $script:0708220807006685$
            # - What do you make of my arrangement with $npcName:11001629[gender:0]$?
            return 40
        elif pick == 1:
            # $script:0708220807006686$
            # - What happened to the vagrants Blackstar took hostage?
            return 50
        elif pick == 2:
            # $script:0712221207006745$
            # - Tell me about $npcName:11001547[gender:0]$.
            return 60
        return -1

    def __40(self, pick: int) -> int:
        # $script:0708220807006687$
        # - To be honest, I don't know why that man—I mean, the boss—keeps you around. The things he's asked you to do... 
        if pick == 0:
            # $script:0708220807006688$
            # - ...could be done by anyone.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0708220807006689$
        # - Yes. Easily. And you don't even like him. So why does he have you do it?
        if pick == 0:
            # $script:0708220807006690$
            # - I think I know the answer to that.
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:0708220807006691$
        # - Oh?
        if pick == 0:
            # $script:0708220807006692$
            # - He's trying to tame me.
            return 43
        return -1

    def __43(self, pick: int) -> int:
        # $script:0708220807006693$
        # - Maybe, but <i>can</i> you be tamed? My peers may think you're harmless, but I see a wolf that's taken care to hide $male:his,female:her$ fangs and claws.
        if pick == 0:
            # $script:0708225907006705$
            # - Let's talk about something else.
            return 30
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0708220807006694$
            # - If you're worried about their safety, well, that all depends on your cooperation.
            return 50
        elif self.index == 1:
            # $script:0708220807006695$
            # - I don't understand why you allow the boss to walk all over you. You have no obligation to him. Blackstar is big, but you...
            if pick == 0:
                # $script:0708220807006696$
                # - I lost the match. I'm honor bound to work with him.
                return 51
            return -1
        return -1

    def __51(self, pick: int) -> int:
        # $script:0708220807006697$
        # - You say that, even knowing that the fight was fixed? Incredible. You're the most loyal, honorable, and... frustratingly righteous person I've ever met.
        if pick == 0:
            # $script:0708225907006706$
            # - I've learned a new lesson from $npcName:11001629[gender:0]$.
            return 52
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629000607006499$
            # - If that's what you think, then I won't ask any further.
            return 52
        elif self.index == 1:
            # $script:0630002207006511$
            # - If you need anything, you can try asking $npcName:11001674[gender:0]$ or $npcName:11001682[gender:0]$. I can't guarantee that they'll be very helpful, though.
            if pick == 0:
                # $script:0708225907006707$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0712221207006746$
        # - $npcName:11001547[gender:0]$ is truly a magnificent beast. It's not just that he's strong—he is completely and utterly fearless.
        if pick == 0:
            # $script:0712221207006747$
            # - What does he have to fear? His dad is the boss!
            return 61
        return -1

    def __61(self, pick: int) -> int:
        if self.index == 0:
            # $script:0712221207006748$
            # - Of course you would assume that $npcName:11001547[gender:0]$ gets special treatment because of his father. But, in truth, it's $npcName:11001618[gender:0]$ who is lucky to have $npcName:11001547[gender:0]$ for a son.
            return 61
        elif self.index == 1:
            # $script:0712221207006749$
            # - When Blackstar was first started, it had many enemies. Hardly a day passed when someone didn't try to take the boss's life. But $npcName:11001547[gender:0]$ watched over $map:02000100$ like a hawk, keeping his father safe and eliminating our enemies one at a time.
            return 61
        elif self.index == 2:
            # $script:0712221207006750$
            # - He won't take credit for it, but there would be no Blackstar without him. And yet, some people still grumble that he acts too cocky for a brat who merely happened to be <i>adopted</i> by the boss.
            if pick == 0:
                # $script:0712221207006751$
                # - Wait, $npcName:11001547[gender:0]$ was adopted?
                return 62
            return -1
        return -1

    def __62(self, pick: int) -> int:
        if self.index == 0:
            # $script:0712221207006752$
            # - I don't know the details. All I know is that the boss brought home this ten-year-old boy one day and treated him as a son. He couldn't possibly be the boss's real child.
            return 62
        elif self.index == 1:
            # $script:0712221207006753$
            # - Whatever their story is, $npcName:11001547[gender:0]$ doesn't seem to care about his birth or his position in Blackstar. Most of us respect and admire him, and those who don't are too cowardly to speak up.
            if pick == 0:
                # $script:0712221207006754$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.NEXT
        elif (self.state, self.index) == (61, 1):
            return Option.NEXT
        elif (self.state, self.index) == (61, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.NEXT
        elif (self.state, self.index) == (62, 1):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
