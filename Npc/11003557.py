""" 11003557: Dr. Galileo's Hologram """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __30(self, pick: int) -> int:
        # $script:0907171907008984$
        # - The simulation is stable. Brainwaves look good. All right, let's get the ball rolling on this test!
        if pick == 0:
            # $script:0907171907008985$
            # - What are you doing here?
            return 31
        elif pick == 1:
            # $script:0907171907008986$
            # - Got any advice for completing this test?
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0907171907008987$
            # - I must admit I have a particular interest in this simulation. You see... An anonymous author from bygone days once wrote about the majesty of the $npcName:99990021$ which occurs so rarely in nature. However, the process if artificially mixing slimes to create them was legally prohibited some time ago.
            return 31
        elif self.index == 1:
            # $script:0907171907008989$
            # - Doesn't that just make your mind race? Why? What was so dangerous or terrible about trying to artificially create a $npcName:99990021$? That fabled splendor... I'd love to see it with my own two eyes.
            if pick == 0:
                # $script:0907171907008990$
                # - Sooo... What should I be doing?
                return 32
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0907171907008991$
        # - Come now, you know I'm not supposed to interfere with the test.
        if pick == 0:
            # $script:0907171907008992$
            # - Am I supposed to make a $npcName:99990021$?
            return 33
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0907171907008993$
            # - Err...!<font color="#909090"> <font size="20">Should I tell them? I can't interfere with the test... Of course they're bound to try mixing them sooner or later...</font>
            return 33
        elif self.index == 1:
            # $script:0907171907008994$
            # - ...Ahem. I suppose it would be all right if I simply explain how the machinery works.
            return 33
        elif self.index == 2:
            # $script:0907171907008995$
            # - The <font color="#ffd200">color meter</font> represents how many of each color of slime have been added to the machine. If the meter for any color reaches the red, that means you've exceeded the appropriate amount of slime.
            return 33
        elif self.index == 3:
            # $script:0907171907008996$
            # - As the mass production of artificial slimes has been outlawed for some time, the blueprints for the related machinery is quite dated and they are likely a bit imprecise. This means that being a single unit over or short of the meter's limit should not impact your success.
            return 33
        elif self.index == 4:
            # $script:0907171907008997$
            # - To achieve the perfect slime ratio, you'll need to get the five color meters as close to 100% as possible.
            return 33
        elif self.index == 5:
            # $script:0907171907008998$
            # - Ah, but there's one important thing to be aware of. The slimes come in three different sizes. <b>The larger the slime you squash, the faster the gauge fills up!</b> Good luck achieving the perfect color ratio!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.NEXT
        elif (self.state, self.index) == (33, 1):
            return Option.NEXT
        elif (self.state, self.index) == (33, 2):
            return Option.NEXT
        elif (self.state, self.index) == (33, 3):
            return Option.NEXT
        elif (self.state, self.index) == (33, 4):
            return Option.NEXT
        elif (self.state, self.index) == (33, 5):
            return Option.CLOSE
        return Option.NONE
