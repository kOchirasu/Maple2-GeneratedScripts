""" 11000144: Tristan """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([20, 50, 60])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000587$
        # - What brings you here?
        return None # TODO

    def __20(self, pick: int) -> int:
        # $script:0831180407000589$
        # - How did you make it this far?
        if pick == 0:
            # $script:0831180407000590$
            # - I walked.
            return 21
        elif pick == 1:
            # $script:0831180407000591$
            # - I ran.
            return 21
        elif pick == 2:
            # $script:0831180407000592$
            # - I flew.
            return 21
        elif pick == 3:
            # $script:0831180407000593$
            # - It just happened.
            return 22
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000594$
            # - You know that's not the answer I wanted. You think this is all a big joke, don't you? Well, let me give you some advice.
            return 21
        elif self.index == 1:
            # $script:0831180407000595$
            # - Go back to where you came from. You're too young to die like a rat out here.
            return -1
        return -1

    def __22(self, pick: int) -> int:
        # $script:0831180407000596$
        # - Then turn around and leave. It's too dangerous for you to hang around here.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180407000598$
        # - Mm? Are you here to find the $map:02000037$ where $npcName:23090005[gender:0]$ is sealed?
        if pick == 0:
            # $script:0831180407000599$
            # - Yep!
            return 51
        elif pick == 1:
            # $script:0831180407000600$
            # - Nope!
            return 53
        return -1

    def __51(self, pick: int) -> int:
        # $script:0831180407000601$
        # - What is your purpose? Is there someone that you want to protect? Or do you covet $npcName:23090005[gender:0]$'s treasure?
        if pick == 0:
            # $script:0831180407000602$
            # - I'm here to protect all of Maple World.
            return 52
        elif pick == 1:
            # $script:0831180407000603$
            # - I want treasure!
            return 54
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000604$
            # - The whole world, eh? What a ridiculous goal...
            return 52
        elif self.index == 1:
            # $script:0831180407000605$
            # - But goals like that keep a $male:man,female:woman$ going against impossible odds. I can respect that. Don't you dare fail!
            return 52
        elif self.index == 2:
            # $script:0831180407000606$
            # - I'm jealous, actually. Jealous that you can still have a bold dream like that. I've seen too many battles to even comprehend a dream like that...
            return 52
        elif self.index == 3:
            # $script:0831180407000607$
            # - Ah, to be young and foolish again.
            return -1
        return -1

    def __53(self, pick: int) -> int:
        # $script:0831180407000610$
        # - Not that it's my place to judge, mind. Your life is yours to throw away as you please.
        return -1

    def __54(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000608$
            # - Another treasure seeker, then...
            return 54
        elif self.index == 1:
            # $script:0831180407000609$
            # - The treasure is great, to be certain. But is it worth risking your life over?
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:1026170307004301$
        # - If $item:30000419$ is what you're after, you should talk to $npcName:11001210[gender:0]$ in $map:02000023$. I'm sure he can help you.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.NEXT
        elif (self.state, self.index) == (21, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.NEXT
        elif (self.state, self.index) == (52, 2):
            return Option.NEXT
        elif (self.state, self.index) == (52, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (53, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (54, 0):
            return Option.NEXT
        elif (self.state, self.index) == (54, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (60, 0):
            return Option.CLOSE
        return Option.NONE
