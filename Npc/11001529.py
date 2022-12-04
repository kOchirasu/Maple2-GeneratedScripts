""" 11001529: 50 Meso """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 40

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0318211907005909$
        # - Whoo! This place is bumpin'!
        return None # TODO

    def __40(self, pick: int) -> int:
        # $script:0318211907005913$
        # - Whoa there! Ask me questions if you got 'em!
        if pick == 0:
            # $script:0318211907005914$
            # - How do you play Dance, Dance, Stop?
            return 41
        elif pick == 1:
            # $script:0318211907005915$
            # - I got eliminated. It's not fair!
            return 47
        elif pick == 2:
            # $script:0318211907005916$
            # - What are you doing here?
            return 48
        return -1

    def __41(self, pick: int) -> int:
        # $script:0318211907005917$
        # - When the numbers appear on the floor panels, hop on them! If you match the number of dancers to the number, you go on to the next round. Otherwise... you're out!
        if pick == 0:
            # $script:0318211907005918$
            # - How do you win? 
            return 42
        elif pick == 1:
            # $script:0318211907005919$
            # - I don't know how to dance.
            return 46
        return -1

    def __42(self, pick: int) -> int:
        # $script:0318211907005920$
        # - Last 5 rounds, and you win. But the longer the game goes on, the less time you have to get on a panel. If you're a quick thinker and a fast runner, you can win... even if you're a terrible dancer!
        if pick == 0:
            # $script:0318211907005921$
            # - Do you have any tips?
            return 43
        elif pick == 1:
            # $script:0318211907005922$
            # - I'll win next time!
            return 45
        return -1

    def __43(self, pick: int) -> int:
        if self.index == 0:
            # $script:0318211907005923$
            # - You know I do! Dancing isn't just fun—it's a great way to get experience. Once you're on a tile for 2 or more dancers, you can block others from joining you. This is a great way to lock down a tricky number and get a fabulous bonus.
            return 43
        elif self.index == 1:
            # $script:0318211907005924$
            # - Just press the action key to block others from joining your panel. You can't leave the tile while you're doing this, so when you're done be sure to press the action key again. But the most important tip I have... is to <i>have fun!</i>
            if pick == 0:
                # $script:0318211907005925$
                # - I'll win next time!
                return 45
            return -1
        return -1

    def __45(self, pick: int) -> int:
        # $script:0318211907005926$
        # - That's the spirit! Keep it real, my friend. Keep it real.
        return -1

    def __46(self, pick: int) -> int:
        # $script:0318211907005927$
        # - Don't even sweat it. Just press the yellow light on the floor, and <i>bam!</i> It's dance time! Press the action key to boogie down with some random dance moves.
        if pick == 0:
            # $script:0318211907005928$
            # - How do you win? 
            return 42
        elif pick == 1:
            # $script:0318211907005929$
            # - I'll win next time!
            return 45
        return -1

    def __47(self, pick: int) -> int:
        # $script:0318211907005930$
        # - Don't let it get to you, my downtrodden dancer. Even if you're eliminated, there's a special dance floor where you can strut yourself. Just go to the yellow stage and press the action key!
        if pick == 0:
            # $script:0318211907005931$
            # - What's the secret to winning the game?
            return 42
        elif pick == 1:
            # $script:0318211907005932$
            # - I'll win next time!
            return 45
        return -1

    def __48(self, pick: int) -> int:
        # $script:0318211907005933$
        # - Mushroom art isn't the only thing I love, yo. Listening to great jams and partying with my people are high on the list.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (43, 0):
            return Option.NEXT
        elif (self.state, self.index) == (43, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (45, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (46, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (47, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (48, 0):
            return Option.CLOSE
        return Option.NONE
