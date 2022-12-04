""" 11001682: Zabeth """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006468$
        # - What're you staring at? You want a piece of me?
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0629000607006471$
        # - You got something to stay, or you just gonna stand there and stare all night? Actually, I don't care. Get outta here.
        if pick == 0:
            # $script:0706173707006643$
            # - How are you doing?
            return 40
        elif pick == 1:
            # $script:0708220807006669$
            # - What do you know about the $map:52000034$?
            return 50
        elif pick == 2:
            # $script:0708220807006670$
            # - What happened to the vagrants Blackstar took hostage?
            return 60
        elif pick == 3:
            # $script:0712221207006734$
            # - Tell me about $npcName:11001547[gender:0]$.
            return 70
        return -1

    def __40(self, pick: int) -> int:
        # $script:0708220807006671$
        # - What do you want to hear? Tales of my exploits? The names of punks I beat to a bloody pulp?
        if pick == 0:
            # $script:0708220807006672$
            # - How did you get the name "Zabeth?"
            return 41
        return -1

    def __41(self, pick: int) -> int:
        if self.index == 0:
            # $script:0708220807006673$
            # - Wh-why do you want to know? Did $npcName:11001674[gender:0]$ put you up to this?
            return 41
        elif self.index == 1:
            # $script:0708220807006674$
            # - Ahem! Don't listen to that fool. My name is Eliza—
            return 41
        elif self.index == 2:
            # $script:0708220807006675$
            # - I-I mean, it's $npcName:11001682[gender:0]$! Just $npcName:11001682[gender:0]$, got it?!
            if pick == 0:
                # $script:0708220807006676$
                # - Your name is Eliza-what?
                return 42
            return -1
        return -1

    def __42(self, pick: int) -> int:
        # $script:0708220807006677$
        # - Quit it with the stupid questions! It's none of your business!
        if pick == 0:
            # $script:0708225907006702$
            # - Let's talk about something else.
            return 30
        return -1

    def __50(self, pick: int) -> int:
        if self.index == 0:
            # $script:0708220807006678$
            # - Is that what this place's called? I didn't know that. I don't care, neither. I just want to get back to base. I belong at $map:63000020$, watching over the fighters. This town doesn't hold a candle to the excitement of the ring.
            return 50
        elif self.index == 1:
            # $script:0706173707006644$
            # - That place before... You could feel the fighting spirit in the air! This place, on the other hand... Words don't do it justice.
            if pick == 0:
                # $script:0708225907006703$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0708220807006679$
        # - I got no idea who you're talking about. Ask $npcName:11001674[gender:0]$. Now, the one I'm interested in... is you. They say you're the Gray Wolf. I don't buy it, 'cause why would the Gray Wolf work with the boss? Gray Wolf or not, you could fight your way to the top of Blackstar if you wanted.
        if pick == 0:
            # $script:0708220807006680$
            # - My code of honor wouldn't allow that.
            return 61
        return -1

    def __61(self, pick: int) -> int:
        # $script:0708220807006681$
        # - Code of honor! That's rich. Sounds like you're too much of a coward to take on Blackstar. Can't blame you, though. I wouldn't want to fight me, neither.
        if pick == 0:
            # $script:0708220807006682$
            # - (Raise your fists.)
            return 62
        return -1

    def __62(self, pick: int) -> int:
        # $script:0708220807006683$
        # - Uh...! D-did you hear that? M-my stomach's calling. I better go home and... and turn it off...
        if pick == 0:
            # $script:0708225907006704$
            # - Let's talk about something else.
            return 30
        return -1

    def __70(self, pick: int) -> int:
        # $script:0712221207006735$
        # - Yeah? What do you want to know?
        if pick == 0:
            # $script:0712221207006736$
            # - I want to know about $npcName:11001547[gender:0]$'s fighting style.
            return 71
        return -1

    def __71(self, pick: int) -> int:
        # $script:0712221207006737$
        # - What're you asking me for? You're the one who faced him in the ring! I told you he'd take you out with a single punch, didn't I? Ha!
        if pick == 0:
            # $script:0712221207006738$
            # - How does $npcName:11001547[gender:0]$ train?
            return 72
        return -1

    def __72(self, pick: int) -> int:
        if self.index == 0:
            # $script:0712221207006739$
            # - Trying to figure out how he got so strong, eh? I think he was just born strong. I hear he never slacks off on his training, but no amount of training makes you as tough as he is.
            return 72
        elif self.index == 1:
            # $script:0712221207006740$
            # - He's got a 30-step routine he goes through every single day. Enough to give a normal man a heart attack, they say. Some of the other lunks in the organization tried it, and they all passed out foaming at the mouth.
            if pick == 0:
                # $script:0712221207006741$
                # - What's the routine?
                return 73
            return -1
        return -1

    def __73(self, pick: int) -> int:
        if self.index == 0:
            # $script:0712221207006742$
            # - It's nothing special, really. 4,000 knuckle push-ups, 1,000 finger push-ups, 5,000 sit-ups, 5,000 squats, 200 laps around the track... That sort of thing.
            return 73
        elif self.index == 1:
            # $script:0712221207006743$
            # - He uses sandbags and chunks of meat as punching bags, and he lets others whale on him to toughen him up. There's no secret to his training. He's just that tough.
            if pick == 0:
                # $script:0712221207006744$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (41, 0):
            return Option.NEXT
        elif (self.state, self.index) == (41, 1):
            return Option.NEXT
        elif (self.state, self.index) == (41, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (42, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.NEXT
        elif (self.state, self.index) == (50, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (62, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (71, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (72, 0):
            return Option.NEXT
        elif (self.state, self.index) == (72, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (73, 0):
            return Option.NEXT
        elif (self.state, self.index) == (73, 1):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
