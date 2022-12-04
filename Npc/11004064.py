""" 11004064: Molten Fountain """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010113$
        # - <font color="#909090">(This fountain is built directly into the $map:02000046$. A steady supply of molten lava gushes from its basin.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010114$
            # - <font color="#909090">(This fountain is built directly into the $map:02000046$. A steady supply of molten lava gushes from its basin.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010115$
            # - <font color="#909090">(A field journal's been left next to the fountain. It has Silver Wolf's name on it.)
            return 10
        elif self.index == 2:
            # $script:0619202207010116$
            # - <i>For generations, we believed $map:02000046$ was a natural formation. However, I'm beginning to think otherwise...</i>
            return 10
        elif self.index == 3:
            # $script:0619202207010117$
            # - <i>While scouting out the area, I noticed that the lava flows in a precise circular path. I scouted out the nearby cave systems, and I can find no source of the lava underground.</i>
            return 10
        elif self.index == 4:
            # $script:0619202207010118$
            # - <i>This must be the work of powerful magic. If that's the case, then whoever did this must be trying to protect something within the Hourglass.</i>
            return 10
        elif self.index == 5:
            # $script:0619202207010119$
            # - <i>I still don't know </i>why<i> the lava is circling the mountain, but whatever the reason, I'm sure it's important. And perhaps valuable...</i>
            return 10
        elif self.index == 6:
            # $script:0619202207010120$
            # - <i>There's a lost temple that was used as a tomb for the great chieftains in ages past. Could this actually be the site of that temple? And how does one get inside...?</i>
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
