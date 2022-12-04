""" 11000042: Orde """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        # TODO: Job 1
        # TODO: RandomPick 10,20,30,40,50,60,70,80,90,100,110,120
        return 0 # Default

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180610000107$
        # - Ugh... I hate being bothered. What is it?
        return None # TODO

    def __1(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000108$
            # - Honestly, I don't care about politics or the court. My time is much better spent reading books in $map:02000031$.
            return 1
        elif self.index == 1:
            # functionID=1 
            # $script:0831180610000109$
            # - People don't understand the value to be found in dusty tomes and conversing with the fairies in $map:02000023$. But you have a certain inquisitiveness in your eyes, an intellectual spark. You might make a good Wizard. I'm not going to push, but if you're the arcane arts, I'd be willing to assist you.
            return None # TODO
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610000110$
        # - Honestly, I don't care about politics or the court, and you shouldn't waste your time on things like that either. Come see me if you ever want to discuss what actually matters in this world. I've got plenty of wisdom to share.
        if pick == 0:
            # $script:0831180610000111$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0831180610000112$
            # - What caused the earthquake?
            return 12
        return -1

    def __11(self, pick: int) -> int:
        # $script:0831180610000113$
        # - It seems the simple minds of ordinary folk can't understand us Wizards. We're more interested in scholarly matters, like understanding the origin of this world and what caused the earthquake, than we are in whether the empress holds her court.
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000114$
            # - Some people think the earthquake was not a naturally occurring phenomenon, and I'm inclined to agree with them. There's evidence to support such a theory...
            return 12
        elif self.index == 1:
            # $script:0831180610000115$
            # - And you have to admit, it's suspicious that the palace canceled court, which would have been the first one in quite a long time, just because of a simple earthquake. Very suspicious indeed...
            return -1
        return -1

    def __13(self, pick: int) -> int:
        # $script:0607163510001504$
        # - What could I possibly have to discuss with you? You and I have nothing in common. Are you looking for magical body-building tips or something? We of the arcane arts don't waste our time trying to enhance our physical forms, as we know that the font of our power lies within.
        if pick == 0:
            # $script:0607163510001505$
            # - I'm simply pursuing my fullest potential, just like you're doing.
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:0607163510001506$
        # - Ultimate potential? <i>Suuuure</i>, I can help. Unleash your "ultimate potential" with my patented brew of enchanted smoothies! They can be yours for the low, low price of 1,200 mesos! Pffft. You sound like you've been roped into some kind of scam.
        if pick == 0:
            # $script:0607181410001555$
            # - Let's talk about something else.
            return 110
        return -1

    def __15(self, pick: int) -> int:
        # $script:0806014810001601$
        # - Are you still here? I'd suggest you stop wasting my time, before I make you a guinea pig for my magical studies.
        if pick == 0:
            # $script:0806014810001602$
            # - Do you know who I am?
            return 16
        return -1

    def __16(self, pick: int) -> int:
        if self.index == 0:
            # $script:0806014810001603$
            # - What, are you some kind of celebrity to the common-folk? Why would I know anything about— Woah... what's up with your aura?
            return 16
        elif self.index == 1:
            # $script:0806014810001604$
            # - I didn't notice it while I was busy trying to ignore you, but your aura is like nothing I've ever seen. I sense two opposing forces swirling within you.
            #   It's like watching two stupid salamanders trying to swallow each others' tails.
            return 16
        elif self.index == 2:
            # $script:0806014810001605$
            # - The first energy unlike anything ever described within the <i>Encyclopedia Arcana</i>... It almost resembles the energy of nature, but... it's so condensed. Incredible. I would never have believed a mortal could accumulate so much power in a single lifetime.
            return 16
        elif self.index == 3:
            # $script:0806014810001606$
            # - And the second is something darker. It's almost feels like... No, that's not possible.
            if pick == 0:
                # $script:0806014810001607$
                # - I don't know what you're talking about.
                return 17
            return -1
        return -1

    def __17(self, pick: int) -> int:
        # $script:0806014810001608$
        # - Just what in the world are you?
        if pick == 0:
            # $script:0806014810001609$
            # - I have no memory of my past.
            return 18
        return -1

    def __18(self, pick: int) -> int:
        # $script:0806014810001610$
        # - Huh? Really? Were you in some kind of accident...? Come closer. I know just the spell for reading memories.
        if pick == 0:
            # $script:0806014810001611$
            # - (Move closer.)
            return 19
        return -1

    def __19(self, pick: int) -> int:
        if self.index == 0:
            # $script:0806014810001612$
            # - Stay perfectly still.
            #   <font color="#909090">(She places her hand on your head and begins to recite an incantation. A spark leaps from her finger tips, and your head starts to feel fuzzy.)</font>
            return 19
        elif self.index == 1:
            # $script:0806014810001613$
            # - I can't see anything... There's a thick purple haze swirling around inside your head, it's obstructing my view.
            return 19
        elif self.index == 2:
            # $script:0806014810001614$
            # - I don't believe it. Could you really be...!? No, it's better not to rush to any conclusions. I've got to consult with my colleagues. In the mean time, I'll be keeping an eye on you. Please leave now.
            if pick == 0:
                # $script:0806014810001615$
                # - Change the subject.
                return 120
            return -1
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180610000116$
        # - A Wizard's life is lonely and difficult. We can never stop studying until we reach the very zenith of magical knowledge. You've got quite a road ahead of you. Is there anything you want to ask a fellow scholar?
        if pick == 0:
            # $script:0831180610000117$
            # - What should I do now?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000120$
            # - Before begin your journey, you should see that you're properly equipped. $npc:11000004[gender:0]$ is a purveyor of fine equipment, and probably has some adequate Wizard gear for sale. Buy whatever supplies are necessary, and venture out into that great, wide world to expand your knowledge!
            return 21
        elif self.index == 1:
            # $script:0831180610000121$
            # - As your studies progress, you will attain new levels. This will allow you to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
            return -1
        return -1

    def __22(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000122$
            # - When you're ready to <font color="#ffd200">upgrade a skill</font>, just press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
            return 22
        elif self.index == 1:
            # $script:0831180610000123$
            # - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
            return -1
        return -1

    def __23(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000124$
            # - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>. 
            return 23
        elif self.index == 1:
            # $script:0831180610000125$
            # - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
            return 23
        elif self.index == 2:
            # $script:0831180610000126$
            # - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently. It would be best to hunt such foes with a party.
            return 23
        elif self.index == 3:
            # $script:0831180610000127$
            # - And as for $itemPlural:40100022$—well, you can learn about those on your own.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180610000128$
        # - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Knight.
        if pick == 0:
            # $script:0831180610000129$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0831180610000130$
            # - What caused the earthquake?
            return 12
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180610000131$
        # - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Berserker.
        if pick == 0:
            # $script:0831180610000132$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0831180610000133$
            # - What caused the earthquake?
            return 12
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180610000134$
        # - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Priest.
        if pick == 0:
            # $script:0831180610000135$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0831180610000136$
            # - What caused the earthquake?
            return 12
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180610000137$
        # - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Archer.
        if pick == 0:
            # $script:0831180610000138$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0831180610000139$
            # - What caused the earthquake?
            return 12
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180610000140$
        # - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Heavy Gunner.
        if pick == 0:
            # $script:0831180610000141$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0831180610000142$
            # - What caused the earthquake?
            return 12
        return -1

    def __80(self, pick: int) -> int:
        # $script:0831180610000143$
        # - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Thief.
        if pick == 0:
            # $script:0831180610000144$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0831180610000145$
            # - What caused the earthquake?
            return 12
        return -1

    def __90(self, pick: int) -> int:
        # $script:0831180610000146$
        # - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Assassin.
        if pick == 0:
            # $script:0831180610000147$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0831180610000148$
            # - What caused the earthquake?
            return 12
        return -1

    def __100(self, pick: int) -> int:
        # $script:1216124310001325$
        # - Honestly, we don't care about politics or the empress's court. Nor do we care that you've chosen the path of the Runeblade.
        if pick == 0:
            # $script:1216124310001326$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:1216124310001327$
            # - What caused the earthquake?
            return 12
        return -1

    def __110(self, pick: int) -> int:
        # $script:0607163510001507$
        # - Honestly, we don't care about politics or the empress's court... nor do we care who you are. Our interests lie in more scholarly pursuits.
        if pick == 0:
            # $script:0607163510001508$
            # - What do you care about, then?
            return 11
        elif pick == 1:
            # $script:0607163510001509$
            # - Do you know what caused the earthquake?
            return 12
        elif pick == 2:
            # $script:0607163510001510$
            # - There's another subject I'd like to ask you about.
            return 13
        return -1

    def __120(self, pick: int) -> int:
        # $script:0806014810001616$
        # - Honestly, we don't care about politics or the empress's court... nor do we care who you are. Our interests lie in more scholarly pursuits.
        if pick == 0:
            # $script:0806014810001617$
            # - What do you care about?
            return 11
        elif pick == 1:
            # $script:0806014810001618$
            # - What caused the earthquake?
            return 12
        elif pick == 2:
            # $script:0806014810001619$
            # - There's another subject I'd like to ask you about.
            return 15
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1, 1):
            return Option.CHANGE_JOB
        elif (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (13, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (14, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (15, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (16, 0):
            return Option.NEXT
        elif (self.state, self.index) == (16, 1):
            return Option.NEXT
        elif (self.state, self.index) == (16, 2):
            return Option.NEXT
        elif (self.state, self.index) == (16, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (17, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (18, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (19, 0):
            return Option.NEXT
        elif (self.state, self.index) == (19, 1):
            return Option.NEXT
        elif (self.state, self.index) == (19, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (20, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (21, 0):
            return Option.NEXT
        elif (self.state, self.index) == (21, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (22, 0):
            return Option.NEXT
        elif (self.state, self.index) == (22, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (23, 0):
            return Option.NEXT
        elif (self.state, self.index) == (23, 1):
            return Option.NEXT
        elif (self.state, self.index) == (23, 2):
            return Option.NEXT
        elif (self.state, self.index) == (23, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (80, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (90, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (100, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (110, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (120, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
