""" 11004067: Chalk Graffiti """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0619202207010135$
        # - <font color="#909090">(You see a message that appears to be written in chalk.)</font>
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0619202207010136$
            # - <font color="#909090">(You see a message that appears to be written in chalk.)</font>
            return 10
        elif self.index == 1:
            # $script:0619202207010137$
            # - <font color="#909090">(The writing is barely legible.)</font>
            #   <i>Ah, my love, my love! Your blue eyes and wavy golden hair haunt me! There's no way you could know my feelings, but my heart will explode if I don't write them down!</i>
            return 10
        elif self.index == 2:
            # $script:0619202207010138$
            # - <i>Are you an angel? I heard a tale that you were born from the goddess of light, but to me, you </i>are<i> the goddess of light!</i>
            return 10
        elif self.index == 3:
            # $script:0619202207010139$
            # - <i>Can you blame me if I despise F? He is the only one who can be near you. Although I'm just one of many guards right now, one day I will be at your side!</i>
            return 10
        elif self.index == 4:
            # $script:0625110307010359$
            # - <font color='#909090'>(This could be trouble for the empress...)</font>
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
