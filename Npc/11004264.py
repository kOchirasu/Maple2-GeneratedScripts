""" 11004264: Khalifa Building """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0911203207011188$
        # - <font color="#909090">(This is the directory to the $npcName:11004264$.)</font>
        #   <i>Welcome to $npcName:11004264$, the pride of $map:02010002$! As the biggest multiplex shopping center on Karkar Island, we have what you're looking for!</i>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0911203207011189$
            # - <font color="#909090">(This is the directory to the $npcName:11004264$.)</font>
            #   <i>Welcome to $npcName:11004264$, the pride of $map:02010002$! As the biggest multiplex shopping center on Karkar Island, we have what you're looking for!</i>
            return 10
        elif self.index == 1:
            # $script:0911203207011190$
            # - <font color="#ffd200">1F</font>
            #   <i>Cosmetics, Accessories, General Merchandise
            #   Offering a truly premium shopping experience, with direct imports from all over Maple World.</i>
            return 10
        elif self.index == 2:
            # $script:0911203207011191$
            # - <font color="#ffd200">2F</font>
            #   <i>Fashion, Shoes, Handbags
            #   The hottest brands from all over the world in one place.</i>
            return 10
        elif self.index == 3:
            # $script:0911203207011192$
            # - <font color="#ffd200">3F</font>
            #   <i>Youth Fashion
            #   The latest trends, straight from the streets.</i>
            return 10
        elif self.index == 4:
            # $script:0911203207011193$
            # - <font color="#ffd200">4F</font>
            #   <i>Sports
            #   Sportswear and supplies to help you and your family stay in shape.</i>
            return 10
        elif self.index == 5:
            # $script:0911203207011194$
            # - <font color="#ffd200">5F</font>
            #   <i>Men's Fashion
            #   A careful curation of the best men's brands in fashion, tech, and accessories.</i>
            return 10
        elif self.index == 6:
            # $script:0911203207011195$
            # - <font color="#ffd200">6F</font>
            #   <i>Kids, Food Court
            #   From toys to fashion, everything a kid could want. Don't forget to check out the premium restaurants, perfect for any palette.</i>
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
            return Option.NEXT
        elif (self.state, self.index) == (10, 5):
            return Option.NEXT
        elif (self.state, self.index) == (10, 6):
            return Option.CLOSE
        return Option.NONE
