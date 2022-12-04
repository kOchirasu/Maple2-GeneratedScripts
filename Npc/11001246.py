""" 11001246: Ishura """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1203181207004692$
        # - Hmm?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1206021407004794$
        # - Ah, $MyPCName$! What a pleasant surprise.
        if pick == 0:
            # $script:1206021407004795$
            # - I have a few questions to ask.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1206021407004796$
        # - Certainly. What would you like to know? 
        if pick == 0:
            # $script:1206021407004797$
            # - What can you tell me about Arazaad?
            return 35
        elif pick == 1:
            # $script:1206021407004798$
            # - What can you tell me about $npcName:11001231[gender:0]$?
            return 32
        elif pick == 2:
            # $script:1211024207004974$
            # - When can we go home?
            return 38
        return -1

    def __32(self, pick: int) -> int:
        # $script:1206021407004799$
        # - Sigh... I'd rather not talk about him, but I suppose you need all the information you can get.
        if pick == 0:
            # $script:1206021407004800$
            # - But I thought you and $npcName:11001231[gender:0]$ were friends.
            return 33
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:1206021407004801$
            # - There was a time long ago that was true, but... well, you know Terrun Calibre's history. I supposed the rift that grew between us was inevitable. The Jibricia value rune magic above all, while the Pelgia prize swordsmanship. And rather than work in harmony, they fight like children.
            return 33
        elif self.index == 1:
            # $script:1206021407004802$
            # - From an early age, $npcName:11001231[gender:0]$ had shown an incredible aptitude for the three elements. It wasn't long before the Jibricia took notice of him. Nor did it take long for him to climb to the top of the sect.
            if pick == 0:
                # $script:1206021407004803$
                # - But how did you and $npcName:11001231[gender:0]$ become friends?
                return 34
            return -1
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:1206021407004804$
            # - He was Jibricia and I was Pelgia. And though our sects were bitterly opposed to one another, $npcName:11001231[gender:0]$ and I recognized in each other a kindred spirit. Our elders forbade us from meeting, but that didn't dissuade us. We had such big plans. You know, we truly believe we could find a way to end the conflict.
            return 34
        elif self.index == 1:
            # $script:1206021407004805$
            # - We would stay up all night, just talking. He was a talented warrior and the strongest of the Eight Blades. Together, I was sure we could really accomplish all the things we used to discuss...
            return 34
        elif self.index == 2:
            # $script:1206021407004806$
            # - Even with the passage of time, I still had hope. I dreamed of building a new future for Terrun Calibre with him...
            return 34
        elif self.index == 3:
            # $script:1206021407004807$
            # - Of course, my dream was destroyed when he killed Arazaad. He crossed a line from which he could never return. And now, I can't help but wonder if there was some sign I could have missed...
            return -1
        return -1

    def __35(self, pick: int) -> int:
        if self.index == 0:
            # $script:1206021407004808$
            # - Arazaad was an admirable man. Not only was he the leader of our sect, Pelgia, but as Elder Blade he was the leader of all Terrun Calibre. This was a source of conflict on both sides. All Arazaad wanted was peace. Though the fighting between the two sects began with the elders, in the end it was Arazaad who took the blame.
            return 35
        elif self.index == 1:
            # $script:1206021407004809$
            # - Some called Arazaad a hypocrite, but the man was nothing short of an inspiration. Even though $npcName:11001231[gender:0]$ was among the leader of our rival sect, the Jibricia, he still looked up to Arazaad.
            return 35
        elif self.index == 2:
            # $script:1206021407004810$
            # - Of course, $npcName:11001231[gender:0]$ was <i>not</i> Arazaad's most trusted student.
            if pick == 0:
                # $script:1206021407004811$
                # - Let me guess, it was you.
                return 36
            return -1
        return -1

    def __36(self, pick: int) -> int:
        # $script:1206021407004812$
        # - Ha! So often did I wish that I were. No, Arazaad's prized student was $npcName:11001230[gender:0]$.
        if pick == 0:
            # $script:1206021407004813$
            # - $npcName:11001230[gender:0]$? Really? I would have never guessed.
            return 37
        return -1

    def __37(self, pick: int) -> int:
        if self.index == 0:
            # $script:1206021407004814$
            # - I can't blame you, he certainly doesn't act the part. Initially, Arazaad tried to keep $npcName:11001230[gender:0]$ on a tight leash. But the more defiant $npcName:11001230[gender:0]$ became, the more attention he got from Arazaad.
            return 37
        elif self.index == 1:
            # $script:1206021407004815$
            # - And now he's the acting Elder Blade of Terrun Calibre. In any case, I've said more than I should have. It wouldn't be right to discuss such things without him here to share his side of the story.
            return -1
        return -1

    def __38(self, pick: int) -> int:
        # $script:1211024207004975$
        # - You miss Calibre Island already? Don't fret, I'm sure we'll be able to return... someday.
        if pick == 0:
            # $script:1211024207004976$
            # - Why can't we go back now?
            return 39
        return -1

    def __39(self, pick: int) -> int:
        # $script:1211024207004977$
        # - Simply reaching the island requires massive amounts of rune mana, and there isn't much to be found in a place like this. Our only hope of returning is in finding all the pieces of the Wisdom of the Baaz.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.NEXT
        elif (self.state, self.index) == (34, 2):
            return Option.NEXT
        elif (self.state, self.index) == (34, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (35, 0):
            return Option.NEXT
        elif (self.state, self.index) == (35, 1):
            return Option.NEXT
        elif (self.state, self.index) == (35, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (36, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (37, 0):
            return Option.NEXT
        elif (self.state, self.index) == (37, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (38, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (39, 0):
            return Option.CLOSE
        return Option.NONE
