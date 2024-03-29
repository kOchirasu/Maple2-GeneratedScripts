""" 11000508: Ophelia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000473$
        # - And... that's another sword fresh off the grinding stone! What a beaut. This will make for one happy customer... Oh hi there, can I help you? 
        return None # TODO

    def __10(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000477$
            # - And... that's another sword fresh off the grinding stone! What a beaut. This will make for one happy customer... Oh hi there, can I help you?
            return 10
        elif self.index == 1:
            # $script:0323154410001454$
            # - Ah now, let me guess... You want to enchant your gear? Let's have a look, then!
            if pick == 0:
                # $script:0831180610000478$
                # - Can you enchant my items?
                return 31
            elif pick == 1:
                # $script:0323154410001455$
                # - How about we change some bonus attributes?
                return 30
            elif pick == 2:
                # $script:0323154410001456$
                # - Tell me about your work.
                return 29
            return -1
        return -1

    def __29(self, pick: int) -> int:
        if self.index == 0:
            # $script:0330140410001950$
            # - Everyone knows I'm the best smith... on this street.
            return 29
        elif self.index == 1:
            # $script:0330140410001951$
            # - Great artisans are a dime-a-dozen in $map:2000076$. This is the place to be if you aim to make a living at crafting. It makes competition fierce, sure, but that only forces me to push myself harder. And it's kind of inspirational, being around all these people who live for their craft.
            return 29
        elif self.index == 2:
            # $script:0330140410001952$
            # - Anyway, if you want to strengthen your equipment, come to me. Just remember that you'll need to bring some special materials. You probably know which ones... the $itemPlural:40100001$, $itemPlural:40100023$, and $itemPlural:40100024$ that $map:2000051$ is so famous for.
            return 29
        elif self.index == 3:
            # $script:0330140410001953$
            # - You can get $itemPlural:40100023$ by dismantling gear that's level 20 or higher. Just use the Dismantle button in your inventory window. As for $itemPlural:40100024$, that comes at a much higher cost. It only comes from dismantling gear that is epic or better.
            return 29
        elif self.index == 4:
            # $script:0330140410001954$
            # - People compete for $itemPlural:40100023$ in the Personal Arena, so you could go there. If you think you can win, that is...
            return 29
        elif self.index == 5:
            # $script:0330140410001955$
            # - By the way, Elliana got ahold of yet another strange weapon, and she's been begging me to enchant it for her. I told her such flashy, impractical weapons like that can't be enchanted, but she doesn't listen. Why can't she just accept that only items marked as "Can be Enchanted" can, well, be enchanted?
            return 29
        elif self.index == 6:
            # $script:0330140410001956$
            # - That's not all! Aside from functioning as weaponry or armor, high-grade gear imparts special abilities. But there's a catch: these abilities are completely random! If you would prefer gear that better suits your needs, I can help you modify the gear.
            return 29
        elif self.index == 7:
            # $script:0330140410001957$
            # - Have you heard about $itemPlural:40100026$? They were invented by those eggheads in $map:02000270$. I hear they're made from real meteors! With a material like that, I can change the bonus attributes on a piece of gear.
            return 29
        elif self.index == 8:
            # $script:0330140410001958$
            # - It's not some magic bullet, of course. There's no telling what new attribute you'll wind up with. And don't forget, I also need $itemPlural:40100001$, $itemPlural:40100002$, $itemPlural:40100003$, or $itemPlural:40100021$ to go with the $itemPlural:40100026$.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # functionID=1 
        # $script:0323154410001460$
        # - Do you want to change the bonus attributes on your gear? Then pick an item to change! Just remember that it needs to be epic or better armor and accessories at level 50 and above.
        return -1

    def __31(self, pick: int) -> int:
        # functionID=1 
        # $script:0330140710001959$
        # - Okay, let's see the gear you want to enchant. I'm warning you now, it has to be marked with "Can be Enchanted."
        return -1

    def __999(self, pick: int) -> int:
        # $script:0831180610000568$
        # - Ho boy, I'm busy! Busy, busy, busy... If you were hoping for my services, I just don't have the time right now. I'm working on a special order from the palace.
        if pick == 0:
            # $script:0831180610000569$
            # - Can you enchant my items?
            return 41
        elif pick == 1:
            # $script:0831180610000570$
            # - What do you do?
            return 39
        return -1

    def __39(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000571$
            # - Isn't it obvious? I'm a blacksmith! The best one there is, too. Well, on this street.
            return 39
        elif self.index == 1:
            # $script:0831180610000572$
            # - The thing is that <font color="#ffd200">$map:2000076$</font> is absolutely lousy with craftsmen and women. This is the heart of the blacksmithing trade for Maple World, and that makes competition fierce. But that competition is inspiring for people like me. I learn a lot from my peers, and I relate to people who are willing to pour their heart and soul into their work.
            return 39
        elif self.index == 2:
            # $script:0831180610000573$
            # - You're not here to talk about me though, are you? You need your gear tuned up, I'm your woman. All I need are the right materials, and I'll work my magic. You know what I'm talking about, right? $itemPlural:40100001$, $itemPlural:40100023$, and $itemPlural:40100024$, all produced in $map:2000051$, usually.
            return 39
        elif self.index == 3:
            # $script:0831180610000574$
            # - <font color="#ffd200">$itemPlural:40100023$</font> come from <font color="#ffd200">dismantling</font> gear that's level 20 or higher. Just use the <font color="#ffd200">Dismantle</font> button in your inventory window. As for <font color="#ffd200">$itemPlural:40100024$</font>, you'll need to dismantle gear that is rated Epic or better.
            return 39
        elif self.index == 4:
            # $script:0831180610000575$
            # - People compete for <font color="#ffd200">$itemPlural:40100023$</font> in the <font color="#ffd200">Personal Arena</font>, so you could go there. If you think you can win, that is...
            return 39
        elif self.index == 5:
            # $script:0831180610000576$
            # - Keep in mind that the only items you can enchant are Top, Bottom, Suit, and Weapon items at level 20 or above. That frustrates some folks, but I need a solid base to work from. Elliana found some weird weapon she wanted to enchant, but she doesn't get that there are rules to these things. I'm good, but even I have my limits!
            return -1
        return -1

    def __41(self, pick: int) -> int:
        # $script:0831180610000577$
        # - I'd love to help you, but right now I have to focus on this special order from the palace.
        #   No exceptions! Absolutely not! 
        #   You wouldn't want me to stop your order to work on someone else's, so why would you expect me to do that to the palace?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.NEXT
        elif (self.state, self.index) == (10, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (29, 0):
            return Option.NEXT
        elif (self.state, self.index) == (29, 1):
            return Option.NEXT
        elif (self.state, self.index) == (29, 2):
            return Option.NEXT
        elif (self.state, self.index) == (29, 3):
            return Option.NEXT
        elif (self.state, self.index) == (29, 4):
            return Option.NEXT
        elif (self.state, self.index) == (29, 5):
            return Option.NEXT
        elif (self.state, self.index) == (29, 6):
            return Option.NEXT
        elif (self.state, self.index) == (29, 7):
            return Option.NEXT
        elif (self.state, self.index) == (29, 8):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (31, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (999, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (39, 0):
            return Option.NEXT
        elif (self.state, self.index) == (39, 1):
            return Option.NEXT
        elif (self.state, self.index) == (39, 2):
            return Option.NEXT
        elif (self.state, self.index) == (39, 3):
            return Option.NEXT
        elif (self.state, self.index) == (39, 4):
            return Option.NEXT
        elif (self.state, self.index) == (39, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (41, 0):
            return Option.CLOSE
        return Option.NONE
