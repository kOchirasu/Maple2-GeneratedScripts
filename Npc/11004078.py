""" 11004078: Scribbles under the Bridge """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010226$
        # - <font color="#909090">(A teeny-tiny scribble written so small, it almost appears to be shy.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010227$
            # - <font color="#909090">(A teeny-tiny scribble written so small, it almost appears to be shy.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010228$
            # - <i>$npcName:11000015[gender:1]$'s secret, exposed! She actually has a boyfriend! We've been betrayed!</i>
            return 10
        elif self.index == 2:
            # $script:0619202207010229$
            # - <font color="#909090">(Is the person who wrote this... angry? $npcName:11000015[gender:1]$'s fans can be scary sometimes...)</font>
            return 10
        elif self.index == 3:
            # $script:0619202207010230$
            # - <font color="#909090">(Wait. There's another note written here!)</font>
            return 10
        elif self.index == 4:
            # $script:0619202207010231$
            # - <i>Interesting rumor. If you happen to meet my boyfriend, bring him to me. I want to know what he looks like.
            #   - $npcName:11000015[gender:1]$</i>
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
