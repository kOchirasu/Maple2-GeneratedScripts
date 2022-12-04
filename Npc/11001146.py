""" 11001146: Recipe Note """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([10, 20, 21, 23])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0916043407003980$
        # - Read $npcName:11001146$.
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0916043407003981$
            # - <u><font color="#FA5656">$item:30000395$ Recipe</font></u>
            #   <b>1.</b> Squeeze <font color="#ffd200">$item:30000390$</font> from <font color="#ffd200">$npcNamePlural:21000031$</font>
            #   <b>2.</b> Harvest <font color="#ffd200">$item:30000392$</font> from <font color="#ffd200">$npcNamePlural:21000009$</font>
            return 10
        elif self.index == 1:
            # $script:0916043407003982$
            # - <b>3.</b> Acquire <font color="#ffd200">$itemPlural:30000391$</font> from the <font color="#ffd200">Hot Cocoa Springs</font>
            #   <b>4.</b> Pick <font color="#ffd200">$itemPlural:30000393$</font> from the <font color="#ffd200">red trees</font>
            #   <font size="20" color="#FC0404">      *Note: Use only locally sourced ingredients!</font>
            return -1
        return -1

    def __20(self, pick: int) -> int:
        if self.index == 0:
            # $script:0916043407003983$
            # - <u><font color="#FA5656">$item:30000395$ Recipe</font></u>
            #   <b>1.</b> Squeeze <font color="#ffd200">$item:30000390$</font> from <font color="#ffd200">$npcNamePlural:21000031$</font>
            #   <b>2.</b> Harvest <font color="#ffd200">$item:30000392$</font> from <font color="#ffd200">$npcNamePlural:21000009$</font>
            return 20
        elif self.index == 1:
            # $script:0916043407003984$
            # - <b>3.</b> Acquire <font color="#ffd200">$itemPlural:30000391$</font> from the <font color="#ffd200">Hot Cocoa Springs</font>
            #   <b>4.</b> Pick <font color="#ffd200">$itemPlural:30000393$</font> from the <font color="#ffd200">red trees</font>
            #   <font size="20" color="#FC0404">      *Note: Use only locally sourced ingredients!</font>
            if pick == 0:
                # $script:0916043407003985$
                # - (Read it again.)
                return 21
            elif pick == 1:
                # $script:0916043407003986$
                # - (Read the back side.)
                return 22
            return -1
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0916043407003987$
            # - <u><font color="#FA5656">$item:30000395$ Recipe</font></u>
            #   <b>1.</b> Squeeze <font color="#ffd200">$item:30000390$</font> from <font color="#ffd200">$npcNamePlural:21000031$</font>
            #   <b>2.</b> Harvest <font color="#ffd200">$item:30000392$</font> from <font color="#ffd200">$npcNamePlural:21000009$</font>
            return 21
        elif self.index == 1:
            # $script:0916043407003988$
            # - <b>3.</b> Acquire <font color="#ffd200">$itemPlural:30000391$</font> from the <font color="#ffd200">Hot Cocoa Springs</font>
            #   <b>4.</b> Pick <font color="#ffd200">$itemPlural:30000393$</font> from the <font color="#ffd200">red trees</font>
            #   <font size="20" color="#FC0404">      *Note: Use only locally sourced ingredients!</font>
            if pick == 0:
                # $script:0916060407004042$
                # - (Read it again.)
                return 23
            elif pick == 1:
                # $script:0916060407004043$
                # - (Read the back side.)
                return 22
            return -1
        return -1

    def __22(self, pick: int) -> int:
        if self.index == 0:
            # $script:0916043407003989$
            # - <u><font color="#FA5656">Cooking the $item:30000395$</font></u>
            #   <b>1.</b> While stirring, gradually add the following ingredients to the <i>$npcName:11001147$</i>:
            #   <font color="#ffd200">8 $itemPlural:30000390$</font>, <font color="#ffd200">10 $itemPlural:30000392$</font>, <font color="#ffd200"> 7 $itemPlural:30000391$</font>, and <font color="#ffd200">9 $itemPlural:30000393$</font>
            return 22
        elif self.index == 1:
            # $script:0916043407003990$
            # - <b>2.</b> Cook over low heat for 5 minutes, stirring until uniform in consistency.
            #   <b>3.</b> Pour and let harden
            #   <font size="20" color="#FC0404">      *Note: $npcName:11001147$ is finicky. Remove cooked candy immediately.</font>
            return -1
        return -1

    def __23(self, pick: int) -> int:
        if self.index == 0:
            # $script:0916060407004044$
            # - <u><font color="#FA5656">$item:30000395$ Recipe</font></u>
            #   <b>1.</b> Squeeze <font color="#ffd200">$item:30000390$</font> from <font color="#ffd200">$npcNamePlural:21000031$</font>
            #   <b>2.</b> Harvest <font color="#ffd200">$item:30000392$</font> from <font color="#ffd200">$npcNamePlural:21000009$</font>
            return 23
        elif self.index == 1:
            # $script:0916060407004045$
            # - <b>3.</b> Acquire <font color="#ffd200">$itemPlural:30000391$</font> from the <font color="#ffd200">Hot Cocoa Springs</font>
            #   <b>4.</b> Pick <font color="#ffd200">$itemPlural:30000393$</font> from the <font color="#ffd200">red trees</font>
            #   <font size="20" color="#FC0404">      *Note: Use only locally sourced ingredients!</font>
            if pick == 0:
                # $script:0916060407004046$
                # - (Read it again.)
                return 21
            elif pick == 1:
                # $script:0916060407004047$
                # - (Read the back side.)
                return 22
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.NEXT
        elif (self.state, self.index) == (20, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.NEXT
        elif (self.state, self.index) == (21, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.NEXT
        elif (self.state, self.index) == (22, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.NEXT
        elif (self.state, self.index) == (23, 1):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
