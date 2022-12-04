""" 11004482: Wariki """
from npc_api import Option, Script
import random


class Main(Script):
    def first(self) -> int:
        return 10

    def select(self) -> int:
        return 0

    def __0(self, pick: int) -> int:
        # $script:0104110407012553$
        # - I've never seen such a place... Huh? Where'd you come from?
        return None # TODO

    def __10(self, pick: int) -> int:
        # $script:0104110407012554$
        # - I've never seen such a place... Huh? Where'd you come from?
        if pick == 0:
            # $script:0104110407012555$
            # - Who are you?
            return 11
        return -1

    def __11(self, pick: int) -> int:
        # $script:0104110407012556$
        # - Oh, you kidder. You know me. We boarded Sky Fortress together!
        if pick == 0:
            # $script:0104110407012557$
            # - I'm pretty sure I've never met you before.
            return 12
        elif pick == 1:
            # $script:0104110407012558$
            # - Of course! I'd never forget a face like yours.
            return 13
        return -1

    def __12(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104110407012559$
            # - You scatterbrain! I was the facility manager at the $map:52010059$. I can't believe you forgot about me...
            return 12
        elif self.index == 1:
            # $script:0104110407012560$
            # - Anyway, Bastet picked up this structure during a routine scan. I thought I'd check it out, but this place is thick with monsters...
            if pick == 0:
                # $script:0104110407012561$
                # - Who's Bastet?
                return 14
            elif pick == 1:
                # $script:0104110407012562$
                # - Why are you here, anyway?
                return 16
            return -1
        return -1

    def __13(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104110407012563$
            # - Of course you didn't forget me! I'm unforgettable, as my mother always said.
            return 13
        elif self.index == 1:
            # $script:0104110407012564$
            # - Anyway, Bastet picked up this structure during a routine scan. I thought I'd check it out, but this place is thick with monsters...
            return 13
        elif self.index == 2:
            # $script:0104110407012565$
            # - I've never seen such a building. The architecture is breathtaking...
            return 13
        elif self.index == 3:
            # $script:0104110407012566$
            # - Oh... Maybe this isn't the time for such chatter. I'd better get out of here while I still can.
            return -1
        return -1

    def __14(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104110407012567$
            # - Not who, but what. Bastet is our cutting-edge surveillance satellite! There's nothing she can't spot. I think.
            return 14
        elif self.index == 1:
            # $script:0104110407012568$
            # - She's technically still a prototype. When Kritias showed up from out of nowhere, it seemed like a good chance to put her through her paces.
            return 14
        elif self.index == 2:
            # $script:0104110407012569$
            # - She can count your nose hairs from orbit!
            if pick == 0:
                # $script:0104110407012570$
                # - Impressive! Who came up with that?
                return 15
            return -1
        return -1

    def __15(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104110407012571$
            # - Who do you think? $npcName:11004437[gender:0]$, of course! At Captain $npcName:11004434[gender:0]$ command, of course.
            return 15
        elif self.index == 1:
            # $script:0104110407012572$
            # - The captain even came up with the name "Bastet," you see. I wonder what it means...?
            if pick == 0:
                # $script:0114162007012707$
                # - Beats me.
                return 17
            return -1
        return -1

    def __16(self, pick: int) -> int:
        if self.index == 0:
            # $script:0104110407012573$
            # - I'm here to research structures and facilities here on Kritias, of course. Unfortunately, the going hasn't exactly been easy.
            return 16
        elif self.index == 1:
            # $script:0104110407012574$
            # - But it's definitely worth it! Look at this beauty of a building right here.
            return 16
        elif self.index == 2:
            # $script:0104110407012575$
            # - Oh... Maybe this isn't the time for such chatter. I'd better get out of here while I still can.
            return -1
        return -1

    def __17(self, pick: int) -> int:
        # $script:0114162107012707$
        # - I'm sure it means <i>something</i>. The captain isn't the sort to name things all willy-nilly.
        return -1

    def button(self) -> Option:
        if (self.state, self.index) == (10, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (11, 0):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (12, 0):
            return Option.NEXT
        elif (self.state, self.index) == (12, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (13, 0):
            return Option.NEXT
        elif (self.state, self.index) == (13, 1):
            return Option.NEXT
        elif (self.state, self.index) == (13, 2):
            return Option.NEXT
        elif (self.state, self.index) == (13, 3):
            return Option.CLOSE
        elif (self.state, self.index) == (14, 0):
            return Option.NEXT
        elif (self.state, self.index) == (14, 1):
            return Option.NEXT
        elif (self.state, self.index) == (14, 2):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (15, 0):
            return Option.NEXT
        elif (self.state, self.index) == (15, 1):
            return Option.SELECTABLE_DISTRACTOR
        elif (self.state, self.index) == (16, 0):
            return Option.NEXT
        elif (self.state, self.index) == (16, 1):
            return Option.NEXT
        elif (self.state, self.index) == (16, 2):
            return Option.CLOSE
        elif (self.state, self.index) == (17, 0):
            return Option.CLOSE
        return Option.NONE
