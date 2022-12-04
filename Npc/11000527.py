""" 11000527: Hermit """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([30, 40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407002251$
        # - Welcome. It's nice to meet you.
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002254$
            # - $MyPCName$, I can't believe we're meeting again like this. I can see in your eyes how much you've grown since last we met. Do you remember what I told you then? That the world would need a hero? 
            return 30
        elif self.index == 1:
            # $script:0831180407002255$
            # - Looking at you now, I believe that you're the one.
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180407002256$
        # - Ha ha ha, you look like you have many questions for me. What do you want to know?
        if pick == 0:
            # $script:0831180407002257$
            # - How did you end up on Victoria Island?
            return 41
        elif pick == 1:
            # $script:0831180407002258$
            # - Why did you save $npcName:11000064[gender:0]$?
            return 43
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002259$
            # - This $map:02000051$ is where I was born and raised. The last time I left, I swore I'd never return... I thought that was best for everyone here. 
            return 41
        elif self.index == 1:
            # $script:0831180407002260$
            # - But something happened, and it made me wonder if I made the right decision. I came back to finish what I couldn't finish then.
            if pick == 0:
                # $script:0831180407002261$
                # - What is it?
                return 42
            return -1
        return -1

    def __42(self, pick: int) -> int:
        # $script:0831180407002262$
        # - That's... I'll tell you when I'm ready.
        return -1

    def __43(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407002263$
            # - I couldn't ignore the wish of a dying man. Even if he was a prisoner... 
            return 43
        elif self.index == 1:
            # $script:0831180407002264$
            # - And when he awoke after his brush with death, I could see in his eyes that he was innocent. I didn't ask any questions, but I knew I had to help him.
            return 43
        elif self.index == 2:
            # $script:0831180407002265$
            # - Stay true to yourself, and you can overcome anything. No matter how difficult it is, you can do it.
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0809153207007164$
        # - Every age needs a hero.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (43, 0):
            return Option.NEXT
        elif (self.state, self.index) == (43, 1):
            return Option.NEXT
        elif (self.state, self.index) == (43, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.CLOSE
        return Option.NONE
