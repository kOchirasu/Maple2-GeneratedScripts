""" 11004485: Gracilis """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 30])

    def select(self) -> int:
        return random.choice([0, 20])

    def __0(self, pick: int) -> int:
        # $script:1227192907012266$
        # - Those clothes... You're from Maple World, like me! You must be the first friendly face I've seen in days.
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0104144307012585$
        # - Hm...
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:1227192907012267$
        # - Those clothes... You're from Maple World, like me! You must be the first friendly face I've seen in days.
        if pick == 0:
            # $script:1227192907012268$
            # - How's the research going?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:1227192907012269$
            # - It's going... slowly. I can't stop thinking about this machine here...
            return 11
        elif self.index == 1:
            # $script:1227192907012270$
            # - In design, it resembles the noblest of tools, the humble drill. You can see why I've become obsessed with it.
            return 11
        elif self.index == 2:
            # $script:1227192907012271$
            # - But this is no ordinary drill, if it even is a drill at all. It seems like it can absorb energy of a certain wavelength. The same wavelength that aetherine resonates at, in fact.
            return 11
        elif self.index == 3:
            # $script:1227192907012272$
            # - Perhaps it is used to mine for aetherine, then transmit the energy somehow? That's my hypothesis, at any rate.
            if pick == 0:
                # $script:0114163707012712$
                # - Amazing!
                return 70
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0104144307012586$
        # - Yes, yes. I'm sure I've seen your face somewhere before. I'm really much too busy just now, though, so...
        if pick == 0:
            # $script:0104144307012587$
            # - What are you up to?
            return 40
        return -1

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104144307012588$
            # - An amateur academic. Of course. I suppose I can spare a minute of my time to explain.
            return 40
        elif self.index == 1:
            # $script:0104144307012589$
            # - I am one of the premier mechanical engineers of Victoria Island! I snuck aboard—I mean, I legitimately boarded Sky Fortress in order to study the machines of Kritias.
            return 40
        elif self.index == 2:
            # $script:0104144307012590$
            # - And look! I have discovered the most wonderful drills!
            return 40
        elif self.index == 3:
            # $script:0104144307012591$
            # - At least, it looks like a drill. Technically speaking, that's not quite right.
            return 40
        elif self.index == 4:
            # $script:0104144307012592$
            # - The structure of this drill defies all known convention—it's no twist drill, nor straight shank drill, nor step drill, and so forth.
            return 40
        elif self.index == 5:
            # $script:0104144307012593$
            # - And this material! They've somehow found something better than cemented carbide. I can't even— I mean, it's just not—
            return 40
        elif self.index == 6:
            # $script:0104144307012594$
            # - GASP! Sorry... I got so excited, I forgot to breathe.
            return 40
        elif self.index == 7:
            # $script:0104144307012595$
            # - Anyway, it's all clear now, is it not?
            if pick == 0:
                # $script:0104144307012596$
                # - Not in the slightest.
                return 50
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0104144307012597$
        # - You jest. I explained it clearly enough for a five-year-old to understand.
        if pick == 0:
            # $script:0104144307012598$
            # - Then I must be four.
            return 60
        return -1

    def __60(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104144307012599$
            # - ...
            return 60
        elif self.index == 1:
            # $script:0104144307012600$
            # - You tire me. Shoo.
            return 60
        elif self.index == 2:
            # $script:0104144307012601$
            # - But what is this drill for...?
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:0114163707012714$
        # - There's no shortage of amazing things in Kritias. That's why I'm so busy with research!
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.NEXT
        elif (self.state, self.index) == (11, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.NEXT
        elif (self.state, self.index) == (40, 2):
            return Option.NEXT
        elif (self.state, self.index) == (40, 3):
            return Option.NEXT
        elif (self.state, self.index) == (40, 4):
            return Option.NEXT
        elif (self.state, self.index) == (40, 5):
            return Option.NEXT
        elif (self.state, self.index) == (40, 6):
            return Option.NEXT
        elif (self.state, self.index) == (40, 7):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.NEXT
        elif (self.state, self.index) == (60, 1):
            return Option.NEXT
        elif (self.state, self.index) == (60, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        return Option.NONE
