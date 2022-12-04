""" 11000745: Ghanush """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002891$
        # - Do you think you can beat me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407002894$
        # - Do you want to challenge me? You know how to play rock-paper-scissors, right? Heh, let's do it. Rock, paper, scissors!
        if pick == 0:
            # $script:0831180407002895$
            # - Scissors!
            # TODO: goto 31,32,33,34,35
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180407002896$
            # - Rock!
            # TODO: goto 36,37,38,39,40
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180407002897$
            # - Paper!
            # TODO: goto 41,42,43,44,45
            self.close()
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180407002898$
        # - <font color="#909090">(She plays scissors.)</font>
        #   We tied. Not bad. Do you want to try again?
        if pick == 0:
            # $script:0831180407002899$
            # - Again!
            return 50
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180407002900$
        # - <font color="#909090">(She plays scissors.)</font>
        #   We tied. Why don't you try again?
        if pick == 0:
            # $script:0831180407002901$
            # - Again!
            return 50
        return -1

    def __33(self, pick: int) -> int:
        # $script:0831180407002902$
        # - <font color="#909090">(She plays rock.)</font>
        #   I won. Looks like you're no match for me either.
        if pick == 0:
            # $script:0831180407002903$
            # - Again!
            return 50
        return -1

    def __34(self, pick: int) -> int:
        # $script:0831180407002904$
        # - <font color="#909090">(She plays rock.)</font>
        #   I won. What's wrong, cat got your tongue? Oh, right... losers don't get to speak! Hee hee... Want to play again?
        if pick == 0:
            # $script:0831180407002905$
            # - Again!
            return 50
        return -1

    def __35(self, pick: int) -> int:
        # $script:0831180407002906$
        # - <font color="#909090">(She plays paper.)</font>
        #   Oh no, I lost! I can't believe it!
        if pick == 0:
            # $script:0831180407002907$
            # - I won!
            return 46
        return -1

    def __36(self, pick: int) -> int:
        # $script:0831180407002908$
        # - <font color="#909090">(She plays scissors.)</font>
        #   D-did I really just lose?
        if pick == 0:
            # $script:0831180407002909$
            # - I won!
            return 46
        return -1

    def __37(self, pick: int) -> int:
        # $script:0831180407002910$
        # - <font color="#909090">(She plays rock.)</font>
        #   We tied. This isn't over. Let's go again!
        if pick == 0:
            # $script:0831180407002911$
            # - Again!
            return 50
        return -1

    def __38(self, pick: int) -> int:
        # $script:0831180407002912$
        # - <font color="#909090">(She plays rock.)</font>
        #   We tied. Not bad. Do you want to try again?
        if pick == 0:
            # $script:0831180407002913$
            # - Again!
            return 50
        return -1

    def __39(self, pick: int) -> int:
        # $script:0831180407002914$
        # - <font color="#909090">(She plays paper.)</font>
        #   I won. Seems I can't find a good match for me here, either. Do you want to try again?
        if pick == 0:
            # $script:0831180407002915$
            # - Again!
            return 50
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407002916$
        # - <font color="#909090">(She plays paper.)</font>
        #   I'm tired of winning. I'm willing to play you one more time, though. What do you say?
        if pick == 0:
            # $script:0831180407002917$
            # - Again!
            return 50
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180407002918$
        # - <font color="#909090">(She plays scissors.)</font>
        #   I won. As expected. Do you want to try again?
        if pick == 0:
            # $script:0831180407002919$
            # - Again!
            return 50
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407002920$
        # - <font color="#909090">(She plays scissors.)</font>
        #   Ahhh... Winning doesn't excite me anymore. Do you want to try again?
        if pick == 0:
            # $script:0831180407002921$
            # - Again!
            return 50
        return -1

    def __43(self, pick: int) -> int:
        # $script:0831180407002922$
        # - <font color="#909090">(She plays rock.)</font>
        #   N-no way... D-did I really lose?
        if pick == 0:
            # $script:0831180407002923$
            # - Again!
            return 46
        return -1

    def __44(self, pick: int) -> int:
        # $script:0831180407002924$
        # - <font color="#909090">(She plays paper.)</font>
        #   Err? We tied. Let's try again!
        if pick == 0:
            # $script:0831180407002925$
            # - Again!
            return 50
        return -1

    def __45(self, pick: int) -> int:
        # $script:0831180407002926$
        # - <font color="#909090">(She plays paper.)</font>
        #   Hmph, tying is no fun. Let's try again.
        if pick == 0:
            # $script:0831180407002927$
            # - Yes!
            return 50
        return -1

    def __46(self, pick: int) -> int:
        # $script:0831180407002928$
        # - <font color="#909090">(She gives you a sideways scowl.)</font> 
        #   I think you played after I did. You're lucky that my eyes are too old to see clearly.
        if pick == 0:
            # $script:0831180407002929$
            # - Don't you have something for me?
            # TODO: goto 47,48
            # TODO: gotoFail 49
            return 49
        return -1

    def __47(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180407002930$
        # - <font color="#909090">(Her scowl deepens.)</font>
        #   Here!
        return -1

    def __48(self, pick: int) -> int:
        # $script:0831180407002931$
        # - I already gave you your prize!
        return -1

    def __49(self, pick: int) -> int:
        # $script:0831180407002932$
        # - You'd better lighten your bag first if you want a prize.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407002933$
        # - Let's get to it! Rock, paper, scissors!
        if pick == 0:
            # $script:0831180407002934$
            # - Scissors!
            # TODO: goto 31,32,33,34,35
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180407002935$
            # - Rock!
            # TODO: goto 36,37,38,39,40
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180407002936$
            # - Paper!
            # TODO: goto 41,42,43,44,45
            self.close()
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407002937$
        # - Do you know how to play rock-paper-scissors? It's a little more complex than making funny shapes with your hand.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (35, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (37, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (38, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (39, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (44, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (45, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (46, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (47, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (48, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (49, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
