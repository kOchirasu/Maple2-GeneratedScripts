""" 11000777: Cordelia """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return random.choice([1, 2, 3, 4, 5, 6, 9001, 9002, 9003, 100])

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0831180509002981$
        # - What is it, meow?
        return None # TODO

    def __1(self, pick: int) -> int:
        # $script:0831180509002982$
        # - Meow! Welcome home.
        if pick == 0:
            # $script:0831180509002983$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002984$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002985$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __2(self, pick: int) -> int:
        # $script:0831180509002986$
        # - Did you call me, meow?
        if pick == 0:
            # $script:0831180509002987$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002988$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002989$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __3(self, pick: int) -> int:
        # $script:0831180509002990$
        # - Meow? How long have you been standing there?
        if pick == 0:
            # $script:0831180509002991$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002992$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002993$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __4(self, pick: int) -> int:
        # $script:0831180509002994$
        # - Meow! Welcome home.
        if pick == 0:
            # $script:0831180509002995$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509002996$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509002997$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509002998$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __5(self, pick: int) -> int:
        # $script:0831180509002999$
        # - Did you call me, meow?
        if pick == 0:
            # $script:0831180509003000$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003001$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003002$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003003$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __6(self, pick: int) -> int:
        # $script:0831180509003004$
        # - Meow? How long have you been standing there?
        if pick == 0:
            # $script:0831180509003005$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003006$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003007$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003008$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __9(self, pick: int) -> int:
        # $script:0831180509003009$
        # - Are you going to give me those shiny blue things?
        #   <b>(Wage: $MaidSalary$ — Extends Contract Through: $MaidExtendDate$)</b>
        if pick == 0:
            # $script:0831180509003010$
            # - (Refuse to pay.)
            # TODO: goto 8040,8050,8060,9040
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003011$
            # - (Pay $MaidSalary$.)
            # TODO: goto 8000,8001,8010,8011,8901
            # TODO: gotoFail 8900,8910
            return 8900,8910
        return -1

    def __8000(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003012$
        # - I'll take it! So pretty, meow!
        return -1

    def __8001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003013$
        # - $npcName:11000708$ said it's important to trust my servant, but that doesn't happen overnight. Keep paying me early, and I'll grow to trust you.
        return -1

    def __8010(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003014$
        # - I'd like to think that you were too busy saving the world from utter catastrophe to pay me on time, meow. I'm glad you eventually remembered your priorities.
        return -1

    def __8011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003015$
        # - I was just thinking that perhaps I should fire you and search for a better servant, but it seems you've realized the error of your ways. I'll show you some grace... this time... 
        return -1

    def __8020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003016$
        # - $OwnerName$, our contract expires soon. Do I really have to remind you of things like this, meow?
        return -1

    def __8021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003017$
        # - You might be more work than you're worth...
        if pick == 0:
            # $script:0831180509003018$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003019$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003020$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003021$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8040(self, pick: int) -> int:
        # $script:0831180509003022$
        # - What is it, meow?
        if pick == 0:
            # $script:0831180509003023$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003024$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003025$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003026$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8050(self, pick: int) -> int:
        # $script:0831180509003027$
        # - $OwnerName$, what took so long? Servants shouldn't neglect their masters, meow.
        if pick == 0:
            # $script:0831180509003028$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003029$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003030$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003031$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8060(self, pick: int) -> int:
        # $script:0831180509003032$
        # - Did you call me, meow?
        if pick == 0:
            # $script:0831180509003033$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003034$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003035$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003036$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __8900(self, pick: int) -> int:
        # $script:0831180509003037$
        # - Don't you have any more of those shiny blue things? I feel so unmotivated if I don't get some once every month or so.
        return -1

    def __8901(self, pick: int) -> int:
        # $script:0831180509003038$
        # - Did you already give me your monthly tribute? You're as forgetful as $npcName:11000075[gender:1]$.
        return -1

    def __8910(self, pick: int) -> int:
        # $script:0831180509003039$
        # - Don't you have any more of those shiny blue things? I feel so unmotivated if I don't get some once every month or so.
        return -1

    def __8999(self, pick: int) -> int:
        # $script:0831180509003040$
        # - Meow... I'm sleepy... Let's do it later... Zzz... 
        return -1

    def __9001(self, pick: int) -> int:
        # $script:0831180509003041$
        # - I must... have more... of those shiny... blue... things!
        if pick == 0:
            # $script:0831180509003042$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003043$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003044$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9002(self, pick: int) -> int:
        # $script:0831180509003045$
        # - No longer interested in me? Hm! Bad servant! Bad!
        if pick == 0:
            # $script:0831180509003046$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003047$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003048$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9003(self, pick: int) -> int:
        # $script:0831180509003049$
        # - Haven't you forgotten something, meow?  
        if pick == 0:
            # $script:0831180509003050$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003051$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003052$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9010(self, pick: int) -> int:
        # $script:0831180509003053$
        # - I don't feel like it. Hey, if you give me some of those pretty blue things, I might change my mind.
        return -1

    def __9011(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003054$
        # - Mew...  I want to go back to $map:02000025$. I should've never left the castle, meow...
        return -1

    def __9020(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003055$
        # - I haven't eaten for$MaidPassedDay$! Must get more shiny blue thingies!
        return -1

    def __9021(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003056$
        # - Can't you see the circles under my eyes?
        if pick == 0:
            # $script:0831180509003057$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003058$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003059$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9040(self, pick: int) -> int:
        # $script:0831180509003060$
        # - You really are oblivious, aren't you?
        if pick == 0:
            # $script:0831180509003061$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        elif pick == 1:
            # $script:0831180509003062$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003063$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __9030(self, pick: int) -> int:
        # $script:0831180509003064$
        # - ...Meow...  
        #   <font color="#909090">(She peers at you for 3 seconds, and then turns around and moves away.)</font>
        return -1

    def __9031(self, pick: int) -> int:
        # $script:0831180509003065$
        # - I'm going to find myself another servant, meow.
        return -1

    def __9032(self, pick: int) -> int:
        # $script:0831180509003066$
        # - Meow.
        #   <font color="#909090">(She circles around you, rubs her face against your leg, and then softly walks away.)</font>
        return -1

    def __10(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003067$
        # - Want some shiny blue things, meow? Want me to go pick some up?
        return -1

    def __11(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003068$
        # - Finding shiny things is my favorite, meow.
        return -1

    def __20(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003069$
        # - Meow, are you curious about me?
        return -1

    def __21(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003070$
        # - Meow, you're no fun.
        if pick == 0:
            # $script:0831180509003071$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003072$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003073$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __22(self, pick: int) -> int:
        # functionID=1 
        # $script:0831180509003074$
        # - Meow, you're no fun.
        if pick == 0:
            # $script:0831180509003075$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003076$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003077$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003078$
            # - Don't I owe you money? (Pay salary of $MaidSalary$.)
            return 9
        return -1

    def __30(self, pick: int) -> int:
        # $script:0831180509003079$
        # - Cats can't talk... Is that what you think?
        if pick == 0:
            # $script:0831180509003080$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509003081$
            # - (Play with her.)
            # TODO: goto 3000,3100,4000,4100,4200,4300,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509003082$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003083$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __31(self, pick: int) -> int:
        # $script:0831180509003084$
        # - I'm bored, meow. Play with me.
        if pick == 0:
            # $script:0831180509003085$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509003086$
            # - (Play with her.)
            # TODO: goto 3000,3100,4000,4100,4200,4300,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509003087$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003088$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __32(self, pick: int) -> int:
        # $script:0831180509003089$
        # - I'm sleepy, meow...
        if pick == 0:
            # $script:0831180509003090$
            # - Anything interesting happen today?
            # TODO: goto 1000,1100,1200,1300,1400,1500,1600,2000,2100,2200,9011
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509003091$
            # - (Play with her.)
            # TODO: goto 3000,3100,4000,4100,4200,4300,9011
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509003092$
            # - (Ask your servant a personal question.)
            # TODO: goto 5000,5100,6000,7000,9011
            self.close()
            return -1
        elif pick == 3:
            # $script:0831180509003093$
            # - Back.
            # TODO: goto 8040,8050,8060,40,50,60,9040
            self.close()
            return -1
        return -1

    def __40(self, pick: int) -> int:
        # $script:0831180509003094$
        # - What is it, meow?
        if pick == 0:
            # $script:0831180509003095$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003096$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003097$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __50(self, pick: int) -> int:
        # $script:0831180509003098$
        # - $OwnerName$, what took so long? Servants shouldn't neglect their masters, meow.
        if pick == 0:
            # $script:0831180509003099$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003100$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003101$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0831180509003102$
        # - Did you call me, meow?
        if pick == 0:
            # $script:0831180509003103$
            # - I need you to craft something.
            # TODO: goto 10,9010
            # TODO: gotoFail 8999
            return 8999
        elif pick == 1:
            # $script:0831180509003104$
            # - I want to check your profile.
            # TODO: goto 20,8020,9020
            # TODO: gotoFail 8999
            return 8999
        elif pick == 2:
            # $script:0831180509003105$
            # - Let's chat!
            # TODO: goto 30,31,32,9030,9031,9032
            self.close()
            return -1
        return -1

    def __1000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003106$
            # - Take this food, meow. I went out for a stroll and picked it up next door. No one was home. It was sitting out on the kitchen counter waiting for me.
            return 1000
        elif self.index == 1:
            # $script:0831180509003107$
            # - I started eating it but then remembered you, $OwnerName$. You should be thankful. I don't always share.
            if pick == 0:
                # $script:0831180509003108$
                # - You stole this food!
                # TODO: goto 1001,1002
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509003109$
                # - Thank you.
                # TODO: goto 1011,1012
                self.close()
                return -1
            return -1
        return -1

    def __1001(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003110$
        # - Stolen? Do you forget who I am? Everything I see is rightfully mine. The minister never understood that...
        return -1

    def __1002(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003111$
        # - If that bothers you, why are you eating it? It's a little dirty because I had to drag it all this way, but you seem content enough.
        return -1

    def __1011(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003112$
        # - You're welcome, meow. I'll bring you something tomorrow, too.
        return -1

    def __1012(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003113$
        # - Of course. I take care of my minions, when the mood strikes. Tomorrow, I'll take my walk through the palace.
        return -1

    def __1100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003114$
            # - Whoop, this reminds me...
            return 1100
        elif self.index == 1:
            # $script:0831180509003115$
            # - We can snack together, meow. Go on, take some. Mm? You want to know where I get this?
            return 1100
        elif self.index == 2:
            # $script:0831180509003116$
            # - When you're not home, $OwnerName$, a girl stops by to play with me and give me treats. I wasn't hungry earlier, so I saved this for you.
            if pick == 0:
                # $script:0831180509003117$
                # - Girl? What girl?
                # TODO: goto 1111,1112
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509003118$
                # - You let a stranger into the house?!
                # TODO: goto 1101,1102
                self.close()
                return -1
            return -1
        return -1

    def __1101(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003119$
        # - Are you deaf, servant? She's not a stranger, she's my friend. Now go away for a while.
        return -1

    def __1102(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003120$
        # - Well, you weren't here to screen our guest. What do I hire you for anyway, servant?
        return -1

    def __1111(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003121$
        # - I never asked her name, meow. She's from Carimia Island, where she lives with grandpa. She works around here, though. She's cute, but not as cute as me!
        return -1

    def __1112(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003122$
            # - I'm not sure. I think she also lives with a servant, like I do. She seems lonely because her servant is rarely home, too.
            return 1112
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003123$
            # - She visits me when she's lonely, meow. Between you and me, I don't think she's much of a cook...
            return -1
        return -1

    def __1200(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003124$
            # - You've been looking a bit ragged, so I got this for you. You don't want to know where I got it.
            return 1200
        elif self.index == 1:
            # $script:0831180509003125$
            # - It's a health drink. It should perk you right up.
            if pick == 0:
                # $script:0831180509003126$
                # - No, no, you take it. I insist.
                # TODO: goto 1211,1212
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509003127$
                # - Where did you get it?
                # TODO: goto 1201,1202
                self.close()
                return -1
            return -1
        return -1

    def __1201(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003128$
        # - You're gonna regret asking... I nabbed it from $map:2000065$ while I was in $map:2000025$. The minister drinks it, so it's got to be good.
        return -1

    def __1202(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003129$
        # - I picked it up in $map:2000025$ $map:2000065$. Hey, my minions deserve the best.
        return -1

    def __1211(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003130$
        # - No thank you. I had a sip and did not enjoy the flavor. But it's good for your health, so you should drink every last drop.
        return -1

    def __1212(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003131$
            # - I'm touched, meow. Servant, I had no idea you cared so much!
            return 1212
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003132$
            # - But you should take it. You're the peon who pays the rent, so I need you in good health.
            return -1
        return -1

    def __1300(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003133$
            # - Meow. $OwnerName$, I've got something to tell you.
            return 1300
        elif self.index == 1:
            # $script:0831180509003134$
            # - You must be hungry. Eat this, meow. I must be the only cat who worries about her minions this much.
            return 1300
        elif self.index == 2:
            # $script:0831180509003135$
            # - Meow? Why are you looking at me like that?
            if pick == 0:
                # $script:0831180509003136$
                # - Did you cook this?
                # TODO: goto 1301,1302
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509003137$
                # - I'm just so touched!
                # TODO: goto 1311,1312
                self.close()
                return -1
            return -1
        return -1

    def __1301(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003138$
        # - Don't be silly, meow. Have you ever seen a cat cooking?
        return -1

    def __1302(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003139$
        # - I didn't cook it, meow. I picked it up next door.
        return -1

    def __1311(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003140$
        # - Aww, you're easy. I'll bring stuff more often, then.
        return -1

    def __1312(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003141$
        # - It's just leftovers. Don't read too much into it. 
        return -1

    def __1400(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003142$
            # - Look at this, meow. I found it under the bed while playing with some ants.
            return 1400
        elif self.index == 1:
            # $script:0831180509003143$
            # - Weren't you looking for this, meow?
            if pick == 0:
                # $script:0831180509003144$
                # - Ants?! Where?!
                # TODO: goto 1411,1412
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509003145$
                # - Thank you.
                # TODO: goto 1401,1402
                self.close()
                return -1
            return -1
        return -1

    def __1401(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003146$
        # - Don't make it a habit. It's your job to look after me, not the other way around.
        return -1

    def __1402(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003147$
        # - You're welcome. There are other things under the bed, but I forbid you to look.
        return -1

    def __1411(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003148$
        # - We were enjoying our time together when they suddenly stopped moving. Maybe they were sleepy after being tossed into the air and stomped on. Should I be worried about them?
        return -1

    def __1412(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003149$
        # - They went back home, meow. It's all right. Their family is so big that I see them everywhere.
        return -1

    def __1500(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003150$
            # - Look at this, meow! It looks like new, doesn't it? I think we can use it!
            return 1500
        elif self.index == 1:
            # $script:0831180509003151$
            # - Want to know where I got it? There's a girl who drops by when you're not home. She left it here as a gift, looking totally bummed out about it.
            if pick == 0:
                # $script:0831180509003152$
                # - I know just the spot for it!
                # TODO: goto 1501,1502
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509003153$
                # - Girl? What girl?
                # TODO: goto 1511,1512
                self.close()
                return -1
            return -1
        return -1

    def __1501(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003154$
        # - Where? Where? Oooh, I can't wait to see!
        return -1

    def __1502(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003155$
        # - That's right. It's ours now! Let's do what we want with it!
        return -1

    def __1511(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003156$
            # - She lives with her servant, just like I do. She's pretty cute, even with her glasses. I don't know her name, though.
            return 1511
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003157$
            # - Her servant must have been displeased she picked something up from the street. How rude!
            return -1
        return -1

    def __1512(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003158$
            # - She lives in the neighborhood. I only knows that she's from an island, meow.
            return 1512
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003159$
            # - She looked upset. I think her servant yelled at her. She said the servant called the item trash! I told her she should fire her servant, but then she started crying. 
            return -1
        return -1

    def __1600(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003160$
            # - I was taking a stroll when I found something shiny, so I brought it home with me. I almost didn't see it because it was covered in dirt, meow.
            return 1600
        elif self.index == 1:
            # $script:0831180509003161$
            # - It doesn't look like it's good for anything, but you can have it if you want, meow.
            if pick == 0:
                # $script:0831180509003162$
                # - Thanks! I'd love more if you find more!
                # TODO: goto 1611,1612
                self.close()
                return -1
            elif pick == 1:
                # $script:0831180509003163$
                # - More! I must have more!
                # TODO: goto 1601,1602
                self.close()
                return -1
            return -1
        return -1

    def __1601(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003164$
        # - That's all I've got. Why are your eyes gleaming like a crazy person's?
        return -1

    def __1602(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003165$
        # - I don't have any more. But if it's that great, I'm going to keep the next one I find.
        return -1

    def __1611(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003166$
        # - Meow? You like it? It's not even edible... But I can bring you more next time.
        return -1

    def __1612(self, pick: int) -> int:
        # functionID=1 openTalkReward=True 
        # $script:0831180509003167$
        # - $map:2000025$ is full of shiny things, meow. I'll bring more if I go there next time.
        return -1

    def __2000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003168$
            # - Nothing at all, meow. What could possibly happen in such a tiny house?
            return 2000
        elif self.index == 1:
            # $script:0831180509003169$
            # - Unless you're interested in the cockroaches. I played with them all day.
            return 2000
        elif self.index == 2:
            # $script:0831180509003170$
            # - But they suddenly stopped playing with me! If they didn't like me pulling off their legs, they should've said so.
            return -1
        return -1

    def __2100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003171$
            # - Strange people keep barging into the house. Do you owe them money or something?
            return 2100
        elif self.index == 1:
            # $script:0831180509003172$
            # - It's okay if you do. I've got it under control. I just look at them with large sparkly eyes, and they leave with a dreamy look on their faces.
            return -1
        return -1

    def __2200(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003173$
            # - Yes, I was bored! So, so bored! It's not nice to leave me alone for so long!
            return 2200
        elif self.index == 1:
            # $script:0831180509003174$
            # - A friend visited today. $npcName:11000367$ from Barrota Harbor.
            return 2200
        elif self.index == 2:
            # $script:0831180509003175$
            # - He brought his girlfriend, and they were all lovey dovey. Say, $OwnerName$, do you have someone you love? Why don't you introduce me sometime?
            return -1
        return -1

    def __3000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003176$
            # - ...! Did you see that? Look!! A red dot! It's moving there... and there... and back there...!
            return 3000
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003177$
            # - I'm gonna catch it! Catch it! Yes, come here, come to me, gotcha!
            return -1
        return -1

    def __3100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003178$
            # - ...A feather rod? I'm going to pluck out all the feathers!
            return 3100
        elif self.index == 1:
            # functionID=1 openTalkReward=True 
            # $script:0831180509003179$
            # - Kyaah! I was so close to catching it! Servant, you're getting better at snapping your wrist! Good!
            return -1
        return -1

    def __4000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003180$
            # - What are we playing today, meow? A ball? It's... flyinnnngggg! Come to meeeeee!
            return 4000
        elif self.index == 1:
            # $script:0831180509003181$
            # - Kyaah! I got it, meow! Meow? You want me to fetch it. No! It's mine now, and I'm going to toy with it all day long!
            return -1
        return -1

    def __4100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003182$
            # - What's this? What's inside? Let me in, let me in, let me in... I will get in!
            return 4100
        elif self.index == 1:
            # $script:0831180509003183$
            # - It's a... bit snug, but it's okay. Meow, so comfy! I'm sleepy... meow... Zzz... 
            return -1
        return -1

    def __5000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003184$
            # - $OwnerName$, as my servant, there are a few things you should know about me.
            return 5000
        elif self.index == 1:
            # $script:0831180509003185$
            # - First, I like dark, tight places where I can curl up. I hate open spaces and the cold. You shouldn't disturb me when I sleep inside your sock drawer.
            return 5000
        elif self.index == 2:
            # $script:0831180509003186$
            # - Second, I hate loud noises, such as vacuum cleaners. Those are forbidden in this house!
            return 5000
        elif self.index == 3:
            # $script:0831180509003187$
            # - Third, I love grooming myself, meow. I love to lick my hair and nails clean, but I don't like bathing. 
            return 5000
        elif self.index == 4:
            # $script:0831180509003188$
            # - Huh? You want to tell me a few thing about yourself too? I can already tell you'll be trouble. We've got time. You can tell me all about you later.
            return -1
        return -1

    def __5100(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003189$
            # - Haven't you heard it's rude to pry? But, if you insist on knowing more about me...
            return 5100
        elif self.index == 1:
            # $script:0831180509003190$
            # - I'm from $map:2000025$. $npc:11000075[gender:1]$ loves cats. Have you ever been in the presence of her fine cat, $npc:11000708$?
            return 5100
        elif self.index == 2:
            # $script:0831180509003191$
            # - $npc:11000075[gender:1]$ loves $npc:11000708$ like her own child. That's probably why it became a trend among the nobility to raise cats. Cats like me.
            return 5100
        elif self.index == 3:
            # $script:0831180509003192$
            # - Life at the palace was peaceful, but $npc:11000708$ said something to me that was life-changing. She said, "$MaidName$, you should find someone who loves you as much as the Empress loves me." So I set out to do just that.
            return 5100
        elif self.index == 4:
            # $script:0831180509003193$
            # - Oh, I'm not saying that person is you, $OwnerName$. Oh, no no. Let's not jump to conclusions.
            return -1
        return -1

    def __6000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003194$
            # - $npc:11000708$ is the $npc:11000075[gender:1]$'s favorite cat. A slender body, beautiful golden hair, a shiny ribbon... And I've descended from an equally noble bloodline.
            return 6000
        elif self.index == 1:
            # $script:0831180509003195$
            # - But $npc:11000708$'s beauty isn't what makes her so great, meow. The $npc:11000075[gender:1]$ relies on her for comfort. I don't want to imagine what Maple World would be like if $npc:11000708$ didn't exist...
            return 6000
        elif self.index == 2:
            # $script:0831180509003196$
            # - Want to know how important $npc:11000075[gender:1]$ is to her owner? Being the Empress of Maple World is not easy, meow. $npc:11000708$ once didn't go to the bathroom for three days to stay with the Empress while she was in deep anguish.
            return 6000
        elif self.index == 3:
            # $script:0831180509003197$
            # - I want to be as loyal as $npc:11000708$, but I can't not go to the bathroom for three days, mew. $OwnerName$, please make sure I never have to choose between you and the bathroom. 
            return -1
        return -1

    def __7000(self, pick: int) -> int:
        if self.index == 0:
            # $script:0831180509003198$
            # - When I lived in the Palace, I used to look forward to the Cat Assembly. It's a meeting among the courtiers who love cats, meow. It's hosted by the $npc:11000075[gender:1]$, and the guests of honor are us cats.
            return 7000
        elif self.index == 1:
            # $script:0831180509003199$
            # - At the meeting, everyone from the $npc:11000075[gender:1]$ to $npc:11000601[gender:1]$ and even the guards laugh and chat regardless of station, meow. No one mentions serious subjects like the Lapentas or the Shadow World.
            return 7000
        elif self.index == 2:
            # $script:0831180509003200$
            # - It was always fun to hear what was going on in the palace. Oh, speaking of which, I remember something $npc:11000708$ told me, meow.
            return 7000
        elif self.index == 3:
            # $script:0831180509003201$
            # - Everyone thinks the Empress stays in the palace all the time, working, but she goes out sometimes, meow. When she does, she disguises herself and crawls through a hole in a corner of the castle wall.
            return 7000
        elif self.index == 4:
            # $script:0831180509003202$
            # - One time, she went to her hair salon in $map:52000008$... and got caught by $npcName:11000702[gender:0]$, meow!
            return 7000
        elif self.index == 5:
            # $script:0831180509003203$
            # - The Empress quickly used $skill:20000011$ to scale the castle wall and run away from him, meow. Who knew she was good at $skill:20000011$? I'd love to see her use it one day.
            return -1
        return -1

    def __100(self, pick: int) -> int:
        # $script:0831180509003204$
        # - You're a stranger, meow.  I hate strangers... 
        if pick == 0:
            # $script:0831180509003205$
            # - (Pat her on the head.) 
            # TODO: goto 101,102
            self.close()
            return -1
        elif pick == 1:
            # $script:0831180509003206$
            # - (Rub her belly.)
            # TODO: goto 103,104
            self.close()
            return -1
        elif pick == 2:
            # $script:0831180509003207$
            # - Here, kitty kitty kitty.
            # TODO: goto 105,106
            self.close()
            return -1
        return -1

    def __101(self, pick: int) -> int:
        # $script:0831180509003208$
        # - How dare you touch me, lowly human?!
        return -1

    def __102(self, pick: int) -> int:
        # $script:0831180509003209$
        # - Everyone who visits the house wants to touch me, meow. But do they think to ask first? Noooo.
        return -1

    def __103(self, pick: int) -> int:
        # $script:0831180509003210$
        # - Kyaawwoonngghh! Not there! Get away from me!!
        return -1

    def __104(self, pick: int) -> int:
        # $script:0831180509003211$
        # - Rude!!!
        return -1

    def __105(self, pick: int) -> int:
        # $script:0831180509003212$
        # - ...?
        return -1

    def __106(self, pick: int) -> int:
        # $script:0831180509003213$
        # - ...Huh? 
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
            return Option.CLOSE
        elif (self.state, self.index) == (1200, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1200, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1201, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1202, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1211, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1212, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1212, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (1300, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1300, 1):
            return Option.NEXT
        elif (self.state, self.index) == (1300, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1301, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1302, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1311, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1312, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1400, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1400, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1401, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1402, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1411, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1412, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1500, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1500, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1501, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1502, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1511, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1511, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (1512, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1512, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (1600, 0):
            return Option.NEXT
        elif (self.state, self.index) == (1600, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (1601, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1602, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1611, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (1612, 0):
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
        elif (self.state, self.index) == (2200, 0):
            return Option.NEXT
        elif (self.state, self.index) == (2200, 1):
            return Option.NEXT
        elif (self.state, self.index) == (2200, 2):
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
            return Option.NEXT
        elif (self.state, self.index) == (4000, 1):
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
            return Option.NEXT
        elif (self.state, self.index) == (5000, 3):
            return Option.NEXT
        elif (self.state, self.index) == (5000, 4):
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
            return Option.CLOSE
        elif (self.state, self.index) == (6000, 0):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 1):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 2):
            return Option.NEXT
        elif (self.state, self.index) == (6000, 3):
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
            return Option.NEXT
        elif (self.state, self.index) == (7000, 5):
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
