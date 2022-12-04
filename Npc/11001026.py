""" 11001026: Raymon """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407003483$
        # - Sigh... 
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0831180407003486$
        # - Everything that happened to us is my fault. I shouldn't have dragged $npcName:11000492[gender:0]$ into it... I was blinded by greed and... he died because of me. 
        if pick == 0:
            # $script:0831180407003487$
            # - How did $npcName:11000492[gender:0]$ die?
            return 31
        elif pick == 1:
            # $script:0831180407003488$
            # - What kind of deal did you make with $npcName:11000044[gender:0]$?
            return 32
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003489$
            # - Well... It's all because of that blasted caravan attack. Just before $npcName:11000492[gender:0]$ became a suspect, he wanted to go over our alibis. I went to our meeting spot in the $map:02000043$ to meet him.
            return 31
        elif self.index == 1:
            # $script:0831180407003490$
            # - $npcName:11000044[gender:0]$'s assassins were waiting for us when I got there. They thought $npcName:11000492[gender:0]$ and I were loose ends, so they were going to get rid of us.
            return 31
        elif self.index == 2:
            # $script:0831180407003491$
            # - I escaped, but it was too late for $npcName:11000492[gender:0]$. I never imagined things would go so wrong.
            return -1
        return -1

    def __32(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003492$
            # - It wasn't a deal so much as extortion. I've been stealing money from Barrota for years. Basic stuff–a redirected delivery here, an extra fee there.
            return 32
        elif self.index == 1:
            # $script:0831180407003493$
            # - $npcName:11000044[gender:0]$ found out somehow. If I didn't work with him, he'd have exposed me to the public.
            if pick == 0:
                # $script:0831180407003494$
                # - And what did he want?
                return 33
            return -1
        return -1

    def __33(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407003495$
            # - He wanted the supplies for the big court gathering in $map:02000001$. I offered to pay him off, but he said he wasn't interested in money. That's when I realized he was up to something truly dangerous... but it didn't make a difference to me.
            return 33
        elif self.index == 1:
            # $script:0831180407003496$
            # - Of course, stealing imperial supplies is a tall order. I needed a man on the inside, and I got it in $npcName:11000492[gender:0]$. He had a reputation for being a straight shooter, but everyone has a price.
            return 33
        elif self.index == 2:
            # $script:0831180407003497$
            # - $npcName:11000492[gender:0]$'s mother is sick. I told him I could get her the best medicine money can buy. Better, even. That did the trick.
            return 33
        elif self.index == 3:
            # $script:0831180407003498$
            # - I promised $npcName:11000492[gender:0]$ that nobody would get hurt. It was a lie, of course, but desperate men will believe anything to ease their consciences. It wasn't hard to get the caravan route and schedule out of him.
            return 33
        elif self.index == 4:
            # $script:0831180407003499$
            # - I delivered the plans to $npcName:11000044[gender:0]$ personally. Met him at $map:02000117$. Him and the lady in the red cloak... I knew then that I'd never be able to live with myself after what I'd done.
            return 33
        elif self.index == 5:
            # $script:0831180407003500$
            # - But it was all over... or so I thought. The court was canceled, an earthquake tore up the royal road... All I knew was that I wanted out.
            if pick == 0:
                # $script:0831180407003501$
                # - And how did that go?
                return 34
            return -1
        return -1

    def __34(self, pick: int) -> int:
        # $script:0831180407003502$
        # - You know darn well how that went. Now $npcName:11000492[gender:0]$ is gone and my life is ruined...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (32, 0):
            return Option.NEXT
        elif (self.state, self.index) == (32, 1):
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.CLOSE
        return Option.NONE
