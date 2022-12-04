""" 11003552: Yoharang """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0905163707008895$
        # - I miss $map:63000044$... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0905163707008898$
        # - I wonder how the weather on $map:63000044$ is today...
        if pick == 0:
            # $script:0905163707008899$
            # - Tell me about $map:63000044$.
            return 31
        elif pick == 1:
            # $script:0905163707008900$
            # - I want to see $map:63000044$ at its most pristine.
            return 32
        elif pick == 2:
            # $script:0905163707008901$
            # - Show me $map:52000058$ when it's poisoned.
            return 33
        elif pick == 3:
            # $script:0905163707008902$
            # - Bring me to $map:52000059$ during an eruption! 
            return 34
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0905163707008903$
            # - If you've ever been to $map:63000044$, then you know that it was once a peaceful haven. The water was clean and clear, the fish flourished... My beloved hometown...
            return 31
        elif self.index == 1:
            # $script:0905163707008904$
            # - I'm not sure why, but the water's become muddy and poisonous, and weird fish have started showing up. There was nothing we could do...  
            return 31
        elif self.index == 2:
            # $script:0905163707008905$
            # - Then, a little later, $map:63000044$ erupted into a giant volcano! Some folks thought it was a mermaid's curse, and others claimed that it was a government plot. Personally, I think the volcano was always there, sleeping... Waiting...
            return 31
        elif self.index == 3:
            # $script:0905163707008906$
            # - Anyway, I can send you to any version of $map:63000044$ that you like. Whether you seek the pristine lake or a sea of molten lava... How can I do that? It's simple.
            return 31
        elif self.index == 4:
            # $script:0905163707008907$
            # - But it's nearly time for my nap, so I won't go into the details now. Besides, what's the point of life without a bit of mystery? 
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # functionID=1 
        # $script:0905163707008908$
        # - When it was clean and peaceful, huh? Well, guess what? I can send you back there if you want! 
        return -1

    def __33(self, pick: int) -> int:
        # functionID=2 
        # $script:0905163707008909$
        # - When it was mysteriously contaminated, huh? Well, guess what? I can send you back there if you want! 
        return -1

    def __34(self, pick: int) -> int:
        # functionID=3 
        # $script:0905163707008910$
        # - When it was covered in hot lava, huh? Well, guess what? I can send you back there if you want! 
        return -1

    def __40(self, pick: int) -> int:
        # $script:0905163707008911$
        # - Have you ever been to $map:63000044$? It's quiet and empty... the perfect fishing spot!
        if pick == 0:
            # $script:0905163707008912$
            # - How do I get there?
            return 41
        return -1

    def __41(self, pick: int) -> int:
        # $script:0905163707008913$
        # - You can go there after you finish the fishing quest in the Maple Guide. Every fisher should visit that place at least once in their life.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.NEXT
        elif (self.state, self.index) == (31, 3):
            return Option.NEXT
        elif (self.state, self.index) == (31, 4):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (33, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
