""" 11000041: Rekk """
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
        # $script:0831180610000062$
        # - Do you want to become a true warrior?
        return None # TODO

    def __1(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000063$
            # - Argh, this place is so boring, it's driving me crazy! If it weren't for the War Chief's order, I would be cracking skulls on Vayar Mountain and having a blast! Hey, you look pretty tough. How are you in a fight?
            return 1
        elif self.index == 1:
            # functionID=1 
            # $script:0831180610000064$
            # - With a greatsword in our hands, we're fearless in battle. We can be overzealous sometimes, but that's inevitable when you've got our passion for fighting. So, how'd you like to swear fealty to the War Chief and walk the path of the Berserker?
            return None # TODO
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610000065$
        # - Argh, this place is so boring, it's driving me crazy! If it weren't for the War Chief's order, I would be cracking skulls on Vayar Mountain and having a blast! Hey, you look pretty tough. How are you in a fight?
        if pick == 0:
            # $script:0831180610000066$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0831180610000067$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000068$
            # - We wouldn't be able to survive the sunbaked steppes of $map:02000051$ if it weren't for our War Chief. He's a great warrior and greater leader. Our trust in him is unwavering.
            return 11
        elif self.index == 1:
            # $script:0831180610000069$
            # - If you want to meet him, then go to $map:02000051$'s western plateau. But first, you'll have to get approval from his son and our vice chief, $npc:11000009[gender:0]$.
            return 11
        elif self.index == 2:
            # $script:0831180610000070$
            # - Oh, and when you see him, just be yourself and be honest. He can tell instantly when you're hiding something.
            return -1
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000071$
            # - You must not get around much if you haven't heard of Vayar Mountain. It's south of $map:02000051$. We named it after the giant golems that lurk inside.
            return 12
        elif self.index == 1:
            # $script:0831180610000072$
            # - The golems, or Vayars, were created by the ancients to protect their sanctum. That was centuries ago, and the ancients are long gone. But the Vayars remain, protecting the mountain from any adventurers brave or foolish enough to enter.
            return 12
        elif self.index == 2:
            # $script:0831180610000073$
            # - Speaking of which, I've heard rumors that someone evaded the 
            #   Vayars' detection and snuck into the mountain. What was their name? I can't remember...
            return -1
        return -1

    def __20(self, pick: int) -> int:
        # $script:0831180610000074$
        # - Sometimes in the heat of battle, I achieve inhuman feats simply because, in my rage, I forget fear and all my weaknesses. I wouldn't count that as a blessing, though... Some things are worth forgetting, but you must never forget who you are. Now, was there something you wanted to ask me?
        if pick == 0:
            # $script:0831180610000075$
            # - What should I do now?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000078$
            # - First, arm yourself to the teeth. $npc:11000004[gender:0]$ is a merchant of fine equipment, and probably has some great Berserker equipment for sale. Gear up and head out to battle!
            return 21
        elif self.index == 1:
            # $script:0831180610000079$
            # - Crush all the foes who stand before you, and you will soon grow to new levels. Then you will find yourself ready to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
            return -1
        return -1

    def __22(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000080$
            # - Want to <font color="#ffd200">upgrade a skill</font>? Press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
            return 22
        elif self.index == 1:
            # $script:0831180610000081$
            # - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
            return -1
        return -1

    def __23(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000082$
            # - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>. 
            return 23
        elif self.index == 1:
            # $script:0831180610000083$
            # - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
            return 23
        elif self.index == 2:
            # $script:0831180610000084$
            # - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently.
            return 23
        elif self.index == 3:
            # $script:0831180610000085$
            # - There's also $itemPlural:40100022$, but I don't think you're ready for those just yet.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180610000086$
        # - You've really chosen to become a Knight? I don't know what you'll accomplish waving a dinky sword like that around, but good luck surviving.
        if pick == 0:
            # $script:0831180610000087$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0831180610000088$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180610000089$
        # - You've really chosen to become a Knight? I don't really see how shouting gibberish from musty old tomes is going to keep you alive in battle, but I won't tell you how to live what's left of your life.
        if pick == 0:
            # $script:0831180610000090$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0831180610000091$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180610000092$
        # - A priest? You've chosen to be a Priest? A fat lot of good prayer is going to do you against a horde of charging Koborcs.
        if pick == 0:
            # $script:0831180610000093$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0831180610000094$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180610000095$
        # - You've really chosen to become an Archer? Striking down hapless foes from a distance is great, until your quiver runs dry. When the enemy comes bearing down on you, you'll wish you'd gone with a blade.
        if pick == 0:
            # $script:0831180610000096$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0831180610000097$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __70(self, pick: int) -> int:
        # $script:0831180610000098$
        # - You've chosen to become a Heavy Gunner, of all things? Guns are a crutch of the cowardly. A true warrior faces their opponent head on. Don't look to me when that cannon jams in the heat of battle.
        if pick == 0:
            # $script:0831180610000099$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0831180610000100$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __80(self, pick: int) -> int:
        # $script:0831180610000101$
        # - You've chosen to become a Thief? Throwing your only weapons at the enemy seems like a foolhardy strategy, but who am I to stand in the way of a someone with a deathwish?
        if pick == 0:
            # $script:0831180610000102$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0831180610000103$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __90(self, pick: int) -> int:
        # $script:0831180610000104$
        # - You've chosen to become an Assassin? Skulking around in the shadows, hoping to strike without being seen... There's no honor in that.
        if pick == 0:
            # $script:0831180610000105$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0831180610000106$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __100(self, pick: int) -> int:
        # $script:1216124310001322$
        # - You've chosen to become a Runeblade? To split one's focus between two completely different arts in the midst of battle seems like a reckless strategy. Perhaps you'll prove me wrong by not dying.
        if pick == 0:
            # $script:1216124310001323$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:1216124310001324$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __110(self, pick: int) -> int:
        # $script:0607163510001501$
        # - I sense your fighting spirit is akin to the rage that fuels us Berserkers. A fire that burns within the soul and cannot be quenched! Some advice from one warrior to another: never let your anger get the better of you on the battlefield, or you might wind up dead.
        if pick == 0:
            # $script:0607163510001502$
            # - Tell me about the War Chief.
            return 11
        elif pick == 1:
            # $script:0607163510001503$
            # - Tell me about Vayar Mountain.
            return 12
        return -1

    def __120(self, pick: int) -> int:
        # $script:0806014810001598$
        # - The rage that fuels us Berserkers is a hot and roiling one that scorches the soul. And I can see it's just not in you. You're just like everyone else... you'll never know what it feels like to be truly alive.
        if pick == 0:
            # $script:0806014810001599$
            # - Tell me about the war chief.
            return 11
        elif pick == 1:
            # $script:0806014810001600$
            # - Tell me about Vayar Mountain.
            return 12
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
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.NEXT
        elif (self.state, self.index) == (12, 2):
            return Option.CLOSE
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
