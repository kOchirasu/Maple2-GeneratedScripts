""" 11000510: Peachy """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1123232210001189$
        # - I better take a break from the forge and do some finishing. Did you see my jig or wire brush around?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1123232210001193$
        # - Just a quick rap on the anvil to break off the fire scale, and this sword is done... Oh, hello. Have you come to enchant your gear?
        if pick == 0:
            # $script:1123232210001194$
            # - Can you enchant my items?
            return 31
        elif pick == 1:
            # $script:0323154410001466$
            # - How about we change some bonus attributes?
            return 30
        elif pick == 2:
            # $script:0323154410001467$
            # - Tell me about your work.
            return 29
        return -1

    def __29(self, pick: int) -> int:
        if self.index == 0:
            # $script:1123232210001196$
            # - Hehe. I'm a blacksmith.
            return 29
        elif self.index == 1:
            # $script:1123232210001197$
            # - I love the work that I do. There's nothing more satisfying than using my wrench to tinker with gear or banging metal into shape in front of a hot forge.
            return 29
        elif self.index == 2:
            # $script:1123232210001198$
            # - If you need to strengthen your equipment, come to me! You'll have to gather the materials: $itemPlural:40100001$, $itemPlural:40100023$, and $itemPlural:40100024$.
            return 29
        elif self.index == 3:
            # $script:1123232210001199$
            # - You can get $itemPlural:40100023$ by dismantling level 20 or higher gear. Just use the Dismantle button in your inventory window. As for $itemPlural:40100024$, they'll only come from dismantling gear that's epic or better.
            return 29
        elif self.index == 4:
            # $script:1123232210001200$
            # - People also compete for $itemPlural:40100023$ at the Maple Arena, if that's something you're interested in.
            return 29
        elif self.index == 5:
            # $script:1123232210001201$
            # - I used to enchant low level gear for people, but we all soon realized it's just not worth it. So now, I only enchant items marked as "Can be Enchanted."
            return 29
        elif self.index == 6:
            # $script:0323154410001468$
            # - Oh! One more thing! I'm sure you know that some high-grade gear grant random special abilities. If you're interested in modifying those abilities, I can help!
            return 29
        elif self.index == 7:
            # $script:0323154410001469$
            # - This is a brand new service blacksmiths can provide, thanks to a breakthrough at the $map:02000270$ research center. Hehe. They've refined meteoric ores into $itemPlural:40100026$ that can change the chemical properties in gear!
            return 29
        elif self.index == 8:
            # $script:0323154410001470$
            # - Of course, bonus attributes are hard to rely on since the results are so random. And in addition to $itemPlural:40100026$, you'll also need $itemPlural:40100001$, $itemPlural:40100002$, $itemPlural:40100003$, or $itemPlural:40100021$, depending on the work being done.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # functionID=1 
        # $script:0323154410001471$
        # - Oh! Of course! Just pick an item for me to work on. Remember, I only handle epic and legendary armor and accessories level 50 and above.
        return -1

    def __31(self, pick: int) -> int:
        # functionID=1 
        # $script:1123232210001202$
        # - Oh! Sure thing! Select an item for me to enchant. It's got to have the "Can be Enchanted" mark on it, you hear?
        return -1

    def __999(self, pick: int) -> int:
        # $script:1123232210001278$
        # - I'm so sorry! I'm swamped! Never been so busy in my life. I'm working on a special order, you see.
        if pick == 0:
            # $script:1123232210001279$
            # - Can you enchant my items?
            return 41
        elif pick == 1:
            # $script:1123232210001280$
            # - What do you do?
            return 39
        return -1

    def __39(self, pick: int) -> int:
        if self.index == 0:
            # $script:1123232210001281$
            # - Hehe. I'm a blacksmith.
            return 39
        elif self.index == 1:
            # $script:1123232210001282$
            # - I love the work that I do. There's nothing more satisfying than using my wrench to tinker with gear or banging metal into shape in front of a hot forge.
            return 39
        elif self.index == 2:
            # $script:1123232210001283$
            # - If you need to strengthen your equipment, come to me! You'll have to gather the materials: $itemPlural:40100001$, $itemPlural:40100023$, and $itemPlural:40100024$.
            return 39
        elif self.index == 3:
            # $script:1123232210001284$
            # - You can get $itemPlural:40100023$ by dismantling level 20 or higher gear. Just use the Dismantle button in your inventory window. As for $itemPlural:40100024$, they'll only come from dismantling gear that's epic or better.
            return 39
        elif self.index == 4:
            # $script:1123232210001285$
            # - People also compete for $itemPlural:40100023$ at the Maple Arena, if that's something you're interested in.
            return 39
        elif self.index == 5:
            # $script:1123232210001286$
            # - Some customers desire for me to enchant low level gear, but it's simply not worth the time. I only enchant items marked as "Can be Enchanted."
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:1123232210001287$
        # - I'd love to help you, but for now I have to focus on this special order I've got. I'll take especially good care of you if you come back later, I promise.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (29, 0):
            return Option.NEXT
        elif (self.state, self.index) == (29, 1):
            return Option.NEXT
        elif (self.state, self.index) == (29, 2):
            return Option.NEXT
        elif (self.state, self.index) == (29, 3):
            return Option.NEXT
        elif (self.state, self.index) == (29, 4):
            return Option.NEXT
        elif (self.state, self.index) == (29, 5):
            return Option.NEXT
        elif (self.state, self.index) == (29, 6):
            return Option.NEXT
        elif (self.state, self.index) == (29, 7):
            return Option.NEXT
        elif (self.state, self.index) == (29, 8):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (999, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (39, 0):
            return Option.NEXT
        elif (self.state, self.index) == (39, 1):
            return Option.NEXT
        elif (self.state, self.index) == (39, 2):
            return Option.NEXT
        elif (self.state, self.index) == (39, 3):
            return Option.NEXT
        elif (self.state, self.index) == (39, 4):
            return Option.NEXT
        elif (self.state, self.index) == (39, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
