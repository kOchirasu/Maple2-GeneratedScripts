""" 11004079: Tellah """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0620203007010255$
        # - Rain, rain, go away. Go away forever.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0620203007010256$
            # - Rain, rain, go away. Go away forever.
            return 10
        elif self.index == 1:
            # $script:0620203007010257$
            # - Oh, a passing adventurer. Why don't you take a break and chat with me?
            if pick == 0:
                # $script:0620203007010258$
                # - Okay. Know any stories?
                return 31
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0620203007010259$
        # - Well, I can tell you <i>your</i> story, if you like. You've been pushing forward without rest. But do you really know where you're going?
        if pick == 0:
            # $script:0620203007010260$
            # - What do you mean?
            return 32
        return -1

    def __32(self, pick: int) -> int:
        # $script:0620203007010261$
        # - I've been here for over a century. I know many things, including things about <i>you</i>. What would you like to know?
        if pick == 0:
            # $script:0620203007010262$
            # - Tell me about my future.
            return 33
        elif pick == 1:
            # $script:0620203007010263$
            # - Will I ever find true love?
            return 34
        elif pick == 2:
            # $script:0620203007010264$
            # - How did Maple World come to be?
            return 35
        return -1

    def __33(self, pick: int) -> int:
        # $script:0620203007010265$
        # - I tell you I know things, and you assume I'm a darned prophet. Ha! Okay, I'll play along. I see much potential in you, my friend. Your future holds many great things.
        if pick == 0:
            # $script:0626201407010371$
            # - ...
            return 36
        return -1

    def __34(self, pick: int) -> int:
        # $script:0620203007010266$
        # - And what would I know about love? I've been alone my entire life...
        if pick == 0:
            # $script:0626201407010372$
            # - Are you making this up?
            return 37
        return -1

    def __35(self, pick: int) -> int:
        # $script:0620203007010267$
        # - Why are you asking me? Didn't someone fill you in when you first started your adventure? Something about two goddesses and the birth of $npcName:11000075[gender:1]$.
        if pick == 0:
            # $script:0626201407010373$
            # - I think I remember that.
            return 40
        return -1

    def __36(self, pick: int) -> int:
        if self.index == 0:
            # $script:0626201407010374$
            # - Live long enough, and you begin to lose perspective on good and evil—right and wrong. The hero of yesterday can become the villain of tomorrow.
            return 36
        elif self.index == 1:
            # $script:0626201407010375$
            # - I can't say whether the future will be good or bad, but now... for now, you are magnificent.
            return 36
        elif self.index == 2:
            # $script:0626201407010376$
            # - I like to think that everything will work out for people who live their lives with conviction and purpose. You may not believe me now, but someday you'll think back on this old turtle's words and understand.
            return -1
        return -1

    def __37(self, pick: int) -> int:
        # $script:0626201407010377$
        # - That's not to say I've never been in love. There was someone in my life... but she passed away in an accident. I never mustered up the courage to tell her how I felt...
        if pick == 0:
            # $script:0626201407010378$
            # - Sorry. I didn't mean to stir up bad memories.
            return 38
        return -1

    def __38(self, pick: int) -> int:
        # $script:0626201407010379$
        # - Oh, it's all in the past now. Perhaps, when I leave behind this mortal coil, I'll see her again. It's something that gives me hope, anyway.
        if pick == 0:
            # $script:0626201407010380$
            # - I'm sure you'll see her again.
            return 39
        return -1

    def __39(self, pick: int) -> int:
        # $script:0626201407010381$
        # - That's kind of you to say. If I were to give you any advice, it would be this—don't follow in my footsteps. When you find someone you love, tell them how you feel. Don't live your whole life wondering what could have been...
        return -1

    def __40(self, pick: int) -> int:
        # $script:0626201407010382$
        # - The goddess of light may be gone, but the remnants of her power permeate this world. It is up to you to help the empress carry that blessed light on into the future.
        if pick == 0:
            # $script:0626201407010383$
            # - How'd you know I'm helping the empress?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0626201407010384$
        # - Oh, you don't get to my age without learning how to keep your ears open.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
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
            return Option.NEXT
        elif (self.state, self.index) == (36, 1):
            return Option.NEXT
        elif (self.state, self.index) == (36, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (37, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (38, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (39, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
