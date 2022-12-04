""" 11004077: Blackstar Hideout """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010220$
        # - <font color="#909090">(Pressing your ear to the door, you hear some Blackstar gangsters talking.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010221$
            # - <font color="#909090">(Pressing your ear to the door, you hear some Blackstar gangsters talking.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010222$
            # - <font color="#f45342">The big party's tomorrow. You get that cake for Haren yet?</font>
            return 10
        elif self.index == 2:
            # $script:0619202207010223$
            # - <font color="#41f441">I'm workin' on it! That bakery ya sent me to ain't exactly quick. You know they take orders years in advance?</font>
            return 10
        elif self.index == 3:
            # $script:0619202207010224$
            # - <font color="#41f441">Wait a sec. This is for Haren? I told 'em to put Min's name on the cake!</font>
            return 10
        elif self.index == 4:
            # $script:0619202207010225$
            # - <font color="#f45342">You <b>what?!</b> Chen's gonna smash my head in when he sees we messed up Haren's birthday bash!</font>
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
