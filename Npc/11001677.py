""" 11001677: Royal Guard """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 50

    def select(self) -> int:
        return 1

    def __1(self, pick: int) -> int:
        # $script:0704194107006574$
        # - How may I help you?
        return None # TODO

    def __50(self, pick: int) -> int:
        # $script:0704194107006579$
        # - Welcome to $map:02000001$. How may I help you?
        if pick == 0:
            # $script:0704194107006580$
            # - Sell me on this $map:02000001$ business.
            return 51
        elif pick == 1:
            # $script:0704194107006581$
            # - What happened to the empress's celebration?
            return 52
        elif pick == 2:
            # $script:0704194107006582$
            # - Hey there. I'm new in town.
            # TODO: goto 61,62,63,64,65,66,67,68,69,70,80,90
            self.close()
            return -1
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0704194107006584$
            # - $map:02000001$ is the biggest city in all of Maple World and the seat of $npcName:11000075[gender:1]$'s power.
            return 51
        elif self.index == 1:
            # $script:0704194107006585$
            # - $map:02000025$ watches over the city from the north. It's off-limits to the public, I'm afraid. Her majesty's safety takes priority over the curiosity of tourists.
            return 51
        elif self.index == 2:
            # $script:0704194107006586$
            # - The $map:02000188$, the Banners of Glory, and a taxi stop are all conveniently located in the center of the city. For a reasonable fee, you can hire a taxi to take you to any other taxi stop you've visited, you know. Oh, and the job instructors from all over are gathered in the $map:02000188$.
            return 51
        elif self.index == 3:
            # $script:0704194107006587$
            # - The Banners of Glory in front of the palace mark the victories of certain powerful guilds and individuals. We update the banners all the time, so you can stop by whenever you like to see who has the most trophies and victories.
            return 51
        elif self.index == 4:
            # $script:0704194107006588$
            # - In the northern parts of the city, you'll find the royal office and library. $map:02000031$ is a must-see for any book lover, of course. It's not the biggest library in Maple World, but I like to think that it's the best. When I'm off-duty, I love to wander the stacks.
            return 51
        elif self.index == 5:
            # $script:0704194107006589$
            # - Behind the library is a shopping district where you can find special items, anything from home decor to mounts.
            return 51
        elif self.index == 6:
            # $script:0704194107006590$
            # - To the southwest, you'll find shops that sell equipment and other supplies. $npcName:11000004[gender:0]$ is one of the best smiths in the land, and $npcName:11000010[gender:1]$ sells all the latest herbs and potions. Never pick a fight without a stack of potions, I always say.
            return 51
        elif self.index == 7:
            # $script:0704194107006591$
            # - Head southeast and you'll find the residential district and hospital. Kick your feet up and relax after a long journey at $map:02000033$. Have your ailments treated by Tria's finest physician at $map:02000125$. And there's nothing $npcName:11000038[gender:0]$ can't cure.
            return 51
        elif self.index == 8:
            # $script:0704194107006592$
            # - And that's $map:02000001$ in a nutshell. A long, wordy nutshell. If I told you everything about the city, you'd be here all night. Is there anything else you want to know?
            return -1
        return -1

    def __52(self, pick: int) -> int:
        if self.index == 0:
            # $script:0704194107006593$
            # - I know that you probably came from very far away to see the empress, but these things can't be helped. Thank you for understanding that we had to cancel the open court in the face of unexpected disaster.
            return 52
        elif self.index == 1:
            # $script:0704194107006594$
            # - $map:02000001$ is the political, economic, and cultural heart of Maple World, so it's always crowded. But in preparation for open court, there must have been ten times the normal number of people here.
            return 52
        elif self.index == 2:
            # $script:0704194107006595$
            # - Of course, when you have so many people in one place, problems are certain to crop up. Thieves, con artists, and the incident at the celebra—Oops. Maybe I shouldn't have said that.
            return 52
        elif self.index == 3:
            # $script:0704194107006596$
            # - Anyway, Captain $npcName:11000119[gender:0]$ is determined to keep the peace. Enjoy your stay here, and stay out of trouble. For your own sake.
            return -1
        return -1

    def __53(self, pick: int) -> int:
        if self.index == 0:
            # $script:0704194107006611$
            # - Everyone in Maple World dreams of having a home to call their own. The empress and her court work tirelessly to open up new plots of land, but there's only so much space, so not many people can have the luxury of owning a magnicifent villa.
            return 53
        elif self.index == 1:
            # $script:0704194107006612$
            # - If you don't have a house yet, you should consider $map:02000001$. Property in the city proper is expensive, but the outlying suburb of $map:02000002$ is partially subsidized by the empress. And there's always $map:02000119$... And $map:02000064$...
            return 53
        elif self.index == 2:
            # $script:0704194107006613$
            # - There are many advantages to owning a house, you know. These days, every home comes with a device that will let you teleport there at anytime from almost anywhere. Let me tell you, it's saved my butt plenty of times after a long day of patrolling $map:02000092$.
            return 53
        elif self.index == 3:
            # $script:0704194107006614$
            # - And the merchants in $map:02000036$, west of $map:02000023$, have all kinds of interesting furnishings for sale. Decorate your floors, walls, furniture, and yard to create a house that's unique to you. Some merchants will even sell buildings you can place on your lot! When you're ready to buy, go to $map:02000036$ to shop for your house.
            return 53
        elif self.index == 4:
            # $script:0704194107006615$
            # - If you already have a house, you could always hire an assistant or two to keep you company. $npcName:11000700[gender:1]$ in the northwestern district of $map:02000001$ hires them out. But first thing's first. You have to buy a house before you can get an assistant!
            return -1
        return -1

    def __61(self, pick: int) -> int:
        # $script:0704194107006599$
        # - Gosh, you're a Knight! I may be a humble guard now, but someday I want to be just like you.
        return -1

    def __62(self, pick: int) -> int:
        # $script:0704194107006600$
        # - You know, an old friend of mine left town to become a Berserker. I wonder how he's doing...
        return -1

    def __63(self, pick: int) -> int:
        # $script:0704194107006601$
        # - If you're a Wizard, then you'll want to visit $map:02000031$. Even the fairies of $map:02000023$ say our library is the best.
        return -1

    def __64(self, pick: int) -> int:
        # $script:0704194107006602$
        # - It is an honor to serve you, Priest. How is the empress doing?
        return -1

    def __65(self, pick: int) -> int:
        # $script:0704194107006603$
        # - You're a Green Hood, aren't you? That's great. We guard could use the support of people like you during these crazy times.
        return -1

    def __66(self, pick: int) -> int:
        # $script:0704194107006604$
        # - You're a Heavy Gunner, aren't you? I've always wanted to visit $map:2000270$.
        return -1

    def __67(self, pick: int) -> int:
        # $script:0704194107006605$
        # - We're watching you, Thief. You are a guest of the kingdom, but we won't abide any criminal activity.
        return -1

    def __68(self, pick: int) -> int:
        # $script:0704194107006606$
        # - Know this, Assassin. $map:02000001$ is a city of light.
        return -1

    def __69(self, pick: int) -> int:
        if self.index == 0:
            # $script:0704194107006597$
            # - If you're looking to take up a job, you should make a stop at the $map:02000188$ in the center of $map:02000001$. Job masters from all over the world are gathered there.
            return 69
        elif self.index == 1:
            # $script:0704194107006598$
            # - The timing is pretty lucky for you. If it weren't for the empress's court, they wouldn't be here. Of course, if you aren't at least level 10, they won't even talk to you.
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:0704194107006607$
        # - They say Runeblades are masters of swordsmanship and magic. Being good at either one is hard enough... How did you manage to master both?
        return -1

    def __80(self, pick: int) -> int:
        # $script:0704194107006608$
        # - Hey, you're the Gray Wolf of $map:02000100$, aren't you? They say that you're a master martial artist and that you're taking the fight straight to the gangsters! A real champion of the people! You're my hero! Though... I thought you'd be taller.
        if pick == 0:
            # $script:0704194107006609$
            # - You've mistaken me for someone else.
            return 81
        return -1

    def __81(self, pick: int) -> int:
        # $script:0704194107006610$
        # - R-really? I'm sorry. I always wanted to meet $male:him,female:her$ in person. I guess I just got excited.
        return -1

    def __90(self, pick: int) -> int:
        # $script:0805235907007127$
        # - Not many people know this, but there's a sect of animal people who live in the mountains and practice mysterious martial arts. I've heard legends that they can even bring the dead back to life...
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (50, 0):
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
            return Option.NEXT
        elif (self.state, self.index) == (51, 8):
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
            return Option.NEXT
        elif (self.state, self.index) == (53, 3):
            return Option.NEXT
        elif (self.state, self.index) == (53, 4):
            return Option.CLOSE
        elif (self.state, self.index) == (61, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (62, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (63, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (64, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (65, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (66, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (67, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (68, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (69, 0):
            return Option.NEXT
        elif (self.state, self.index) == (69, 1):
            return Option.CLOSE
        elif (self.state, self.index) == (70, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (80, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (81, 0):
            return Option.CLOSE
        elif (self.state, self.index) == (90, 0):
            return Option.CLOSE
        return Option.NONE
