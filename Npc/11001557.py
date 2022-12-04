""" 11001557: Junta """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0617105607006361$
        # - Have you been training? Answer carefully.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0727223007006796$
        # - Get to the point.
        if pick == 0:
            # $script:0727223007006797$
            # - I want to know the secrets of animus.
            return 40
        elif pick == 1:
            # $script:0727223007006798$
            # - Tell me about last year's incident.
            return 50
        elif pick == 2:
            # $script:0727223007006799$
            # - Why aren't there more students of Guidance?
            return 60
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006800$
            # - Knowledge is just as important as strength. For that reason, I will answer your questions, no matter how stupid they are. Don't make me repeat myself.
            return 40
        elif self.index == 1:
            # $script:0727223007006801$
            # - Animus is both the core philosophy and the energy developed by the Lone Spirit, who founded our order long ago. When you become one with nature, you can harness this energy and turn it into martial power.
            return 40
        elif self.index == 2:
            # $script:0727223007006802$
            # - The outsiders wield a similar force that they call magic. Animus is more powerful, of course, but it takes years of dedicated training to master.
            #   <font color="#909090">(He eyes you coolly.)</font>
            if pick == 0:
                # $script:0727233607006912$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006803$
            # - The master and I were traveling the Land of Darkness on a training journey when we heard a series of explosions. We followed the sound and found you, dying.
            return 50
        elif self.index == 1:
            # $script:0727233607006913$
            # - I didn't even realize you were alive at first, you were so close to death. The master tried to cure you, but you were too far gone.
            return 50
        elif self.index == 2:
            # $script:0727223007006804$
            # - The master refused to let you die. He channeled his animus into you so that you would live. Do you understand what that means?
            if pick == 0:
                # $script:0727223007006805$
                # - No.
                return 51
            elif pick == 1:
                # $script:0727223007006806$
                # - Yes.
                return 52
            return -1
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006807$
            # - If you don't understand your roots, you will never know wisdom. If you don't show gratitude, you will never know humanity. And you... You know neither. So just listen and nod.
            return 51
        elif self.index == 1:
            # $script:0727223007006808$
            # - I begged him not to, but he gave you a portion of his power. He didn't simply heal you... he transferred his animus into you. Animus developed over centuries of training.
            return 51
        elif self.index == 2:
            # $script:0727223007006809$
            # - I don't understand why the master was so determined to save you, but your life is his now. The only way to repay him is to train as hard as you can and become a great student of Guidance.
            if pick == 0:
                # $script:0727233607006914$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __52(self, pick: int) -> int:
        # $script:0727223007006810$
        # - If you knew that, maybe you wouldn't have slacked off in your training so much! Did you really think I wouldn't notice? You need to put your all into it!
        if pick == 0:
            # $script:0727233607006915$
            # - Let's talk about something else.
            return 30
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006811$
            # - There is only you, myself, and $npcName:11001699[gender:1]$. Does it bother you that there are only three of us?
            return 60
        elif self.index == 1:
            # $script:0727223007006812$
            # - When I joined Guidance, there were quite a few students. In its heyday, the mountain was teeming with them.
            if pick == 0:
                # $script:0727223007006813$
                # - Where did they all go?
                return 61
            return -1
        return -1

    def __61(self, pick: int) -> int:
        if self.index == 0:
            # $script:0727223007006814$
            # - They left for various reasons. Some thought the training was too hard. Others left to join the world of humans after their training journey. A few only wanted to learn some simple tricks, and left as soon as they'd done so.
            return 61
        elif self.index == 1:
            # $script:0727223007006815$
            # - A few of our former students created their own group in the outside world. If they couldn't make it here, I doubt they'd have much success on their own. They certainly wouldn't hold to our values of integrity and righteousness...
            return 61
        elif self.index == 2:
            # $script:0727223007006816$
            # - What did they call themselves? The Blackwinds? The Jaw Smashers? Something insane like that. Let their mistakes be a reminder to stay on the path of training.
            if pick == 0:
                # $script:0727233607006916$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.SELECTABLE_DISTRACTOR
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.NEXT
        elif (self.state, self.index) == (61, 1):
            return Option.NEXT
        elif (self.state, self.index) == (61, 2):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
