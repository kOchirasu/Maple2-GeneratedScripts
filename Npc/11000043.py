""" 11000043: Trini """
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
        # $script:0831180610000149$
        # - How may I help you?
        return None # TODO

    def __1(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000150$
            # - The recent earthquake has struck fear into the hearts of many. We restore the people's hope by spreading the goddess's teachings. Would you join us on our holy mission? You seem more than qualified to serve the goddess.
            return 1
        elif self.index == 1:
            # functionID=1 
            # $script:0831180610000151$
            # - Illuminate this world with your good heart and unshakable faith.
            #   The goddess awaits with open arms all who you will shepherd into the light.
            return None # TODO
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610000152$
        # - The recent earthquake has struck fear into the hearts of many. We restore the people's hope by spreading the goddess's teachings. Would you join us on our holy mission? 
        if pick == 0:
            # $script:0831180610000153$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0831180610000154$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000155$
            # - The road between $map:02000062$ and $map:02000001$ bore the brunt of the earthquake's damage. Fortunately, the road was nearly deserted when the shaking began.
            return 11
        elif self.index == 1:
            # $script:0831180610000156$
            # - I know that many are disappointed about the court's cancellation, but I think the can all agree that our current focus should be on supporting one another, and dealing with the damage of the quake.
            return -1
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000157$
            # - Oh, what a silly question! She's the empress, of course. $npc:11000075[gender:1]$ was surely just as disappointed about the court as everyone else, but her safety is paramount to Maple World.
            return 12
        elif self.index == 1:
            # $script:0831180610000158$
            # - If you're here for an audience with the Empress, you might as well go home. She's too busy these days governing the realm. Since the incident, the people have relied on her strong leadership more than ever.
            return -1
        return -1

    def __13(self, pick: int) -> int:
        # $script:0607163510001511$
        # - $MyPCName$, do you believe in... the Light?
        if pick == 0:
            # $script:0607163510001512$
            # - I only believe in what I can see.
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:0607163510001513$
        # - The Light shines on everyone, regardless of their belief or lack of belief.
        if pick == 0:
            # $script:0607163510001514$
            # - What's the Light ever done for the poor of $map:02000100$?
            return 15
        return -1

    def __15(self, pick: int) -> int:
        # $script:0607163510001515$
        # - I believe the ordeals we experience throughout life are ultimately blessings in disguise, arranged by the Light. Hardship happens for a reason. I shall pray for you and everyone else. May the Light's blessing be with you wherever you go.
        if pick == 0:
            # $script:0607163510001516$
            # - Let's talk about something else.
            return 110
        return -1

    def __16(self, pick: int) -> int:
        # $script:0806014810001620$
        # - $MyPCName$, do you believe in... the Light?
        if pick == 0:
            # $script:0806014810001621$
            # - What do you mean by "the light"?
            return 17
        return -1

    def __17(self, pick: int) -> int:
        # $script:0806014810001622$
        # - The Light <font color="#ffd200">shines on everyone</font>, regardless of their belief or lack of belief.
        #   It <font color="#ffd200">guides</font> you through the darkness, keeping you from wandering astray.
        if pick == 0:
            # $script:0806014810001623$
            # - No light has ever guided me.
            return 18
        return -1

    def __18(self, pick: int) -> int:
        if self.index == 0:
            # $script:0806014810001624$
            # - You just haven't noticed it. I can see it all around you, though it is rather dim.
            return 18
        elif self.index == 1:
            # $script:0806014810001625$
            # - You may not realize it, but that warm light is guiding you along your path.
            #   <font color="#909090">(You think <i>that's</i> a rich presumption. Doesn't this person know that this light has nothing to do with you? Your guide is the Lone Spirit and the Master's teachings.)</font>
            if pick == 0:
                # $script:0806014810001626$
                # - Change the subject.
                return 120
            return -1
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180610000159$
        # - Don't forget, you're now an agent of the Empress and, by extension, an agent of the goddess. It is your duty to perform good deeds and help the weak. Now, do you have any questions?
        if pick == 0:
            # $script:0831180610000160$
            # - What should I do now?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000163$
            # - To help the weak and needy, you yourself must be strong. $npc:11000004[gender:0]$ is a merchant of fine equipment, and probably has some excellent Priest gear for sale. Once you're properly equipped, you should venture forth and enact the will of the goddess.
            return 21
        elif self.index == 1:
            # $script:0831180610000164$
            # - In your service to the goddess, you'll inevitably reach new levels. When this happens you'll be able to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
            return -1
        return -1

    def __22(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000165$
            # - Press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
            return 22
        elif self.index == 1:
            # $script:0831180610000166$
            # - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
            return -1
        return -1

    def __23(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000167$
            # - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>.
            return 23
        elif self.index == 1:
            # $script:0831180610000168$
            # - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
            return 23
        elif self.index == 2:
            # $script:0831180610000169$
            # - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently.
            return 23
        elif self.index == 3:
            # $script:0831180610000170$
            # - $itemPlural:40100022$, you are dangerous, and must be handled with care.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180610000171$
        # - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Knight. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0831180610000172$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0831180610000173$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180610000174$
        # - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Berserker. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0831180610000175$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0831180610000176$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180610000177$
        # - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Wizard. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0831180610000178$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0831180610000179$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180610000180$
        # - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Archer. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0831180610000181$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0831180610000182$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180610000183$
        # - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Heavy Gunner. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0831180610000184$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0831180610000185$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __80(self, pick: int) -> int:
        # $script:0831180610000186$
        # - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Thief. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0831180610000187$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0831180610000188$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __90(self, pick: int) -> int:
        # $script:0831180610000189$
        # - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Assassin. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0831180610000190$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0831180610000191$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __100(self, pick: int) -> int:
        # $script:1216124310001328$
        # - I'm afraid you cannot join the priesthood, as you've already chosen the path of the Runeblade. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:1216124310001329$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:1216124310001330$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        return -1

    def __110(self, pick: int) -> int:
        # $script:0607163510001517$
        # - I'm afraid you cannot join the priesthood, as you've already chosen your path. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0607163510001518$
            # - Did the earthquake cause a lot of damage?
            return 11
        elif pick == 1:
            # $script:0607163510001519$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        elif pick == 2:
            # $script:0607163510001520$
            # - Let's change the subject.
            return 13
        return -1

    def __120(self, pick: int) -> int:
        # $script:0806014810001627$
        # - I'm afraid you cannot join the priesthood, as you've already chosen your path. Nonetheless, I pray for your prosperity.
        if pick == 0:
            # $script:0806014810001628$
            # - How bad was the quake?
            return 11
        elif pick == 1:
            # $script:0806014810001629$
            # - Who is $npc:11000075[gender:1]$?
            return 12
        elif pick == 2:
            # $script:0806014810001630$
            # - Talk to $npcName:11000043[gender:1]$ about a different subject.
            return 16
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1, 1):
            return Option.CHANGE_JOB
        elif (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.NEXT
        elif (self.state, self.index) == (11, 1):
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (17, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (18, 0):
            return Option.NEXT
        elif (self.state, self.index) == (18, 1):
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
