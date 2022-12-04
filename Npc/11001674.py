""" 11001674: Bravos """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 30

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0629000607006397$
        # - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
        return None # TODO

    def __30(self, pick: int) -> int:
        # $script:0629000607006400$
        # - Do you have business with me? Hm?
        if pick == 0:
            # $script:0629000607006401$
            # - Tell me about yourself.
            return 40
        elif pick == 1:
            # $script:0629000607006402$
            # - What do you know about the $map:52000034$?
            return 70
        elif pick == 2:
            # $script:0706165507006631$
            # - What happened to the vagrants Blackstar took hostage?
            return 80
        elif pick == 3:
            # $script:0712221207006725$
            # - Tell me about $npcName:11001547[gender:0]$.
            return 90
        return -1

    def __40(self, pick: int) -> int:
        # $script:0708181707006654$
        # - How about this. You know why they call me $npcName:11001674[gender:0]$?
        if pick == 0:
            # $script:0708181707006655$
            # - No clue.
            return 50
        elif pick == 1:
            # $script:0708181707006656$
            # - Yes.
            return 60
        return -1

    def __50(self, pick: int) -> int:
        # $script:0629000607006403$
        # - I'm so great I deserve a standing ovation! Haw! I can't believe you never heard of me. Well, remember me for next time.
        if pick == 0:
            # $script:0708181707006657$
            # - I heard your real name is Brav-gross.
            return 51
        return -1

    def __51(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629000607006404$
            # - Has somebody been tarnishing my good name? It's $npcName:11001682[gender:0]$, isn't it?
            return 51
        elif self.index == 1:
            # $script:0708181707006658$
            # - Ahem! I don't know where you heard that, but it's a dirty lie. $npcName:11001674[gender:0]$ is my name, and $npcName:11001674[gender:0]$ is who I am. Now get outta here, before you make me mad!
            if pick == 0:
                # $script:0708225907006698$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __60(self, pick: int) -> int:
        # $script:0629000607006405$
        # - You probably already heard this, but listen anyway. They call me Bravos 'cause I'm so great I deserve a standing ovation! Get it?
        if pick == 0:
            # $script:0708181707006659$
            # - I heard your real name is Brav-gross.
            return 61
        return -1

    def __61(self, pick: int) -> int:
        if self.index == 0:
            # $script:0629000607006406$
            # - Has somebody been tarnishing my good name? It's $npcName:11001682[gender:0]$, isn't it?
            return 61
        elif self.index == 1:
            # $script:0708181707006660$
            # - Ahem! I don't know where you heard that, but it's a dirty lie. $npcName:11001674[gender:0]$ is my name, and $npcName:11001674[gender:0]$ is who I am. Now get outta here, before you make me mad!
            if pick == 0:
                # $script:0708225907006699$
                # - Let's talk about something else.
                return 30
            return -1
        return -1

    def __70(self, pick: int) -> int:
        # $script:0706165507006632$
        # - I don't know, exactly. I heard we were gonna set up a base of operations in $map:02000001$, but there were problems with the construction. Eventually we gave up on the building, and... Well, take a look around you.
        if pick == 0:
            # $script:0706165507006633$
            # - Blackstar is moving in on $map:02000001$?
            return 71
        return -1

    def __71(self, pick: int) -> int:
        # $script:0706165507006634$
        # - You really have no idea how big Blackstar is, do you? Every gangster in the underworld is connected to it one way or another. Gray Wolf or not, you can't take it on by yourself.
        if pick == 0:
            # $script:0708181707006661$
            # - How big is your organization, really?
            return 72
        return -1

    def __72(self, pick: int) -> int:
        # $script:0708181707006662$
        # - Why do you care? That's none of your business. Now, I'd say that's enough stupid questions out of you.
        if pick == 0:
            # $script:0708225907006700$
            # - Let's talk about something else.
            return 30
        return -1

    def __80(self, pick: int) -> int:
        if self.index == 0:
            # $script:0708181707006663$
            # - How should I know? It wasn't my operation. I don't even know where they are. I know you made some sorta deal with the boss, but let me give you some advice anyway: don't do anything stupid.
            return 80
        elif self.index == 1:
            # $script:0708181707006664$
            # - What I wanna know is why you're going along with whatever the boss says. A strong fighter like you could take Blackstar for $male:himself,female:herself$ if $male:he,female:she$ wanted. Maybe you just don't have the guts.
            if pick == 0:
                # $script:0708181707006665$
                # - I'm just afraid for their safety.
                return 81
            return -1
        return -1

    def __81(self, pick: int) -> int:
        # $script:0708181707006666$
        # - Yeah, sure you are. And that's the only reason you wanna know?
        if pick == 0:
            # $script:0708181707006667$
            # - I lost the match. I'm honor bound to work with him.
            return 82
        return -1

    def __82(self, pick: int) -> int:
        # $script:0708181707006668$
        # - You're a bigger fool than $npcName:11001682[gender:0]$. Well, I guess I can't hold it against you if it means you're working <i>with</i> us instead of <i>against</i> us.
        if pick == 0:
            # $script:0708225907006701$
            # - Let's talk about something else.
            return 30
        return -1

    def __90(self, pick: int) -> int:
        # $script:0712221207006726$
        # - You've come to the right man. What do you wanna know?
        if pick == 0:
            # $script:0712221207006727$
            # - Does $npcName:11001618[gender:0]$ get along with $npcName:11001547[gender:0]$?
            return 91
        return -1

    def __91(self, pick: int) -> int:
        # $script:0712221207006728$
        # - Maybe you didn't know this, but $npcName:11001547[gender:0]$ is the boss's son. Heir to the kingdom, though you wouldn't know it to talk to him. All the officers sure seem to like him, though.
        if pick == 0:
            # $script:0712221207006729$
            # - And why is that?
            return 92
        return -1

    def __92(self, pick: int) -> int:
        # $script:0712221207006730$
        # - You ever meet a boss's kid before? You know the type. Throws his daddy's weight around. Makes all the company goons do whatever he says. Well, $npcName:11001547[gender:0]$ ain't like that. He doesn't care about power or money. So why wouldn't they like him?
        if pick == 0:
            # $script:0712221207006731$
            # - And what does the rank-and-file think?
            return 93
        return -1

    def __93(self, pick: int) -> int:
        # $script:0712221207006732$
        # - $npcName:11001547[gender:0]$ is our hero. His pop's the head honcho, but $npcName:11001547[gender:0]$ didn't ever get nothing that he didn't earn with his own two fists. A real man's man, you know?
        if pick == 0:
            # $script:0712221207006733$
            # - Let's talk about something else.
            return 30
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (30, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (40, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (50, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (51, 0):
            return Option.NEXT
        elif (self.state, self.index) == (51, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (60, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (61, 0):
            return Option.NEXT
        elif (self.state, self.index) == (61, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (70, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (71, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (72, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (80, 0):
            return Option.NEXT
        elif (self.state, self.index) == (80, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (81, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (82, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (90, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (91, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (92, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (93, 0):
            return Option.SELECTABLE_DISTRACTOR
        return Option.NONE
