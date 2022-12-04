""" 11000102: Bunny Gal """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180407000399$
        # - How may I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0831180407000400$
        # - Oh, hello! How do you like $map:02000064$ so far?
        if pick == 0:
            # $script:0831180407000401$
            # - What are you doing?
            return 51
        elif pick == 1:
            # $script:0831180407000402$
            # - What events does the palace sponsor?
            return 52
        elif pick == 2:
            # $script:0831180407000403$
            # - How can I participate in mini-games?
            return 53
        elif pick == 3:
            # $script:0831180407000404$
            # - What do I get for winning mini-games?
            return 54
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000405$
            # - What am I doing?  Can't you see? I'm dancing for everyone who came to $map:02000064$. Some folks have said I should stop because of the earthquake, but I don't get it.
            return 51
        elif self.index == 1:
            # $script:0831180407000406$
            # - Come on, don't be so serious. Don't wallow in disappointment. We should cheer up and stay optimistic. Even $npcName:11000075[gender:1]$ said so!
            return 51
        elif self.index == 2:
            # $script:0831180407000407$
            # - And don't push yourself too hard. Sometimes you need to take a break and collect yourself. Maple World has all kinds of fun and exciting events to keep you busy. You can meet new people and win fabulous prizes, too!
            return -1
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000408$
            # - Oh man, I thought everybody knew about those! The palace advertises them everywhere. Okay, well, I can still tell you about it.
            return 52
        elif self.index == 1:
            # $script:0831180407000409$
            # - The palace sponsors many events all across Maple World. A decade ago, when Maple World faced one of the greatest challenges in its history, $npcName:11000075[gender:1]$ decided to do something to help distract the people from their worries.
            return 52
        elif self.index == 2:
            # $script:0831180407000410$
            # - She said that Maple World needs something to bring people together. Since then, we've held all sorts of games on a regular basis for the benefit of the people.
            return 52
        elif self.index == 3:
            # $script:0831180407000411$
            # - Of course, Maple World is still not completely safe. The recent earthquake, for instance... Oops, I shouldn't have mentioned that. A-anyway, these events are important just in how much they help the morale of the populace. 
            return -1
        return -1

    def __53(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000412$
            # - Participating in mini-games is easy! $npcName:11001899$ will make an announcement anytime a game goes live. All you have to do is play!
            return 53
        elif self.index == 1:
            # $script:0831180407000413$
            # - And even if you're feeling lazy and not up for traveling, there's no need to worry! You can teleport to mini-games from anywhere in the universe! When the Event Notification window appears, just press Enter next to the event you want to join!
            return 53
        elif self.index == 2:
            # $script:0831180407000414$
            # - Well, what are you standing around here for? Go play some mini-games!
            return -1
        return -1

    def __54(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180407000415$
            # - Win palace-sponsored events to receive the blessing of $npcName:11000075[gender:1]$. It's a great honor, you know!
            return 54
        elif self.index == 1:
            # $script:0831180407000416$
            # - And that's not all! You'll earn mesos, nice skins, and useful potions, too. A lot of people come to this place, dreaming of wealth and fame.
            return 54
        elif self.index == 2:
            # $script:0831180407000417$
            # - Oh, right. When you join $map:61000001$ or $map:61000002$ games, keep an eye out for the merchants who sell interesting items! That should make your time in $map:02000064$ even more worthwhile!
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.NEXT
        elif (self.state, self.index) == (51, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (52, 0):
            return Option.NEXT
        elif (self.state, self.index) == (52, 1):
            return Option.NEXT
        elif (self.state, self.index) == (52, 2):
            return Option.NEXT
        elif (self.state, self.index) == (52, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (53, 0):
            return Option.NEXT
        elif (self.state, self.index) == (53, 1):
            return Option.NEXT
        elif (self.state, self.index) == (53, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (54, 0):
            return Option.NEXT
        elif (self.state, self.index) == (54, 1):
            return Option.NEXT
        elif (self.state, self.index) == (54, 2):
            return Option.CLOSE
        return Option.NONE
