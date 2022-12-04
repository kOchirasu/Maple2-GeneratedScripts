""" 11000008: Green Hood """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 1

    def __1(self, pick: int) -> int:
        # $script:0831180407000032$
        # - What's wrong?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407000037$
        # - Welcome to $map:02000076$. How may I help you?
        if pick == 0:
            # $script:0831180407000038$
            # - Sell me on this $map:02000076$ business.
            return 51
        elif pick == 1:
            # $script:0831180407000039$
            # - What happened to the empress's celebration?
            return 52
        elif pick == 2:
            # $script:0831180407000040$
            # - Hey there. I'm new in town.
            return 53
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000042$
            # - $map:02000076$ used to be the home of archers and craftsmen, all living in a collective. They produced many great works and great hunters, generation after generation.
            return 51
        elif self.index == 1:
            # $script:0831180407000043$
            # - The Green Hoods formed to protect the village from outside threats to their peace. Their current leader is their fifth, $npcName:11000015[gender:1]$.
            return 51
        elif self.index == 2:
            # $script:0831180407000044$
            # - Is $npcName:11000015[gender:1]$ the chief of this village? Ha ha, no. Henesys's chief is $npcName:11000001[gender:0]$. $npcName:11000015[gender:1]$'s father and $npcName:11000001[gender:0]$ have been best friends since they were young.
            return 51
        elif self.index == 3:
            # $script:0831180407000045$
            # - That's why $npcName:11000001[gender:0]$ takes care of $npcName:11000015[gender:1]$ like his own. You know, $npcName:11000015[gender:1]$ doesn't like people talking about her. So, maybe don't tell her about this conversation?
            return -1
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000046$
            # - I've heard a great earthquake occurred near $map:02000001$, and the empress's court was canceled as a result. I hope the damage isn't too serious. That disaster might also keep $npcName:11000045[gender:0]$ from returning anytime soon.
            return 52
        elif self.index == 1:
            # $script:0831180407000047$
            # - $npcName:11000045[gender:0]$ won't tolerate anyone trying to take advantage of a chaotic situation. I hope he'll be back soon. We need him more than ever. 
            return -1
        return -1

    def __53(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000048$
            # - You've probably noticed that the Green Hoods are all archers. We're renowned throughout Victoria Island for our marksmanship, and even $npcName:11000045[gender:0]$, the master archer of $map:02000001$, is a Green Hood.
            return 53
        elif self.index == 1:
            # $script:0831180407000049$
            # - In fact, she taught me everything I know about loosing a bow. If you're interested in archery yourself, I'd suggest paying her a visit next time you're in the capital.
            return -1
        return -1

    def __54(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000050$
            # - Everyone in Maple World dreams of having a house of their own. $npcName:11000001[gender:0]$ is doing what he can to manage the housing lots around the village, but there's only so much land.
            return 54
        elif self.index == 1:
            # $script:0831180407000051$
            # - If you don't have a house yet, you could settle down in $map:02000076$. $map:02000105$ is also quite nice, and is famous for its beautiful maple trees. There might be some empty lots still available in $map:02000104$ or $map:02000143$ as well. If you're looking for more affordable options, then you can check out the apartments in $map:02000105$ or $map:02000104$.
            return 54
        elif self.index == 2:
            # $script:0831180407000052$
            # - There are many advantages to owning a house, you know. These days, every home comes with a device that will let you teleport there at anytime from almost anywhere. Let me tell you, it's saved my butt plenty of times after a long day of patrolling the ant tunnels.
            return 54
        elif self.index == 3:
            # $script:0831180407000053$
            # - And the merchants in $map:02000036$, west of $map:02000023$, have all kinds of interesting furnishings for sale. Decorate your floors, walls, furniture, and yard to create a house that's unique to you. Some merchants will even sell buildings you can place on your lot! When you're ready to buy, go to $map:02000036$ to shop for your house.
            return 54
        elif self.index == 4:
            # $script:0831180407000054$
            # - If you already have a house, hiring a maid is a good next step. $npcName:11000700[gender:1]$ in $map:02000001$ is an expert on assistants and can definitely help you out. Maybe you should look for a house around $map:02000076$ first.
            return -1
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
        return Option.NONE
