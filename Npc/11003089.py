""" 11003089: Orde """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0207122607007932$
        # - It's hot! Too hot! Even the air-conditioning spell isn't helping.
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0207122607007933$
        # - Going from cold to hot so quick is not good for your health. Messes up your skin! And our skin is important for mages... helps us sense mana better.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.CLOSE
        return Option.NONE
