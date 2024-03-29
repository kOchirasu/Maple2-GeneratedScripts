""" 11004065: Rainbow Bridge """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010121$
        # - <font color="#909090">(This big, beautiful sculpture spans the lake at $map:02000038$. There's a plaque bearing an inscription on top.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010122$
            # - <font color="#909090">(This big, beautiful sculpture spans the lake at $map:02000038$. There's a plaque bearing an inscription on top.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010123$
            # - <i>The "Rainbow Bridge" is the final work of Mandy, the genius architect responsible for the design of numerous famous buildings. Its purpose, and the significance of its design may never be known, as construction didn't start until after her death.</i>
            return 10
        elif self.index == 2:
            # $script:0619202207010124$
            # - <i>The fact that the arch was constructed with such unusual materials—and that it is called a bridge despite functioning more as an obstacle than a pathway—are hallmarks of Mandy's famed eccentricity.</i>
            return 10
        elif self.index == 3:
            # $script:0619202207010125$
            # - <i>Local legends tell of a portal to a magical land on the shore below the bridge's construction site.</i>
            return 10
        elif self.index == 4:
            # $script:0619202207010126$
            # - <i>Whether you find this portal or not, we hope you enjoy the beautiful scenery here on the Rainbow Bridge.</i>
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
