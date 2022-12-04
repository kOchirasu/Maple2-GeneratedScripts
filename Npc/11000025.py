""" 11000025: Beth """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000138$
        # - What brings you here?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000139$
        # - You don't look like you're from around here. Did you come to see the court?
        if pick == 0:
            # $script:0831180407000140$
            # - Yep!
            return 11
        elif pick == 1:
            # $script:0831180407000141$
            # - That's none of your business.
            return 13
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000142$
            # - Oh, cool! I was planning on attending myself.
            return 11
        elif self.index == 1:
            # $script:0831180407000143$
            # - I asked my brother to see the court with me, but he was more interested in catching some kind of fish while they were in season. I suppose it's good that he didn't come, now that the road to $map:02000001$ is out.
            if pick == 0:
                # $script:0831180407000144$
                # - What happened to the road?
                return 12
            return -1
        return -1

    def __12(self, pick: int) -> int:
        # $script:0831180407000145$
        # - How could you not have heard? The Royal Road leading to $map:02000001$ was torn up by the earthquake the other day. Can't be good for holding court, y'know?
        return -1

    def __13(self, pick: int) -> int:
        # $script:0831180407000146$
        # - Hey, now. No need to be like that. I was just making conversation.
        return -1

    def __60(self, pick: int) -> int:
        # $script:1215100607009653$
        # - Fresh fish! We catch 'em, you buy 'em!
        if pick == 0:
            # $script:1215100607009654$
            # - I have something to ask you.
            return 61
        return -1

    def __61(self, pick: int) -> int:
        # $script:1215100607009655$
        # - Oh, all right. How can I help you, dear?
        if pick == 0:
            # $script:1215100607009656$
            # - What can you tell me about trading airships?
            return 62
        return -1

    def __62(self, pick: int) -> int:
        # $script:1215100607009657$
        # - You mean those new-fangled boats with wings? They show up in $map:02000062$ from time to time. I've gotta tell you, that's not a sight you'll soon forget.
        if pick == 0:
            # $script:1215100607009658$
            # - Have you heard anything about them... disappearing?
            return 63
        return -1

    def __63(self, pick: int) -> int:
        # $script:1215100607009659$
        # - Disappearing? Hm... The ones passing through $map:02000062$ never seem to have any trouble...
        if pick == 0:
            # $script:1215100607009660$
            # - Have you seen them fly?
            return 64
        return -1

    def __64(self, pick: int) -> int:
        # $script:1215100607009661$
        # - Well no, I've never actually seen one in flight. But I can't imagine why they'd have wings if they didn't fly!
        if pick == 0:
            # $script:1215100607009662$
            # - Thanks for the information.
            return 65
        return -1

    def __65(self, pick: int) -> int:
        # $script:1215100607009663$
        # - Let me know if you ever see one fly.
        if pick == 0:
            # $script:1215100607009664$
            # - It seems like the airships traveling by sea are fine...
            return 66
        return -1

    def __66(self, pick: int) -> int:
        # $script:1215100607009665$
        # - Uhh. Good? Now are you sure you don't want any fish?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (13, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (63, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (64, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (65, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (66, 0):
            return Option.CLOSE
        return Option.NONE
