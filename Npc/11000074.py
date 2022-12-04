""" 11000074: Karl """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000345$
        # - How may I help you?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180407000346$
        # - Ever since I was appointed minister, the most important person in my life has become $npcName:11000075[gender:1]$. I live to protect her and assist her in all her affairs. 
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180407000347$
        # - Your eyes tell me what kind of person you are, $MyPCName$, and so I believe I can trust you. Please continue to protect the peace of this world.
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180407000348$
        # - The Land of Darkness is but a stop on the way to the Shadow World. The only way to lock that terrible place away again is to restore the Blue Lapenta.
        return -1

    def __40(self, pick: int) -> int:
        # $script:1215110507009739$
        # - Do you need something?
        if pick == 0:
            # $script:1215110407009728$
            # - I've heard some unsettling rumors about $map:02000001$ lately.
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:1215110407009729$
        # - Bah, you don't listen to rumor and hearsay, do you?
        if pick == 0:
            # $script:1215110407009730$
            # - Well, I also have a photo...
            return 42
        return -1

    def __42(self, pick: int) -> int:
        # $script:1215110407009731$
        # - Oh. Hm... Curious...
        if pick == 0:
            # $script:1215110407009732$
            # - What can you tell me about the photo?
            return 43
        return -1

    def __43(self, pick: int) -> int:
        # $script:1215110407009733$
        # - Hard to say, with the photograph being as blurry as it is. But I think I've seen a similar creature depicted in a tome from my family's library.
        if pick == 0:
            # $script:1215110407009734$
            # - Go on...
            return 44
        return -1

    def __44(self, pick: int) -> int:
        if self.index == 0:
            # $script:1215110407009735$
            # - Long ago, the goddess of light did battle with a dark being, but she was unable to destroy him. The shapes in this picture are similar to its minions.
            return 44
        elif self.index == 1:
            # $script:1215110407009736$
            # - But that's impossible. That evil was banished from this world long ago.
            if pick == 0:
                # $script:1215110407009737$
                # - What else can you tell me about this "being?"
                return 45
            return -1
        return -1

    def __45(self, pick: int) -> int:
        # $script:1215110407009738$
        # - I've told you all I know. Hopefully I've answered your question. Now, if you don't mind, I have matters of state to attend to.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (44, 0):
            return Option.NEXT
        elif (self.state, self.index) == (44, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (45, 0):
            return Option.CLOSE
        return Option.NONE
