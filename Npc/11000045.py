""" 11000045: Ikas """
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
        # $script:0831180610000192$
        # - Whatever this is, please get to the point.
        return None # TODO

    def __1(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000193$
            # - The Green Hoods are a militia group with a long, storied history. Right now, we're keeping an eye on the opportunists who might try to take advantage of the chaos of recent events. We want to prevent as much crime as possible, but that requires talent and mettle. And you... you look like you've got both of those.
            return 1
        elif self.index == 1:
            # functionID=1 
            # $script:0831180610000194$
            # - Our sharp arrows never miss their targets. How would you like to join us on our mission to restore order to this world?
            return None # TODO
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610000195$
        # - The Green Hoods are a militia group with a long, storied history. How'd you like to join us and punish those who would do the world harm?
        if pick == 0:
            # $script:0831180610000196$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0831180610000197$
            # - Tell me about the criminals.
            return 12
        return -1

    def __11(self, pick: int) -> int:
        # $script:0831180610000198$
        # - The Green Hoods are a militia group founded by the legendary archer, Haster. The current commander is a firebrand named Oska. She's the fifth leader in the group's history, and some might say its greatest. If you want to meet her, you'll need to go to $map:02000076$.
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000199$
            # - Haven't you noticed? Petty crimes like theft and pickpocketing have skyrocketed since the earthquake. The guards are so busy trying to restore order that they can't keep eyes on everyone.
            return 12
        elif self.index == 1:
            # $script:0831180610000200$
            # - This couldn't be avoided. There's been such an enormous influx of people into the city from all over Maple World, there was bound to be more than a few bad apples. I just hope order will be restored soon.
            return -1
        return -1

    def __13(self, pick: int) -> int:
        # $script:0607163510001521$
        # - $MyPCName$, you remind me of an arrow that's just been loosed from its bow.
        if pick == 0:
            # $script:0607163510001522$
            # - How so?
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:0607163510001523$
        # - Because... you seem like somebody that never looks back, someone who simply moves forward in spite of uncertainty.
        if pick == 0:
            # $script:0607181410001556$
            # - Let's talk about something else.
            return 110
        return -1

    def __15(self, pick: int) -> int:
        if self.index == 0:
            # $script:0806014810001631$
            # - People <font color="#ffd200">suffer</font> when their daily activities are threatened by crime.
            #   We Green Hoods exist to ensure <font color="#ffd200">peace and safety</font>, even though that's a challenge without end.
            return 15
        elif self.index == 1:
            # $script:0806014810001632$
            # - What about you? Have you ever felt threatened by anything?
            #   <font color="#909090">(Memories of Brother $npcName:11001715[gender:0]$ and $npcName:11001706[gender:1]$ flash through your mind.)</font>
            if pick == 0:
                # $script:0806014810001633$
                # - I prefer not to think about such things.
                return 16
            return -1
        return -1

    def __16(self, pick: int) -> int:
        # $script:0806014810001634$
        # - Fighting crime is only a means to an end. Our <font color="#ffd200">true mission</font> is to protect this whole world from all threats, so that everyone can live without fear. We won't stop until we achieve that.
        if pick == 0:
            # $script:0806014810001635$
            # - Change the subject.
            return 120
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180610000201$
        # - Remember, you're not some aimless adventurer anymore. You're in the Green Hoods now, and that means you've got a mission and a creed. So, anything you'd like to ask?
        if pick == 0:
            # $script:0831180610000202$
            # - What should I do now?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000205$
            # - You're of no use to the Green Hoods without suitable gear. $npcName:11000004[gender:0]$ is a vendor of fine equipment, and probably has some great Archer gear for sale. After you're properly equipped, you should head beyond the city walls and dole out law to the lawless.
            return 21
        elif self.index == 1:
            # $script:0831180610000206$
            # - As you train, you'll ascend to new levels, and become ready to learn new skills. To see the skills you can learn, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
            return -1
        return -1

    def __22(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000207$
            # - Want to <font color="#ffd200">upgrade a skill</font>? Press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
            return 22
        elif self.index == 1:
            # $script:0831180610000208$
            # - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
            return -1
        return -1

    def __23(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000209$
            # - <font color="#ffd200">Upgrading skills</font> requires Crystals. 
            return 23
        elif self.index == 1:
            # $script:0831180610000210$
            # - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
            return 23
        elif self.index == 2:
            # $script:0831180610000211$
            # - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently. So you know, keep that in mind.
            return 23
        elif self.index == 3:
            # $script:0831180610000212$
            # - As for $itemPlural:40100022$... Well, you won't just find them lying around.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180610000213$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishing those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:0831180610000214$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0831180610000215$
            # - Tell me about the criminals.
            return 12
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180610000216$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishing those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:0831180610000217$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0831180610000218$
            # - Tell me about the criminals.
            return 12
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180610000219$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishing those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:0831180610000220$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0831180610000221$
            # - Tell me about the criminals.
            return 12
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180610000222$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishing those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:0831180610000223$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0831180610000224$
            # - Tell me about the criminals.
            return 12
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180610000225$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishing those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:0831180610000226$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0831180610000227$
            # - Tell me about the criminals.
            return 12
        return -1

    def __80(self, pick: int) -> int:
        # $script:0831180610000228$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishing those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:0831180610000229$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0831180610000230$
            # - Tell me about the criminals.
            return 12
        return -1

    def __90(self, pick: int) -> int:
        # $script:0831180610000231$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishing those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:0831180610000232$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0831180610000233$
            # - Tell me about the criminals.
            return 12
        return -1

    def __100(self, pick: int) -> int:
        # $script:1216124310001331$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishing those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:1216124310001332$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:1216124310001333$
            # - Tell me about the criminals.
            return 12
        return -1

    def __110(self, pick: int) -> int:
        # $script:0607163510001524$
        # - It's too bad you've decided not to join the Green Hoods. Still, we'd greatly appreciate any assistance you're willing to offer punishment to those who bear ill will for the people of these lands.
        if pick == 0:
            # $script:0607163510001525$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0607163510001526$
            # - Tell me about the criminals.
            return 12
        elif pick == 2:
            # $script:0607163510001527$
            # - Let's talk about something else.
            return 13
        return -1

    def __120(self, pick: int) -> int:
        # $script:0806014810001636$
        # - You don't have to be a member of the Green Hoods to help protect this world. If you come across wrongdoers, please see to it they're punished.
        if pick == 0:
            # $script:0806014810001637$
            # - Tell me about the Green Hoods.
            return 11
        elif pick == 1:
            # $script:0806014810001638$
            # - Tell me about the criminals.
            return 12
        elif pick == 2:
            # $script:0806014810001639$
            # - Talk to $npcName:11000045[gender:0]$ about a different subject.
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
            return Option.NEXT
        elif (self.state, self.index) == (15, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (16, 0):
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
