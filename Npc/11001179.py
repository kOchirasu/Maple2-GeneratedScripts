""" 11001179: Aliyar """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1014150507004104$
        # - Good day!
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:1014150507004107$
            # - <font color="#ffd200">Yalario!</font> 
            #   I love talking to new people and visiting new places. It's a pleasure to meet you.
            return 30
        elif self.index == 1:
            # $script:1014154907004140$
            # - Ah, an adventurer! Know of any famous monsters around here? I may be a merchant, but I'm just as interested in fighting monsters as selling things. Hahaha!
            if pick == 0:
                # $script:1014150507004108$
                # - Yala-what-io?
                return 31
            elif pick == 1:
                # $script:1014150507004109$
                # - That doesn't sound so great for business...
                return 32
            elif pick == 2:
                # $script:1014150507004110$
                # - Where exactly are you from?
                return 33
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:1014150507004111$
        # - Oh! Forgive me. Sometimes I forget that I am in <i>a foreign land</i>. Where I come from, 'Yalario' is the term we use when meeting someone for the first time. It means "<b>new friend</b>".
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:1014150507004112$
            # - Hahaha! Perhaps not. Truthfully, I am interested in both. Encountering new monsters inspires me to create new products! Mine is a dangerous business, ahahaha!
            return 32
        elif self.index == 1:
            # $script:1014150507004113$
            # - I've sailed around the globe doing battle with all kinds of monsters. You'll find I am as shrewd a warrior as a merchant!
            if pick == 0:
                # $script:1014150507004114$
                # - You're not afraid of monsters?
                return 34
            return -1
        return -1

    def __33(self, pick: int) -> int:
        # $script:1014150507004115$
        # - Far, far across the sea. I haven't seen a single map here which includes my homeland. I have spent half my life sailing around the world, but I had never heard of this 'Wictoria Isslind' until I set foot upon it.
        return -1

    def __34(self, pick: int) -> int:
        # $script:1014150507004116$
        # - Not at all. The people here make a big deal about how dangerous monsters are. But compared to back home, they are as cuddly as teddy bears. I am still hopeful that I will find a worthy challenge.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1026143107004286$
        # - Yalario! How may I help you? If merchandise is what you seek, please browse at your leisure.
        if pick == 0:
            # $script:1026143107004287$
            # - Do you know anything about Cynodia ore?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1026143107004288$
        # - Ah, I know of Cynodia ore. It is filled with mystical power and said to be able to bring balance to unstable magic.
        if pick == 0:
            # $script:1026143107004289$
            # - Do you know where I can find Cynodia ore?
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:1026143107004290$
        # - Hmm... I'm sorry, but they aren't something we carry. Come to think of it, $npcName:11001180[gender:1]$ or $npcName:11001181[gender:0]$ might know where to find some. Why don't you try speaking with them?
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        return Option.NONE
