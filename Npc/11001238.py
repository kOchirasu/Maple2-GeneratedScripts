""" 11001238: Merkaz """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123154807004427$
        # - Hm...
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1123154807004430$
        # - Come, come, tell me what you need. You won't be leaving empty-handed, heh heh heh...
        if pick == 0:
            # $script:1123154807004431$
            # - I bet you get lots of customers.
            return 31
        elif pick == 1:
            # $script:1123154807004432$
            # - Why the creep—er, cheery smile?
            return 32
        elif pick == 2:
            # $script:1123154807004433$
            # - I bet you have all kinds of weird stories.
            return 33
        return -1

    def __31(self, pick: int) -> int:
        # $script:1123154807004434$
        # - Of course, of course! I do not know why they come here, but I do so enjoy watching them skitter here and there.
        return -1

    def __32(self, pick: int) -> int:
        # $script:1123154807004435$
        # - Don't worry your little soul about that. You'll learn soon enough... even if you don't want to.
        return -1

    def __33(self, pick: int) -> int:
        # $script:1123154807004436$
        # - Enough to spend all night in the telling, and then some! So, what would you like to hear? The tale of a young monster slayer and his buxom mage companion? The story of how I've kept my youthful looks? Or... something else? 
        if pick == 0:
            # $script:1123154807004437$
            # - Something else! Please, something else.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:1123154807004438$
            # - Ahhh, yes... I know just the tale for a squirmy adventurer like you. Listen close, dearie...
            return 34
        elif self.index == 1:
            # $script:1123154807004439$
            # - Legend has it that when the Shadow Seed takes root, a new son will be born unto the Demon King and darkness shall swallow the world. A lovely little tale, don't you think?
            if pick == 0:
                # $script:1123154807004440$
                # - You and I have different definitions of 'lovely.'
                return 35
            return -1
        return -1

    def __35(self, pick: int) -> int:
        # $script:1123154807004441$
        # - Blind little child! Lovely is in the eye of the beholder.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1125183507007502$
        # - Even when it is too dark to see, keep your eyes wide open. You'll find your way... eventually.
        if pick == 0:
            # $script:1125183507007503$
            # - Okay. Sure. <i>That</i> makes sense.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1125183507007504$
        # - What I am <i>trying</i> to say is that you shouldn't be here right now. I will send you to where you should be.
        if pick == 0:
            # $script:1125183507007505$
            # - Please send me there again.
            # TODO: goto 42
            # TODO: gotoFail 43
            return 43
        return -1

    def __42(self, pick: int) -> int:
        # functionID=1 
        # $script:1125183507007506$
        # - I've created a portal for you down there. It will take you to $map:52000076$. Next time, use the portal instead of bothering me, all right?
        return -1

    def __43(self, pick: int) -> int:
        # $script:1125185807007507$
        # - You've come here empty-handed. What are you talking about?
        return -1

    def __50(self, pick: int) -> int:
        # $script:1214150707007552$
        # - Do you not realize that you should be somewhere else?
        if pick == 0:
            # $script:1214150707007553$
            # - Yes. Send me to $map:63000050$.
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # functionID=2 
        # $script:1214150707007554$
        # - Heh heh heh... Off with you!
        return -1

    def __52(self, pick: int) -> int:
        # $script:1214150707007555$
        # - Why are you still empty-handed?
        return -1

    def __60(self, pick: int) -> int:
        # $script:1214150707007556$
        # - Come, come, tell me what you need. You won't be leaving empty-handed, heh heh heh...
        if pick == 0:
            # $script:1214150707007557$
            # - I bet you get lots of customers.
            return 61
        elif pick == 1:
            # $script:1214150707007558$
            # - Why the creep—er, cheery smile?
            return 62
        elif pick == 2:
            # $script:1214150707007559$
            # - I bet you have all kinds of weird stories.
            return 63
        return -1

    def __61(self, pick: int) -> int:
        # $script:1214150707007560$
        # - Of course, of course! I do not know why they come here, but I do so enjoy watching them skitter here and there.
        return -1

    def __62(self, pick: int) -> int:
        # $script:1214150707007561$
        # - Don't worry your little soul about that. You'll learn soon enough... even if you don't want to.
        return -1

    def __63(self, pick: int) -> int:
        # $script:1214150707007562$
        # - Enough to spend all night in the telling, and then some! So, what would you like to hear? The tale of a young monster slayer and his buxom mage companion? The story of how I've kept my youthful looks? Or... something else? 
        if pick == 0:
            # $script:1214150707007563$
            # - Something else! Please, something else.
            return 64
        return -1

    def __64(self, pick: int) -> int:
        if self.index == 0:
            # $script:1214150707007564$
            # - Ahhh, yes... I know just the tale for a squirmy adventurer like you. Listen close, dearie...
            return 64
        elif self.index == 1:
            # $script:1214150707007565$
            # - Legend has it that when the Shadow Seed takes root, a new son will be born unto the Demon King and darkness shall swallow the world. A lovely little tale, don't you think?
            if pick == 0:
                # $script:1214150707007566$
                # - You and I have different definitions of 'lovely.'
                return 65
            return -1
        return -1

    def __65(self, pick: int) -> int:
        # $script:1214150707007567$
        # - Blind little child! Lovely is in the eye of the beholder.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (43, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (62, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (63, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (64, 0):
            return Option.NEXT
        elif (self.state, self.index) == (64, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (65, 0):
            return Option.CLOSE
        return Option.NONE
