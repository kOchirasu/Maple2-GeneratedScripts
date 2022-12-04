""" 11000119: Frey """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50, 70, 120])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000508$
        # - What brings you here?
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0831180407000512$
        # - The Royal Guard protects $npcName:11000075[gender:1]$ and all of $map:02000001$. So long as there are threats to peace in this world, we will not rest.
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000513$
            # - Maybe it's time I told you the truth about why the court was canceled. Just before it was scheduled to start, the leadership met to discuss the details of the proceedings. Suddenly, a bloodied guard stumbled into the meeting and said that the court must be canceled.
            return 50
        elif self.index == 1:
            # $script:0831180407000514$
            # - We were shocked, as you might imagine. And before we could question him further, a dagger flew in from a nearby window and took his life. There, before our very eyes...
            return 50
        elif self.index == 2:
            # $script:0831180407000515$
            # - Everyone rushed to find the assailant, but we could find nothing. Our conclusion was that there must be a spy in the palace. The servants of the demon king were plotting something in time for the court. We had to cancel it.
            if pick == 0:
                # $script:0831180407000516$
                # - Why didn't you tell anyone what happened?
                return 51
            return -1
        return -1

    def __51(self, pick: int) -> int:
        # $script:0831180407000517$
        # - You expect us to tell the public that someone was murdered, right in the middle of a meeting like that? People have only just started to calm down after the loss of the Blue Lapenta, we don't need to be riling them back up so soon. 
        return -1

    def __70(self, pick: int) -> int:
        # $script:1215105107009695$
        # - $MyPCName$, what brings you here?
        if pick == 0:
            # $script:1215105107009696$
            # - $npcName:11003534$ sent me.
            return 71
        return -1

    def __71(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215105107009697$
            # - After all this time as the Guard Captain, $npcName:11003534[gender:0]$ still treats me like a child.
            return 71
        elif self.index == 1:
            # $script:1215105107009698$
            # - You go and tell $npcName:11003534$ that I'll do whatever's necessary to protect $npc:11000075[gender:1]$ and $npcName:11000601[gender:1]$. I swore an oath, and on my life I intend to keep it.
            if pick == 0:
                # $script:1215105107009699$
                # - Uh, I'm actually here to ask about the rumors going around $map:02000001$.
                return 72
            return -1
        return -1

    def __72(self, pick: int) -> int:
        # $script:1215105107009700$
        # - Ugh, not you too. These rumors are giving me a headache. I've upped security and tripled patrols to reassure the public, yet the rumors continue to spread.
        if pick == 0:
            # $script:1215105107009701$
            # - And what about the truth behind the rumors?
            return 73
        return -1

    def __73(self, pick: int) -> int:
        # $script:1215105107009702$
        # - I'll tell you the same thing I told the former captain of the Knights when he stopped by. I don't know anything! If we had any insight into the circumstances behind the rumors, the alliance would be the first to know.
        if pick == 0:
            # $script:1215105107009703$
            # - The former captain?
            return 74
        return -1

    def __74(self, pick: int) -> int:
        # $script:1215105107009704$
        # - Ah, it's nothing. Don't worry about it.
        if pick == 0:
            # $script:1215105107009705$
            # - Okay.
            return 75
        return -1

    def __75(self, pick: int) -> int:
        # $script:1215105107009706$
        # - I'm sorry I couldn't be of more help.
        return -1

    def __120(self, pick: int) -> int:
        # $script:0831180407000518$
        # - Some people are curious about my relationship with $npcName:11000076[gender:0]$. It's... quite complicated. I'd rather not get into it.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (71, 0):
            return Option.NEXT
        elif (self.state, self.index) == (71, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (72, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (73, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (74, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (75, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (120, 0):
            return Option.CLOSE
        return Option.NONE
