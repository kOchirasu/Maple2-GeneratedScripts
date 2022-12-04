""" 11001278: Shun """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1208175407004838$
        # - The Baaz watch over us all.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:1211023307004939$
        # - The Baaz watch over us all.
        if pick == 0:
            # $script:1211023307004940$
            # - I have some questions.
            return 31
        return -1

    def __31(self, pick: int) -> int:
        # $script:1211023307004941$
        # - What would you like to ask?
        if pick == 0:
            # $script:1211023307004942$
            # - How did Terrun Calibre get started?
            return 40
        elif pick == 1:
            # $script:1211023307004943$
            # - Why are there sects in Terrun Calibre?
            return 50
        elif pick == 2:
            # $script:1211023307004944$
            # - What are the Eight Blades?
            return 60
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1211023307004945$
            # - Long ago, there lived two masters: a rune mage and a swordsman. Each was convinced that their art was the greater of the two, and so they had a duel. When they proved to be evenly matched, they decided to merge their martial arts and established Terrun Calibre to teach their new fighting style.
            return 40
        elif self.index == 1:
            # $script:1211023307004946$
            # - These were the first Runeblades, Jibritta and Pelgia. Together, they created a legacy of master warrior-mages.
            return 40
        elif self.index == 2:
            # $script:1211023307004947$
            # - They realized they could never reach true mastery of the new fighting style in their lifetime, so instead they focused on recruiting and training skilled warriors. Terrun Calibre continues that tradition to this day.
            if pick == 0:
                # $script:1211023307004948$
                # - I have another question.
                return 70
            return -1
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:1211023307004949$
            # - Every Runeblade knows the names of the first masters, Jibritta and Pelgia. But before these two founded Terrun Calibre, they already had martial arts schools of their own.
            return 50
        elif self.index == 1:
            # $script:1211023307004950$
            # - Not all of their students agreed with the vision of combining rune magic and swordsmanship. Even though these schools were united under Terrun Calibre, the original students of each tradition continued to bump heads.
            return 50
        elif self.index == 2:
            # $script:1211023307004951$
            # - Today, the Runeblades have embraced the combination of magic and martial skill, but these old factions remain—and so do the old loyalties.
            return 50
        elif self.index == 3:
            # $script:1211023307004952$
            # - The members of the Jibritta Sect believe in the superiority of a learned mind, and devote themselves to mastery of the elements. Those in the Pelgia Sect, on the other hand, value physical strength, and spend countless hours honing their bodies into a tool of blade and magic.
            return 50
        elif self.index == 4:
            # $script:1211030007004978$
            # - Each sect has its own leader. Before Arazard was killed, he was the leader of both the Pelgias Sect and Terrun Calibre as a whole, which was unheard of.
            return 50
        elif self.index == 5:
            # $script:1211023307004953$
            # - When $npcName:11001231[gender:0]$ was the leader of the Jibritta Sect, the tension between the two factions reached a new height.
            if pick == 0:
                # $script:1211023307004954$
                # - Which sect do the scouts belong to?
                return 51
            return -1
        return -1

    def __51(self, pick: int) -> int:
        # $script:1211023307004955$
        # - $npcName:11001265[gender:1]$ was one of the sixteen disciples of Arazard, which makes her a Pelgia. But most of the scouts under her are Jibritta.
        if pick == 0:
            # $script:1211023307004956$
            # - But aren't the Jibritta the ones who started this mess?
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:1211023307004957$
        # - No, attitudes like <i>that</i> did. $npcName:11001231[gender:0]$ may have led the Jibritta Sect, but not all Jibritta agree with him. I'm a Jibritta myself, and I'd like nothing more than to see him brought to justice.
        if pick == 0:
            # $script:1211023307004958$
            # - I have another question.
            return 70
        return -1

    def __60(self, pick: int) -> int:
        # $script:1211023307004959$
        # - The eight greatest Runeblades of each generation are named the Eight Blades. They represent the strength of Terrun Calibre. 
        if pick == 0:
            # $script:1211023307004960$
            # - So, how strong are they?
            return 61
        return -1

    def __61(self, pick: int) -> int:
        if self.index == 0:
            # $script:1211023307004961$
            # - I think you know the answer to that already. Your teacher is one of them.
            return 61
        elif self.index == 1:
            # $script:1211023307004962$
            # - $npc:11001246[gender:0]$ is probably one of the five strongest Runeblades of all time. And you'd better believe that $npcName:11001230[gender:0]$ is just as strong.
            if pick == 0:
                # $script:1211023307004963$
                # - So, who's the very strongest?
                return 62
            return -1
        return -1

    def __62(self, pick: int) -> int:
        # $script:1211023307004964$
        # - In terms of skill alone, it would have to be $npcName:11001231[gender:0]$. He's a genius and the best of this generation's Eight Blades. But he betrayed us, and so his genius has become Terrun Calibre's greatest shame.
        if pick == 0:
            # $script:1211023307004965$
            # - I have another question.
            return 70
        return -1

    def __70(self, pick: int) -> int:
        # $script:1211023307004966$
        # - Is there anything else you want to ask?
        if pick == 0:
            # $script:1211023307004967$
            # - How did Terrun Calibre get started?
            return 40
        elif pick == 1:
            # $script:1211023307004968$
            # - Why are there sects in Terrun Calibre?
            return 50
        elif pick == 2:
            # $script:1211023307004969$
            # - What are the Eight Blades?
            return 60
        elif pick == 3:
            # $script:1211023307004970$
            # - I need to be going.
            return 71
        return -1

    def __71(self, pick: int) -> int:
        # $script:1211023307004971$
        # - May the Baaz guide you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
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
            return Option.NEXT
        elif (self.state, self.index) == (50, 3):
            return Option.NEXT
        elif (self.state, self.index) == (50, 4):
            return Option.NEXT
        elif (self.state, self.index) == (50, 5):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.NEXT
        elif (self.state, self.index) == (61, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (71, 0):
            return Option.CLOSE
        return Option.NONE
