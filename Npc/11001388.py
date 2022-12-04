""" 11001388: Chiab """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([40, 50])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:1217193307005388$
        # - This village is good! You just got to look real close to see it.
        return None # TODO

    def __40(self, pick: int) -> int:
        if self.index == 0:
            # $script:1223165107005556$
            # - Beautiful day, isn't it? On days like this, I love to pack a lunch and go on a picnic.
            return 40
        elif self.index == 1:
            # $script:1223165107005557$
            # - Do you like rainbow trout soup? I cook it with my own blend of spices. Everyone says it's the best soup in town.
            if pick == 0:
                # $script:1223165107005558$
                # - <i>I'll</i> be the judge of that!
                return 41
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:1223165107005559$
        # - Ha! All right. Come over to my house sometime, and I'll cook it for you!
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0201104007005858$
            # - Ah, $MyPCName$. I've got some good news for you. A little while back, $npcName:11001396[gender:1]$ came to see me along with $npcName:11001443[gender:0]$. He asked me to gather the villagers, and then told us about what he'd learned about the people suffering in $map:02010005$. He even brought some materials for us to examine.
            return 50
        elif self.index == 1:
            # $script:0201133107005859$
            # - I couldn't understand all the words he used, but I knew what he was trying to say. What they're suffering from is neither a curse nor a disease. $MyPCName$, you were able to come and go without getting sick. So did $npcName:11001443[gender:0]$ and myself. We're the proof of his findings.
            return 50
        elif self.index == 2:
            # $script:0201104007005859$
            # - We decided the affected people shouldn't be left in that old hut, though the decision was not agreed to by all. We've moved them to some of our own houses, as well as the doctor's place.
            if pick == 0:
                # $script:0201104007005860$
                # - Where are $npcName:11001391[gender:0]$ and $npcName:11001392[gender:1]$?
                return 51
            return -1
        return -1

    def __51(self, pick: int) -> int:
        # $script:0201104007005861$
        # - Ha, don't worry. They're in my house. They're not in the best shape, though. So skinny... must have been tough on them. But with some good food and good sleep, they'll be as good as new in no time. 
        if pick == 0:
            # $script:0201104007005862$
            # - That's very kind of you.
            return 52
        return -1

    def __52(self, pick: int) -> int:
        # $script:0201104007005863$
        # - Oh, not at all. If anyone's generous here it's you, $MyPCName$. You went out on a limb to help people that you really didn't know. Being so compassionate and talented, you're bound to be successful in whatever you do. 
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (40, 0):
            return Option.NEXT
        elif (self.state, self.index) == (40, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.NEXT
        elif (self.state, self.index) == (50, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (52, 0):
            return Option.CLOSE
        return Option.NONE
