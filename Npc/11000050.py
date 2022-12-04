""" 11000050: Char """
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
        # $script:0831180610000286$
        # - What brings you here?
        return None # TODO

    def __1(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000287$
            # - Justice is just an concept whose meaning no one can even agree on, so how important could it really be? Live free! Laws are for sheep. You've gotta take what you want, that's just the way the world works.
            return 1
        elif self.index == 1:
            # functionID=1 
            # $script:0831180610000288$
            # - If you wanna win, you've gotta be strong. I can teach you how to be strong.
            return None # TODO
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0831180610000289$
        # - Justice is just an concept whose meaning no one can even agree on, so how important could it really be? Live free! Laws are for sheep. I can show you how to get what you want.
        if pick == 0:
            # $script:0831180610000290$
            # - How can we live free?
            return 11
        elif pick == 1:
            # $script:0831180610000291$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __11(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000292$
            # - Are you serious? Have you really been so brainwashed by society that you don't know what it is anymore? 
            return 11
        elif self.index == 1:
            # $script:0831180610000293$
            # - Do what you want and take what you want. That's what it means to be free. If you want it, all you need is the strength to take it.
            return 11
        elif self.index == 2:
            # $script:0831180610000294$
            # - Justice? Order? Hah! They're for sheep who can't hack it in the wild! If you want to make it in this world you've got to learn how it <i>really</i> works. The only path in life is the one you carve for yourself. 
            return -1
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180610000295$
            # - It's simple be a winner. This world is ruled by competition, it's eat or be eaten. Only the best win, so you've gotta try and make sure that's you.
            return 12
        elif self.index == 1:
            # $script:0831180610000296$
            # - But things don't always go the way you want. You have to know how to turn the tables on your enemy, by any means necessary.
            return 12
        elif self.index == 2:
            # $script:0831180610000297$
            # - We Thieves are the masters of anything-goes. We can move on our enemies in the blink of an eye, and we've got no problem with poison-coated knives. We do what we have to, and if someone has something we want, we take it. It's simple.
            return 12
        elif self.index == 3:
            # $script:0831180610000298$
            # - There's no such thing as right and wrong when it comes to winning. There's only you, or them.
            return -1
        return -1

    def __13(self, pick: int) -> int:
        # $script:0607163510001537$
        # - Stop bothering me. The only people worth talking to are Thieves, and you're obviously not—wait! You... You're...
        if pick == 0:
            # $script:0607163510001538$
            # - You know me?
            return 14
        return -1

    def __14(self, pick: int) -> int:
        # $script:0607163510001539$
        # - Of course! You're the Gray Wolf! Everyone in the back alleys of $map:02000100$ knows who you are. I didn't think you'd ever find your way onto the world stage. What made you change your mind?
        if pick == 0:
            # $script:0607163510001540$
            # - You've got me mistaken for someone else.
            return 15
        return -1

    def __15(self, pick: int) -> int:
        # $script:0607163510001541$
        # - Hm... You're a bad liar. Your eyes give you away. But still, it's interesting to know that major players like you have come out of hiding.
        if pick == 0:
            # $script:0607181410001558$
            # - Let's talk about something else.
            return 110
        return -1

    def __16(self, pick: int) -> int:
        # $script:0806014810001653$
        # - Blah, blah, blah. You're more talkative than you look.
        #   Why are you babbling on like this? Curious about something?
        if pick == 0:
            # $script:0806014810001654$
            # - Do you know who I am?
            return 17
        return -1

    def __17(self, pick: int) -> int:
        # $script:0806014810001655$
        # - What? No. How would I know that? You some sort of celebrity? No, I didn't think so. The only way I could know who you are is if you were from $map:02000100$. Trust me, I know everyone from that place.
        if pick == 0:
            # $script:0806014810001656$
            # - How do you know everyone from there?
            return 18
        return -1

    def __18(self, pick: int) -> int:
        # $script:0806014810001657$
        # - Clearly, <i>you</i> should be asking who <i>I</i> am. I'm all over the back alleys of $map:02000100$. I know everything that happens there.
        if pick == 0:
            # $script:0806014810001658$
            # - Well, let's hear what you know, then!
            return 19
        return -1

    def __19(self, pick: int) -> int:
        if self.index == 0:
            # $script:0806014810001659$
            # - Right now, the talk of the town is the Gray Wolf, who decided to leave the shadows of society and duke it out with the Blackstars. Word is that the Gray Wolf singlehandedly razed the Blackstar stronghold. 
            return 19
        elif self.index == 1:
            # $script:0806014810001660$
            # - But that's not even the most interesting part. What's really amazing is the Gray Wolf took on the champion of $map:63000020$! Everyone knows the Champ can't be beaten, but the Gray Wolf went for it anyway! Dumb decision, really. The Warrior wiped the floor with them. There's a reason he's called the Monster, you know.
            if pick == 0:
                # $script:0806014810001661$
                # - Is the Champ really that tough?
                return 24
            return -1
        return -1

    def __24(self, pick: int) -> int:
        # $script:0806014810001662$
        # - Wow, you really don't know?
        #   He's a champion who successfully defended his title 47 times out of 48 matches. And the one time he didn't win, it was a tie. For the 47 victories, he brought them all down with a single blow, if you can believe it.
        if pick == 0:
            # $script:0806014810001663$
            # - What happened with the tie?
            return 25
        return -1

    def __25(self, pick: int) -> int:
        # $script:0806014810001664$
        # - Oh, it was amazing! The Warrior couldn't land a blow, no matter how hard he tried, and neither could his opponent. They just kept trying until both were exhausted, and it was really tense to watch. Finally, at the end, they were both heaving with fatigue, barely able to stand. Without a word, the challenger turned and stumbled away.
        if pick == 0:
            # $script:0806014810001665$
            # - Tell me about the challenger.
            return 26
        return -1

    def __26(self, pick: int) -> int:
        if self.index == 0:
            # $script:0806014810001666$
            # - I don't know. No one does! See, as if it weren't dramatic enough, nobody could find out anything, except that the challenger was a were-eagle known to some people in $map:63000020$, who of course would admit nothing.
            return 26
        elif self.index == 1:
            # $script:0806014810001667$
            # - And why would they? That would be admitting that the Champ isn't invincible.
            if pick == 0:
                # $script:0806014810001668$
                # - Change the subject.
                return 120
            return -1
        return -1

    def __20(self, pick: int) -> int:
        # functionID=70 
        # $script:0831180610000299$
        # - Congratulations, $MyPCName$, and welcome to the seedy underbelly of society. Now it's time you learned our ways, from surprise attacks to poisoned blades.
        if pick == 0:
            # $script:0831180610000300$
            # - What should I do now?
            return 21
        return -1

    def __21(self, pick: int) -> int:
        if self.index == 0:
            # functionID=60 
            # $script:0831180610000303$
            # - To take down your enemies you've gotta be fast and precise. For that, you'll need a sharp dagger. $npc:11000004[gender:0]$ should have all kinds of Thief gear. So go get yourself a shiny new blade and use it to carve your own path in life. 
            return 21
        elif self.index == 1:
            # functionID=60 
            # $script:0831180610000304$
            # - Stab enough things, and eventually you'll reach a new level, and that means you get to learn new skills. To see the <font color="#ffd200">skills you can learn</font>, press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>.
            return -1
        return -1

    def __22(self, pick: int) -> int:
        if self.index == 0:
            # functionID=60 
            # $script:0831180610000305$
            # - When you're ready to <font color="#ffd200">upgrade a skill</font>, just press <font color="#ffd200">K</font> to open the <font color="#ffd200">Skill window</font>, then press the plus sign next to the skill you'd like to improve. 
            return 22
        elif self.index == 1:
            # functionID=60 
            # $script:0831180610000306$
            # - Upgrading skills requires various types of crystals. One type, $itemPlural:40100001$, are available for purchase from supply merchant $npcName:11000010[gender:1]$ here in $map:02000001$.
            return -1
        return -1

    def __23(self, pick: int) -> int:
        if self.index == 0:
            # functionID=60 
            # $script:0831180610000307$
            # - <font color="#ffd200">Upgrading skills</font> requires <font color="#ffd200">Crystals</font>. 
            return 23
        elif self.index == 1:
            # functionID=60 
            # $script:0831180610000308$
            # - $itemPlural:40100001$ are what remains after polishing rough crystals, and they're distributed throughout Maple World by $map:02000051$. You can easily find them by talking to supply merchants in big cities.
            return 23
        elif self.index == 2:
            # functionID=60 
            # $script:0831180610000309$
            # - Of course, some materials are rarer than others, in particular the Red, Blue, and Green Crystals. They possess so much power that they are unstable, and only <font color="#ffd200">Elite</font> or <font color="#ffd200">Boss</font> enemies will drop them, and very infrequently. So yeah, getting hold of them is no easy feat.
            return 23
        elif self.index == 3:
            # functionID=60 
            # $script:0831180610000310$
            # - And as for $itemPlural:40100022$—well, you can figure that out on your own time.
            return -1
        return -1

    def __30(self, pick: int) -> int:
        # functionID=10 
        # $script:0831180610000311$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Knight here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000312$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000313$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __40(self, pick: int) -> int:
        # functionID=20 
        # $script:0831180610000314$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Berserker here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000315$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000316$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __50(self, pick: int) -> int:
        # functionID=30 
        # $script:0831180610000317$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Wizard here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000318$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000319$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __60(self, pick: int) -> int:
        # functionID=40 
        # $script:0831180610000320$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Priest here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000321$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000322$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __70(self, pick: int) -> int:
        # functionID=50 
        # $script:0831180610000323$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to an Archer here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000324$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000325$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __80(self, pick: int) -> int:
        # functionID=60 
        # $script:0831180610000326$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Heavy Gunner here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:0831180610000327$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000328$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __90(self, pick: int) -> int:
        # functionID=80 
        # $script:0831180610000329$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to an Assassin here. Sure you've crossed some lines, but you're still just a cog in the machine. Just go on your merry way.
        if pick == 0:
            # $script:0831180610000330$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0831180610000331$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __100(self, pick: int) -> int:
        # functionID=90 
        # $script:1216124310001337$
        # - If you were a little more open-minded, I could teach you how to get anything you want. But I'm talking to a Runeblade here. You wouldn't know what freedom is. So just go on your merry way.
        if pick == 0:
            # $script:1216124310001338$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:1216124310001339$
            # - Oh yeah? How can I get anything I want?
            return 12
        return -1

    def __110(self, pick: int) -> int:
        # functionID=100 
        # $script:0607163510001542$
        # - $MyPCName$, I can tell you how to get what you want. Oh, wait... I see now you're not a Thief. Well, then you wouldn't even know what freedom is. Just go along your merry way.
        if pick == 0:
            # $script:0607163510001543$
            # - Okay, try me. What's freedom?
            return 11
        elif pick == 1:
            # $script:0607163510001544$
            # - Oh yeah? How can I get anything I want?
            return 12
        elif pick == 2:
            # $script:0607163510001545$
            # - I don't want to talk about this anymore.
            return 13
        return -1

    def __120(self, pick: int) -> int:
        # functionID=110 
        # $script:0806014810001669$
        # - $MyPCName$, I can tell you <font color="#ffd200">how to get what you want</font>.
        #   Oh, wait... I see now you're not a Thief. Well, then you wouldn't even know what <font color="#ffd200">freedom</font> is. Just go along your merry way.
        if pick == 0:
            # $script:0806014810001670$
            # - What is freedom?
            return 11
        elif pick == 1:
            # $script:0806014810001671$
            # - Oh yeah? How can I get anything I want?
            return 12
        elif pick == 2:
            # $script:0806014810001672$
            # - Talk to $npcName:11000050[gender:0]$ about a different subject.
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
            return Option.NEXT
        elif (self.state, self.index) == (11, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.NEXT
        elif (self.state, self.index) == (12, 2):
            return Option.NEXT
        elif (self.state, self.index) == (12, 3):
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
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (19, 0):
            return Option.NEXT
        elif (self.state, self.index) == (19, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (24, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (25, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (26, 0):
            return Option.NEXT
        elif (self.state, self.index) == (26, 1):
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
