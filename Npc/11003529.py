""" 11003529: Galileo """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0824002407008893$
        # - Need something?
        return None # TODO

    def __30(self, pick: int) -> int:
        if self.index == 0:
            # $script:0824002407008894$
            # - Welcome to the Xenon Systems Research Lab. I want to thank you for joining our study. It wasn't easy finding a guild to participate in our experiment, but I suspect you just might enjoy it!
            return 30
        elif self.index == 1:
            # $script:0906182007008914$
            # - Do you have any questions?
            if pick == 0:
                # $script:0906182007008915$
                # - What's the Xenon System?
                return 31
            elif pick == 1:
                # $script:0906182007008916$
                # - Why do you need guild members for your test?
                return 41
            elif pick == 2:
                # $script:0906182007008917$
                # - What's this newfangled "virtual reality" thing?
                return 51
            elif pick == 3:
                # $script:0906182007008918$
                # - I'm ready to get my VR on!
                return 61
            return -1
        return -1

    def __31(self, pick: int) -> int:
        if self.index == 0:
            # $script:0906182007008919$
            # - The Xenon System is a combat simulation conducted in virtual reality based on the premise of psychic resonance. In layman's terms, it's an array of minds working in harmony with a computer to create a virtual world.
            return 31
        elif self.index == 1:
            # $script:0906182007008920$
            # - Essentially, the computer draws on the memories of everyone connected to create a simulated world that is almost indistinguishable from reality. This simulation is the perfect place to safely run all manner of tests.
            return 31
        elif self.index == 2:
            # $script:0906182007008921$
            # - You may already be familiar with our technology's predecessor. Have you ever participated in a Chaos Raid? 
            if pick == 0:
                # $script:0906182007008922$
                # - I've participated before.
                return 32
            elif pick == 1:
                # $script:0906182007008923$
                # - Nope, never.
                return 33
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0906182007008924$
        # - I see! Yes, you carry yourself like someone who has overcome great trials.
        if pick == 0:
            # $script:0906182007008925$
            # - It wasn't that big of a deal.
            return 34
        elif pick == 1:
            # $script:0906182007008926$
            # - Uhh. Thank... you...?
            return 34
        return -1

    def __33(self, pick: int) -> int:
        # $script:0906182007008927$
        # - Ah, is that so? If I was still young and lithe like you, I'd be running headfirst into danger at every opportunity. You really should take on the challenge, at least once.
        if pick == 0:
            # $script:0906182007008928$
            # - Maybe I'll give it a go.
            return 34
        elif pick == 1:
            # $script:0906182007008929$
            # - That's nice.
            return 34
        return -1

    def __34(self, pick: int) -> int:
        if self.index == 0:
            # $script:0906182007008930$
            # - Ermm... In any case, we've learned a great deal by analyzing data about individuals participating in Chaos Raids, such as how shared hardships lead to team bonding, which in turn lead to greater cooperation, and greater success in battle.
            return 34
        elif self.index == 1:
            # $script:0906182007008931$
            # - However, as scientific tools, the Chaos Raid simulations are inferior. They are little more than a glorified entertainment system, if I'm being honest.
            return 34
        elif self.index == 2:
            # $script:0906182007008932$
            # - But now with the Xenon System, we can expose our guinea pi–errm, volunteers, to all sorts of situations, and conduct studies of real scientific value! It truly is a technological marvel.
            return 34
        elif self.index == 3:
            # $script:0906182007008933$
            # - The possibilities are endless! Everyone from the Royal Guard to the fire brigade can train in real-world situation without risk. Adventurers can visit places they never dreamed of. And I can finally take a vacation without ever leaving the lab! Of course, none of this would be possible without the support of our generous benefactor $npcName:11000264[gender:0]$.
            return 34
        elif self.index == 4:
            # $script:0906182007008934$
            # - Do you have any more questions?
            if pick == 0:
                # $script:0906182007008935$
                # - Why do you need guild members for your test?
                return 41
            elif pick == 1:
                # $script:0906182007008936$
                # - What's this newfangled "virtual reality" thing?
                return 51
            elif pick == 2:
                # $script:0906182007008937$
                # - I'm ready to get my VR on!
                return 61
            return -1
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0906182007008938$
            # - I wanted to put together a group study with a shared history, one conducive to cooperation.
            return 41
        elif self.index == 1:
            # $script:0906182007008939$
            # - After all, the greatest achievements in history come when a group of likeminded individuals unite behind a common cause.
            return 41
        elif self.index == 2:
            # $script:0906182007008940$
            # - There's no better example of this in everyday life than the communal efforts of guilds. I thought them a fitting subject of my test.
            return 41
        elif self.index == 3:
            # $script:0906182007008941$
            # - I hear we're offering an excellent compensation package for the study, although payroll is not my department. Personally, I think it's reward enough have contributed to the advancement of science, and to try out our amazing simulation. But whatever your motives, thank you for participating! 
            return 41
        elif self.index == 4:
            # $script:0906182007008942$
            # - Do you have any more questions?
            if pick == 0:
                # $script:0906182007008943$
                # - What's the Xenon System?
                return 31
            elif pick == 1:
                # $script:0906182007008944$
                # - What's this newfangled "virtual reality" thing?
                return 51
            elif pick == 2:
                # $script:0906182007008945$
                # - I'm ready to get my VR on!
                return 61
            return -1
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0906182007008946$
            # - Virtual reality is a simulated experience designed to believably replicate the real world. Each curated scenario is run on a separate computer server or "Link."
            return 51
        elif self.index == 1:
            # $script:0906182007008947$
            # - Each Link consists of a unique environment with its own hand-tailored objective.
            return 51
        elif self.index == 2:
            # $script:0906182007008948$
            # - Your goal, for the purposes of the study, is to cooperate with your guild members and complete the assigned objective.
            return 51
        elif self.index == 3:
            # $script:0906182007008949$
            # - I have to warn you, our simulations still have some kinks that need working out... You may run into situations or foes that are impossible to overcome, even with your substantial abilities. At such times, you'll need to input override codes provided by the lab.
            return 51
        elif self.index == 4:
            # $script:0906182007008950$
            # - <font color="#ffd200">Override Code</font> items are sold by your <font color="#ffd200">Guild Supply Merchant</font>. I wish we could give them away for free, but these little technological wonders are incredibly sophisticated and costly to produce.
            return 51
        elif self.index == 5:
            # $script:0906182007008951$
            # - As I've said, the various Links are all still under active development. As you proceed to complete the objectives of each simulation in order, we will analyze the data we collect, and use it to fine-tune the subsequent Links.
            return 51
        elif self.index == 6:
            # $script:0906182007008952$
            # - There's still a great deal of science to be done. I hope we can depend on your ongoing contribution!
            return 51
        elif self.index == 7:
            # $script:0906182007008953$
            # - Do you have any more questions?
            if pick == 0:
                # $script:0906182007008954$
                # - What's the Xenon System?
                return 31
            elif pick == 1:
                # $script:0906182007008955$
                # - Why do you need guild members for your test?
                return 41
            elif pick == 2:
                # $script:0906182007008956$
                # - I'm ready to get my VR on!
                return 61
            return -1
        return -1

    def __61(self, pick: int) -> int:
        if self.index == 0:
            # $script:0906182007008957$
            # - Wonderful. I've already booted up the system. When you're ready to access the Link, please enter one of the simulation pods.
            return 61
        elif self.index == 1:
            # $script:0906182007008958$
            # - There's no need to be nervous. Nothing in this simulation can inflict any <i>permanent</i> harm. That said, the study will be meaningless unless you take the scenario seriously!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.NEXT
        elif (self.state, self.index) == (30, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.NEXT
        elif (self.state, self.index) == (31, 1):
            return Option.NEXT
        elif (self.state, self.index) == (31, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (33, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (34, 0):
            return Option.NEXT
        elif (self.state, self.index) == (34, 1):
            return Option.NEXT
        elif (self.state, self.index) == (34, 2):
            return Option.NEXT
        elif (self.state, self.index) == (34, 3):
            return Option.NEXT
        elif (self.state, self.index) == (34, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.NEXT
        elif (self.state, self.index) == (41, 2):
            return Option.NEXT
        elif (self.state, self.index) == (41, 3):
            return Option.NEXT
        elif (self.state, self.index) == (41, 4):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.NEXT
        elif (self.state, self.index) == (51, 2):
            return Option.NEXT
        elif (self.state, self.index) == (51, 3):
            return Option.NEXT
        elif (self.state, self.index) == (51, 4):
            return Option.NEXT
        elif (self.state, self.index) == (51, 5):
            return Option.NEXT
        elif (self.state, self.index) == (51, 6):
            return Option.NEXT
        elif (self.state, self.index) == (51, 7):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.NEXT
        elif (self.state, self.index) == (61, 1):
            return Option.CLOSE
        return Option.NONE
