""" 11001430: Miel """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217205907005427$
        # - Many things shine, not all of them valuable.
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1222203907005509$
            # - It's so close, but I can't reach it. It comes to me in the night and vanishes at dawn.
            return 40
        elif self.index == 1:
            # $script:1222203907005510$
            # - The more I lean into the sunlight, the more I hide in the moonlight. But then, it all drifts apart. I can't continue this way... 
            if pick == 0:
                # $script:1222203907005511$
                # - What on earth are you talking about?
                return 41
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:1222203907005512$
        # - Huh...? Shoo! You wouldn't understand.
        return -1

    def __50(self, pick: int) -> int:
        # $script:0610174107006339$
        # - Hello.
        if pick == 0:
            # $script:0610174107006340$
            # - Did you miss your best friend?
            return 56
        elif pick == 1:
            # $script:0610174107006341$
            # - How are you doing?
            return 51
        return -1

    def __51(self, pick: int) -> int:
        # $script:0610174107006342$
        # - The desert is always the same—beautiful and desolate. $MyPCName$, how have you been?
        if pick == 0:
            # $script:0610174107006343$
            # - I came running all this way to see you.
            return 52
        elif pick == 1:
            # $script:0610174107006344$
            # - Things have been nice and quiet without you to bother me.
            return 55
        return -1

    def __52(self, pick: int) -> int:
        # $script:0610174107006345$
        # - Ha... I see. I thought I saw a bright light coming from afar... It lifted my spirits.
        if pick == 0:
            # $script:0610174107006346$
            # - Do you miss me?
            return 53
        return -1

    def __53(self, pick: int) -> int:
        # $script:0610174107006347$
        # - Are you feeling all right? When I mentioned a bright light from afar, I meant the moon. The moon! Not you.
        if pick == 0:
            # $script:0610174107006348$
            # - I'll be sure to visit more often.
            return 54
        return -1

    def __54(self, pick: int) -> int:
        # $script:0610174107006349$
        # - Sure, you do that. Who knows? Maybe next time I'll even be waiting for you.
        #   <font color="#909090">(In spite of his cool words, there's a warm smile on his lips.)</font> 
        return -1

    def __55(self, pick: int) -> int:
        # $script:0610174107006350$
        # - How nice for you. Leave in peace, then.
        #   <font color="#909090">(He sighs and looks away.)</font>
        return -1

    def __56(self, pick: int) -> int:
        # $script:0610174107006351$
        # - My friend? Who? 
        if pick == 0:
            # $script:0610174107006352$
            # - Have you forgotten our friendship?
            return 57
        elif pick == 1:
            # $script:0610174107006353$
            # - Are you feeling okay?
            return 58
        return -1

    def __57(self, pick: int) -> int:
        # $script:0610174107006354$
        # - Ah, of course I remember! You and I are friends now. It was just a little joke. 
        if pick == 0:
            # $script:0610174107006355$
            # - Keep these jokes up, and I'll stop visiting.
            return 59
        return -1

    def __58(self, pick: int) -> int:
        # $script:0610174107006356$
        # - I feel fine. Thank you for your concern, but... I was just playing a little joke on you. Maybe you're too naive for such play...
        if pick == 0:
            # $script:0610174107006357$
            # - Keep these jokes up, and I'll stop visiting.
            return 59
        return -1

    def __59(self, pick: int) -> int:
        # $script:0610174107006358$
        # - I thought this was what friends do! Now you're making <i>me</i> confused. If visiting me is such a bother, then you don't have to do it, you know. 
        if pick == 0:
            # $script:0610174107006359$
            # - I'll visit you again soon.
            return 54
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (53, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (54, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (55, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (56, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (57, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (58, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (59, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
