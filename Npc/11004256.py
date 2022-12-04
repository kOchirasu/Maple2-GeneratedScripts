""" 11004256: Mysterious Medicine """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0829171107010972$
        # - <font color="#909090">(Pills and liquids in an assortment of colors lay scattered about.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0829171107010973$
            # - <font color="#909090">(Pills and liquids in an assortment of colors lay scattered about.)</font>
            return 10
        elif self.index == 1:
            # $script:0831140807011022$
            # - <font color="#909090">(A brief note can be found next to each item.)</font>
            #   <font color="#ffd200">Cure-all Anesthetic Ver. 2</font>
            #   Prevents blood clots, relieves fever and pain. Effective on muscle pain. Take up to 3 pills per day. Symptoms should abate within 2 days.
            return 10
        elif self.index == 2:
            # $script:0831140807011023$
            # - <font color="#ffd200">Goldus Pharmaceutical's Digest+ Tab Ver. 5</font>
            #   Aids with indigestion, loss of appetite, and overeating. Note for next test session: must be swallowed whole. DO NOT CHEW! Consume 3 times daily, with meals. Take for 3 full days for best results.
            return 10
        elif self.index == 3:
            # $script:0831140807011024$
            # - <font color="#ffd200">Yellow Skin Goo (Name Pending)</font>
            #   Minimizes appearance of eczema. Ointment should also treat folliculitis, boils, and acne, but the tests will tell for sure. Clean affect area, apply twice a day. Or, apply on a clean gauze and staple to skin. Wait, tape might be better.
            return 10
        elif self.index == 4:
            # $script:0831140807011025$
            # - <font color="#ffd200">Ludi-solver (Experimental Solvent)</font>
            #   Slows down or reverses the ludibrification process. NOT TO BE USED ON HUMANS. For inanimate object only. Ingredients extremely toxic.
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.NEXT
        elif (self.state, self.index) == (10, 3):
            return Option.NEXT
        elif (self.state, self.index) == (10, 4):
            return Option.CLOSE
        return Option.NONE
