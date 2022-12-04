""" 11004090: Everfrost Star """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0622133907010321$
        # - <font color='#909090'>(This giant snowflake reflects the brilliant sun. No matter how brightly it shines, it never seems to melt.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0622133907010322$
            # - <font color='#909090'>(This giant snowflake reflects the brilliant sun. No matter how brightly it shines, it never seems to melt.)</font>
            return 10
        elif self.index == 1:
            # $script:0622133907010323$
            # - <font color='#909090'>(Tourists come from all over the world to see the local "Santa" who makes presents for good boys and girls. Taking your picture in front of the snow crystal is a trendy thing to do.)</font>
            return 10
        elif self.index == 2:
            # $script:0622133907010324$
            # - <font color='#909090'>(They say that the snow crystal is a reflection of the goodness and kindness that lives in the hearts of Santas everywhere.)</font>
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.NEXT
        elif (self.state, self.index) == (10, 2):
            return Option.CLOSE
        return Option.NONE
