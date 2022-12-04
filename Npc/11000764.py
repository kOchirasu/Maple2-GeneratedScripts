""" 11000764: Vanilla """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180509000905$
        # - Do you need something?
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180509000906$
        # - Do you need something? Just a moment.
        if pick == 0:
            # $script:0831180509000907$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000908$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000909$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __2(self, pick: int) -> int:
        # $script:0831180509000910$
        # - I'll listen, but make it quick.
        if pick == 0:
            # $script:0831180509000911$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000912$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000913$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __3(self, pick: int) -> int:
        # $script:0831180509000914$
        # - Welcome. What do you need this time?
        if pick == 0:
            # $script:0831180509000915$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000916$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000917$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __4(self, pick: int) -> int:
        # $script:0831180509000918$
        # - Do you need something? Just a moment.
        if pick == 0:
            # $script:0831180509000919$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000920$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000921$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509000922$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, pick: int) -> int:
        # $script:0831180509000923$
        # - I'll listen, but make it quick.
        if pick == 0:
            # $script:0831180509000924$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000925$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000926$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509000927$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, pick: int) -> int:
        # $script:0831180509000928$
        # - Welcome. What do you need this time?
        if pick == 0:
            # $script:0831180509000929$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000930$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000931$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509000932$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, pick: int) -> int:
        # $script:0831180509000933$
        # - My paycheck? You want to pay me now?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509000934$
            # - Let me think about it some more.
            # TODO: goto 8040,8050,8060,9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000935$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000,8001,8010,8011,8901
            # TODO: gotoFail 8900,8910
            return 8900,8910
        return -1

    def __8000(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000936$
        # - Yes! I love you! You're the best! Thanks for paying me on time.
        #   <font color="#909090">(She winks at you.)</font>
        return -1

    def __8001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000937$
        # - Omigosh, you're paying me? Thanks!
        #   <font color="#909090">(She squeezes you in a big hug.)</font>
        return -1

    def __8010(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000938$
        # - A little late, but at least you didn't forget. I like it when people keep their promises.
        return -1

    def __8011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509000939$
        # - I knew it. You just couldn't let me go, could you, $OwnerName$? You had me tricked for a second there!
        return -1

    def __8020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000940$
        # - Hey, it's almost payday!
        return -1

    def __8021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000941$
        # - Payday is my favorite day!
        if pick == 0:
            # $script:0831180509000942$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000943$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000944$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509000945$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, pick: int) -> int:
        # $script:0831180509000946$
        # - You're still talking? All right. I'm still listening.
        if pick == 0:
            # $script:0831180509000947$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000948$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000949$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509000950$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, pick: int) -> int:
        # $script:0831180509000951$
        # - Mm? What do you want to talk about now?
        if pick == 0:
            # $script:0831180509000952$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000953$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000954$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509000955$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, pick: int) -> int:
        # $script:0831180509000956$
        # - I've got nothing more to say.
        if pick == 0:
            # $script:0831180509000957$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000958$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000959$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509000960$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8900(self, pick: int) -> int:
        # $script:0831180509000961$
        # - Why did you hire me if you can't afford me? I'm disappointed in you. I deserve better than this.
        return -1

    def __8901(self, pick: int) -> int:
        # $script:0831180509000962$
        # - I'm touched, but you've already paid me this month, and I don't offer extra services.
        #   <font color="#909090">(She winks.)</font>
        return -1

    def __8910(self, pick: int) -> int:
        # $script:0831180509000963$
        # - I've never been treated so awfully in my life! I'm really, really upset! I can't believe you!
        return -1

    def __8999(self, pick: int) -> int:
        # $script:0831180509000964$
        # - Huh? What's happening? Umm... I think you should try talking to me again later.
        return -1

    def __9001(self, pick: int) -> int:
        # $script:0831180509000965$
        # - Hey, you're $MaidPassedDay$ behind on my pay!
        if pick == 0:
            # $script:0831180509000966$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000967$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000968$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9002(self, pick: int) -> int:
        # $script:0831180509000969$
        # - Hmph, I don't talk to people who don't pay me on time.
        if pick == 0:
            # $script:0831180509000970$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000971$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000972$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9003(self, pick: int) -> int:
        # $script:0831180509000973$
        # - I'm not in the mood to talk. You know why, don't you?
        if pick == 0:
            # $script:0831180509000974$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000975$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000976$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9010(self, pick: int) -> int:
        # $script:0831180509000977$
        # - No pay, no service. Simple as that, hon.
        return -1

    def __9011(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000978$
        # - You know very well I don't want to chit chat with you! You're $MaidPassedDay$ behind on my paycheck!
        return -1

    def __9020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000979$
        # - Now is not the time to be checking out my profile...
        return -1

    def __9021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000980$
        # - Do you even know owe me money?
        if pick == 0:
            # $script:0831180509000981$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000982$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000983$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9040(self, pick: int) -> int:
        # $script:0831180509000984$
        # - Screw it. Do whatever you want.
        if pick == 0:
            # $script:0831180509000985$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509000986$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000987$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9030(self, pick: int) -> int:
        # $script:0831180509000988$
        # - Chat? Chaaaat? How about you pay me first?
        return -1

    def __9031(self, pick: int) -> int:
        # $script:0831180509000989$
        # - Oh, welcome home, $OwnerName$! What do you need? I'll do anything!! Like the good, unpaid slave that I am.
        #   <font color="#909090">(She gives a loud snort.)</font>
        return -1

    def __9032(self, pick: int) -> int:
        # $script:0831180509000990$
        # - Now that I know what you really think of me, I don't want to talk to you. Go away.
        return -1

    def __10(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000991$
        # - What? Oh, you want me to make you a necklace?
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000992$
        # - What do you think? I'm good, aren't I?
        return -1

    def __20(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000993$
        # - What? You're curious about me?
        return -1

    def __21(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000994$
        # - Don't think that you can probe the depths of my soul. Hmph.
        if pick == 0:
            # $script:0831180509000995$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509000996$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509000997$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __22(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509000998$
        # - Don't think that you can probe the depths of my soul. Hmph.
        if pick == 0:
            # $script:0831180509000999$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001000$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001001$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001002$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180509001003$
        # - You have questions for me? Just a moment.
        if pick == 0:
            # $script:0831180509001004$
            # - Did anything interesting happen?
            # TODO: goto 1000,1100,1200,1300,2000,2100,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509001005$
            # - (Stare at her.)
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509001006$
            # - (Tell her a joke.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001007$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180509001008$
        # - I'm kind of busy right now, but sure. Talk away.
        if pick == 0:
            # $script:0831180509001009$
            # - Did anything interesting happen?
            # TODO: goto 1000,1100,1200,1300,2000,2100,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509001010$
            # - (Stare at her.)
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509001011$
            # - (Tell her a joke.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001012$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180509001013$
        # - What is it? You can be a real pest sometimes, you know.
        if pick == 0:
            # $script:0831180509001014$
            # - Did anything interesting happen?
            # TODO: goto 1000,1100,1200,1300,2000,2100,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509001015$
            # - (Stare at her.)
            # TODO: goto 3000,3100,4000,4100,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509001016$
            # - (Tell her a joke.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509001017$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180509001018$
        # - You're still talking? All right. I'm still listening.
        if pick == 0:
            # $script:0831180509001019$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001020$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001021$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180509001022$
        # - Mm? What do you want to talk about now?
        if pick == 0:
            # $script:0831180509001023$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001024$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001025$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180509001026$
        # - I've got nothing more to say.
        if pick == 0:
            # $script:0831180509001027$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509001028$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509001029$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __1000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001030$
            # - I craved sweets something fierce today. You know those macaroons that are crispy on the outside and moist inside? That's what I love. My favorite flavor is rose.
            return 1000
        elif self.index == 1:
            # $script:0831180509001031$
            # - A famous bakery opened a branch in $map:02000001$. It's not cheap, but there's always a long line outside.
            return 1000
        elif self.index == 2:
            # $script:0831180509001032$
            # - So, while you were out, I went and— Ooops, I mean, look at this spot on the ground. I should go find the mop!
            return 1000
        elif self.index == 3:
            # $script:0831180509001033$
            # - M-macaroons? What? Never heard of them. No idea what they are!
            if pick == 0:
                # $script:0831180509001034$
                # - Slacking on the job, huh?
                # TODO: goto 1001,1002
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001035$
                # - I want to try a macaroon. Got any extra?
                # TODO: goto 1011,1012
                self.close()
                return -1
            return -1
        return -1

    def __1001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001036$
        # - Who said that? Do you have proof? Pfft, without proof, you still have to pay me!
        return -1

    def __1002(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001037$
        # - What? I finished everything you asked and more. Give me a break!
        return -1

    def __1011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001038$
        # - Huh? I had no idea you liked macaroons, $OwnerName$! Here, have some! I'm so glad I bought extra! Tasty, huh?
        return -1

    def __1012(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001039$
        # - Heeheehee, I guess I got caught. Here, try one. I waited hours for it!
        return -1

    def __1100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001040$
            # - Not a thing. Actually, one thing happened today: you kept interrupting me from my work!
            return 1100
        elif self.index == 1:
            # $script:0831180509001041$
            # - Something major and tragic happened today. I broke a nail! Do you know how much it costs to get my nails this cute?
            return 1100
        elif self.index == 2:
            # $script:0831180509001042$
            # - Aw, are you worried? Then you should know that I keep breathing in dust when I clean. Won't this stuff make me sick or something?
            return 1100
        elif self.index == 3:
            # $script:0831180509001043$
            # - I'm not complaining! I'm just not used to this type of thing.
            if pick == 0:
                # $script:0831180509001044$
                # - You do tend to complain a lot...
                # TODO: goto 1111,1112
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001045$
                # - Don't worry. I'm used to your complaining by now.
                # TODO: goto 1101,1102
                self.close()
                return -1
            return -1
        return -1

    def __1101(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001046$
        # - Um, are you deaf? I just said I'm not complaining! I'm just not used to working as a maid! Ugh, it upsets me that you think so little of me!
        return -1

    def __1102(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001047$
        # - Um, hello, I don't complain that much! You know what, I don't care what you think. You're really ticking me off!
        return -1

    def __1111(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001048$
        # - Awww, are you complaining about my complaining? That's kind of cute, $OwnerName$! You're like a grumpy old bear!
        return -1

    def __1112(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001049$
            # - <font color="#909090">(She's quiet for a while.)</font>
            return 1112
        elif self.index == 1:
            # $script:0831180509001050$
            # - Hmph!
            return 1112
        elif self.index == 2:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001051$
            # - <font color="#909090">(She bursts out laughing.)</font>
            #   This is why we get along so well. You're so cute when you act goofy, $OwnerName$.
            return -1
        return -1

    def __1200(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001052$
            # - <font color="#909090">(She pretends she can't hear you.)</font>
            return 1200
        elif self.index == 1:
            # $script:0831180509001053$
            # - Oh no! This is bad... Where did my o-ring band go? I can't make any jewelry without it!
            return 1200
        elif self.index == 2:
            # $script:0831180509001054$
            # - Oh, hi $OwnerName$. I'm sorry, I'm a little busy right now. I lost something.
            return 1200
        elif self.index == 3:
            # $script:0831180509001055$
            # - Can we talk later? I'm too distracted to focus right now.
            if pick == 0:
                # $script:0831180509001056$
                # - Oooh, what'd you lose? Is it important?
                # TODO: goto 1201,1202
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001057$
                # - I'll help you look for it.
                # TODO: goto 1211,1212
                self.close()
                return -1
            return -1
        return -1

    def __1201(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001058$
        # - $OwnerName$! I just said that I'm distracted! Will you leave me alone until I find it?
        return -1

    def __1202(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001059$
        # - It's something that I need to craft necklaces. You know what? That's not important right now! You're bothering me. Go away!
        return -1

    def __1211(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001060$
            # - <font color="#909090">(You get down on your hands and knees, searching the ground carefully. You find a small ring and hold it up triumphantly.)</font>
            return 1211
        elif self.index == 1:
            # $script:0831180509001061$
            # - You found it! Thank you, thank you, $OwnerName$!
            return 1211
        elif self.index == 2:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001062$
            # - This ring is used to hope and close the small rings used in necklaces. I can't make necklaces without it!
            return -1
        return -1

    def __1212(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001063$
            # - <font color="#909090">(You carefully scan the floor, diligently searching, and then...)</font>
            return 1212
        elif self.index == 1:
            # $script:0831180509001064$
            # - Thud!
            return 1212
        elif self.index == 2:
            # $script:0831180509001065$
            # - <font color="#909090">(You bump heads with $MaidName$!)</font>
            return 1212
        elif self.index == 3:
            # $script:0831180509001066$
            # - Ouch!
            #   <font color="#909090">(She rubs her head with her palm, surprised.)</font>
            return 1212
        elif self.index == 4:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001067$
            # - <font color="#909090">(Suddenly, she bursts into laughter.)</font>
            #   Oh, $OwnerName$! You don't have to search for it that hard! Thank you for helping me. I know it'll turn up soon!
            return -1
        return -1

    def __1300(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001068$
            # - I was strolling through $map:02000064$ today and ran into $npc:11000711[gender:1]$. Do you know what she told me? She said I had bags under my eyes! That I looked "tired"!
            return 1300
        elif self.index == 1:
            # $script:0831180509001069$
            # - She looks even more ragged than I do. No matter what she does, she— ah, never mind.
            if pick == 0:
                # $script:0831180509001070$
                # - What were you going to say?
                # TODO: goto 1301,1302
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509001071$
                # - You're always so full of life and energy. Not tired at all.
                # TODO: goto 1311,1312
                self.close()
                return -1
            return -1
        return -1

    def __1301(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001072$
        # - Forget it. It was unkind. I never thought you were into mean gossip, $OwnerName$. I don't think that's a good look on you.
        return -1

    def __1302(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001073$
        # - Why do you care? Is it because it's about $npc:11000711[gender:1]$? Are you a fan of hers? Hmph!
        return -1

    def __1311(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001074$
        # - Aw, thanks! I work hard to be that way, so thank you for noticing!
        return -1

    def __1312(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509001075$
        # - Awww, $OwnerName$. Are you trying to sweet talk me? That's totally unlike you!
        return -1

    def __2000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001076$
            # - I'm very busy at the moment. Please do not disturb me.
            return 2000
        elif self.index == 1:
            # $script:0831180509001077$
            # - ...
            return 2000
        elif self.index == 2:
            # $script:0831180509001078$
            # - ...Are you mad? I'm sorry, but I really don't have time for you right now.
            return -1
        return -1

    def __2100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001079$
            # - I wish something amazing would happen. The days get so boring.
            return 2100
        elif self.index == 1:
            # $script:0831180509001080$
            # - Listening to $npc:11000406[gender:0]$ singing usually helps, but not today. I'm so bored.
            return -1
        return -1

    def __3000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001081$
            # - Mm... Mm? Why are you staring at me? Please... stop...
            return 3000
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001082$
            # - <font color="#909090">($MaidName$'s cheeks are turning red.)</font>
            #   Oh, stop. You're making me blush!
            return -1
        return -1

    def __3100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001083$
            # - Stop it, $OwnerName$! You're doing it again? Are you really that helpless to resist my good looks?
            return 3100
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509001084$
            # - Hey, $OwnerName$, did you know your eyes sparkle when you stare at me?
            return -1
        return -1

    def __4000(self, pick: int) -> int:
        # $script:0831180509001085$
        # - Stop staring. Your puppy eyes lost their charm long ago. Come now, no need to pout.
        return -1

    def __4100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001086$
            # - Fine. Let's see who can go the longest without blinking. Ready, set, go!
            return 4100
        elif self.index == 1:
            # $script:0831180509001087$
            # - Forget it. I'm not in the mood, so stop staring at me!
            return -1
        return -1

    def __5000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001088$
            # - Ugh, why would you tell such an old joke? Nobody has laughed at that joke for years!
            return 5000
        elif self.index == 1:
            # $script:0831180509001089$
            # - This explains why you have so few friends, $OwnerName$. Tsk.
            return 5000
        elif self.index == 2:
            # $script:0831180509001090$
            # - I'll laugh to be nice. Haha. There.
            return -1
        return -1

    def __5100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001091$
            # - Please stop with the lame jokes. I'll tell you some that are actually funny.
            return 5100
        elif self.index == 1:
            # $script:0831180509001092$
            # - First up: How do you get a tissue to dance?
            return 5100
        elif self.index == 2:
            # $script:0831180509001093$
            # - You put a little boogie in it! Hahaha, isn't that hilarious?
            return 5100
        elif self.index == 3:
            # $script:0831180509001094$
            # - Next up: What did the zero say to the eight?
            return 5100
        elif self.index == 4:
            # $script:0831180509001095$
            # - Stumped? Then I'll tell you: Nice belt! Hahaha, get it?
            return 5100
        elif self.index == 5:
            # $script:0831180509001096$
            # - Here's the last one, and it's a stumper. Don't be mad if you can't figure it out. Here goes: Why did the tomato blush?
            return 5100
        elif self.index == 6:
            # $script:0831180509001097$
            # - You don't know, do you? Hehehe, the answer is: Because he saw the salad dressing!
            return 5100
        elif self.index == 7:
            # $script:0831180509001098$
            # - Now those are some funny jokes. Don't tell me any more jokes unless they're funnier that those ones!
            return -1
        return -1

    def __6000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001099$
            # - <font color="#909090">($MaidName$ looks at you mournfully.)</font>
            return 6000
        elif self.index == 1:
            # $script:0831180509001100$
            # - It's not you, $OwnerName$. I'm just really not in the mood for jokes right now.
            return 6000
        elif self.index == 2:
            # $script:0831180509001101$
            # - I was thinking of my sister. She's the one who taught me how to make jewelry.
            return 6000
        elif self.index == 3:
            # $script:0831180509001102$
            # - But I haven't heard from her in a long time. I don't even know where she is. Whenever I think of her, I get a pang in my heart so sharp I want to cry.
            return 6000
        elif self.index == 4:
            # $script:0831180509001103$
            # - I'm sorry. I don't know why I'm telling you this. Forget I said anything, okay?
            return 6000
        elif self.index == 5:
            # $script:0831180509001104$
            # - <font color="#909090">(You see $MaidName$'s eyes twinkle.)</font>
            return -1
        return -1

    def __7000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509001105$
            # - Hah! Hah! Hah! That's the funniest joke I've ever heard in my life! You're so hilarious, $OwnerName$!
            return 7000
        elif self.index == 1:
            # $script:0831180509001106$
            # - ...Not. Get a clue, $OwnerName$!
            return 7000
        elif self.index == 2:
            # $script:0831180509001107$
            # - How many times do I have to tell you? Stop telling lame jokes or you'll lose the few friends you have left!
            return 7000
        elif self.index == 3:
            # $script:0831180509001108$
            # - If you're reading lame joke books, why don't you go out and do something productive with your life? Like buying me treats or collecting necklace materials for me? Or helping the needy or something?
            return 7000
        elif self.index == 4:
            # $script:0831180509001109$
            # - Please just— Yikes. Um, I just realized I'm nagging at you like you're a friend. I'm sorry if I crossed a line, $OwnerName$. I just want what's best for you. You know that, right?
            return -1
        return -1

    def __100(self, pick: int) -> int:
        # $script:0831180509001110$
        # - Who are you? You can't just barge in here! Did you come to see me? Still, that doesn't make this okay!
        if pick == 0:
            # $script:0831180509001111$
            # - I'm here to see your master.
            # TODO: goto 101,102
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509001112$
            # - Oh, I don't need anything.
            # TODO: goto 103,104
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509001113$
            # - I came to see you.
            # TODO: goto 105,106
            self.close()
            return -1
        return -1

    def __101(self, pick: int) -> int:
        # $script:0831180509001114$
        # - Oh, you're a friend of $OwnerName$? Well, make yourself at home, and try not to bother me.
        return -1

    def __102(self, pick: int) -> int:
        # $script:0831180509001115$
        # - Are you for real? And here I thought $OwnerName$ had no friends! This is amazing!!
        return -1

    def __103(self, pick: int) -> int:
        # $script:0831180509001116$
        # - Well, if you have no business here, you'd better leave. I just mopped, and I don't need the floor getting all muddy again.
        return -1

    def __104(self, pick: int) -> int:
        # $script:0831180509001117$
        # - Suuuuure. Just be honest and say you're here to talk to me. It happens all the time. I'm used to it, really.
        return -1

    def __105(self, pick: int) -> int:
        # $script:0831180509001118$
        # - I don't think we've met. Are you a member of my fan club? I know you want to see me, but you shouldn't bother me at work, you know?
        return -1

    def __106(self, pick: int) -> int:
        # $script:0831180509001119$
        # - I'm too popular for my own good. Not a day goes by without someone wanting my attention. So what do you want? My autograph?
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (1, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (2, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (3, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (4, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (5, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (6, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8000, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8001, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8010, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8011, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8020, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8021, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8040, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8050, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8060, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (8900, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8901, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8910, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (8999, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9001, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9002, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9003, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9010, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9011, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9020, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9021, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9040, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (9030, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9031, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (9032, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (10, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (11, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (20, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (21, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (22, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (31, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (32, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (1000, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1001, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1002, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1011, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1012, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1100, 2):
            return Option.NEXT
        elif (self.state, self.index) == (1100, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1101, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1102, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1111, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1112, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1112, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1112, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (1200, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1200, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1200, 2):
            return Option.NEXT
        elif (self.state, self.index) == (1200, 3):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1201, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1202, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1211, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1211, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1211, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (1212, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1212, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1212, 2):
            return Option.NEXT
        elif (self.state, self.index) == (1212, 3):
            return Option.NEXT
        elif (self.state, self.index) == (1212, 4):
            return Option.CLOSE
        elif (self.state, self.index) == (1300, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1300, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1301, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1302, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1311, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1312, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (2000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (2000, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (2100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2100, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (3000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (3000, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (3100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (3100, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (4000, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (4100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (4100, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (5000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (5000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (5000, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (5100, 0):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 1):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 2):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 3):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 4):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 5):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 6):
            return Option.NEXT
        elif (self.state, self.index) == (5100, 7):
            return Option.CLOSE
        elif (self.state, self.index) == (6000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 3):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 4):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 5):
            return Option.CLOSE
        elif (self.state, self.index) == (7000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 3):
            return Option.NEXT
        elif (self.state, self.index) == (7000, 4):
            return Option.CLOSE
        elif (self.state, self.index) == (100, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (101, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (102, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (103, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (104, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (105, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (106, 0):
            return Option.CLOSE
        return Option.NONE
