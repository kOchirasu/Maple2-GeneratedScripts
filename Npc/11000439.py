""" 11000439: Dark Wind Watchman """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([50, 60])

    def select(self) -> int:
        return 1

    def __1(self, pick: int) -> int:
        # $script:0831180407001832$
        # - What brings you here?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407001837$
        # - What brings you here?
        if pick == 0:
            # $script:0831180407001838$
            # - Tell me about Kerning City.
            return 51
        elif pick == 1:
            # $script:0831180407001839$
            # - What happened to the empress's celebration?
            return 52
        elif pick == 2:
            # $script:0831180407001840$
            # - Hey there. I'm new in town.
            return 53
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001842$
            # - $map:02000100$ used to be a village of inventors and engineers who worked out of bunkers. It was a center of research and discovery.
            return 51
        elif self.index == 1:
            # $script:0831180407001843$
            # - Their achievements gave rise to the modern, high-tech metropolis that is $map:02000100$. But where are those engineers and inventors now? That question keeps me up at night. 
            return 51
        elif self.index == 2:
            # $script:0831180407001844$
            # - Anyway, security in $map:02000100$ is handled by us Dark Wind scouts. Losing Winn Stilton was a big blow to the group, but we were able to reunite under the great leadership of our current captain, $npcName:11000044[gender:0]$.
            return 51
        elif self.index == 3:
            # $script:0831180407001845$
            # - The current mayor of $map:02000100$ is Mr. $npcName:11000065[gender:0]$. Word is that $npcName:11000252[gender:0]$, the wealthiest man in the city, has the mayor in his pocket. Of course, there are always going to be rumors like that floating around.
            return -1
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001846$
            # - I've heard the court was canceled because of the great earthquake that hit $map:02000001$. It might be a good thing, honestly. The poor people in $map:02000100$ have been upset about the widening gap between them and the rich. Not having the money to attend the court was like salting the wound.
            return 52
        elif self.index == 1:
            # $script:0831180407001847$
            # - But it also worries me. What if the people decide to rise in rebellion, now that the highly-anticipated court was canceled and their beloved $npcName:11000075[gender:1]$ is nowhere to be seen? As part of Dark Wind, I feel more responsible for this city now than ever.
            return -1
        return -1

    def __53(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001848$
            # - You ever visit $map:02000001$? Major players from the backstreets of $map:02000100$ have decided to meet there and recruit new members. Assassin Master $npcName:11000051[gender:1]$ should be there too. 
            return 53
        elif self.index == 1:
            # $script:0831180407001849$
            # - The timing is pretty lucky for you. If it weren't for the empress's court, they wouldn't be there. Of course, if you aren't at least level 10, they won't even talk to you.
            return -1
        return -1

    def __54(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407001850$
            # - Everyone in Maple World dreams of a house of their own. There are many houses in this city, and plenty of people who want them. If you don't have a house yet, how'd you like to settle down in $map:02000100$?
            return 54
        elif self.index == 1:
            # $script:0831180407001851$
            # - North of $map:02000100$ is $map:02000166$, the site of some booming new developments. Recently renovated, $map:02000165$ and $map:02000167$ are often mentioned as hot properties. There are also low-priced apartment complexes in $map:02000164$, west of $map:02000100$. 
            return 54
        elif self.index == 2:
            # $script:0831180407001852$
            # - There are many advantages to owning a house, you know. These days, every home comes with a device that will let you teleport there at anytime from almost anywhere. Let me tell you, it's saved my butt plenty of times after a long day of patrolling $map:02000146$.
            return 54
        elif self.index == 3:
            # $script:0831180407001853$
            # - And the merchants in $map:02000036$, west of $map:02000023$, have all kinds of interesting furnishings for sale. Decorate your floors, walls, furniture, and yard to create a house that's unique to you. Some merchants will even sell buildings you can place on your lot! When you're ready to buy, go to $map:02000036$ to shop for your house.
            return 54
        elif self.index == 4:
            # $script:0831180407001854$
            # - If you already have a house, hiring a maid is a good next step. $npcName:11000700[gender:1]$ in $map:02000001$ is an expert on assistants and can definitely help you out. Maybe you should look for a house around $map:02000100$ first.
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180407001855$
        # - Captain $npcName:11000044[gender:0]$... No, he's not my captain anymore. This is all too much. What's going to happen to Dark Wind now?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.NEXT
        elif (self.state, self.index) == (51, 2):
            return Option.NEXT
        elif (self.state, self.index) == (51, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (53, 0):
            return Option.NEXT
        elif (self.state, self.index) == (53, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (54, 0):
            return Option.NEXT
        elif (self.state, self.index) == (54, 1):
            return Option.NEXT
        elif (self.state, self.index) == (54, 2):
            return Option.NEXT
        elif (self.state, self.index) == (54, 3):
            return Option.NEXT
        elif (self.state, self.index) == (54, 4):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
