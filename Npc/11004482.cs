using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004482: Wariki
/// </summary>
public class _11004482 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0104110407012553$
    // - I've never seen such a place... Huh? Where'd you come from?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0104110407012554$
                // - I've never seen such a place... Huh? Where'd you come from?
                switch (selection) {
                    // $script:0104110407012555$
                    // - Who are you?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0104110407012556$
                // - Oh, you kidder. You know me. We boarded Sky Fortress together!
                switch (selection) {
                    // $script:0104110407012557$
                    // - I'm pretty sure I've never met you before.
                    case 0:
                        return 12;
                    // $script:0104110407012558$
                    // - Of course! I'd never forget a face like yours.
                    case 1:
                        return 13;
                }
                return -1;
            case (12, 0):
                // $script:0104110407012559$
                // - You scatterbrain! I was the facility manager at the $map:52010059$. I can't believe you forgot about me...
                return 12;
            case (12, 1):
                // $script:0104110407012560$
                // - Anyway, Bastet picked up this structure during a routine scan. I thought I'd check it out, but this place is thick with monsters...
                switch (selection) {
                    // $script:0104110407012561$
                    // - Who's Bastet?
                    case 0:
                        return 14;
                    // $script:0104110407012562$
                    // - Why are you here, anyway?
                    case 1:
                        return 16;
                }
                return -1;
            case (13, 0):
                // $script:0104110407012563$
                // - Of course you didn't forget me! I'm unforgettable, as my mother always said.
                return 13;
            case (13, 1):
                // $script:0104110407012564$
                // - Anyway, Bastet picked up this structure during a routine scan. I thought I'd check it out, but this place is thick with monsters...
                return 13;
            case (13, 2):
                // $script:0104110407012565$
                // - I've never seen such a building. The architecture is breathtaking...
                return 13;
            case (13, 3):
                // $script:0104110407012566$
                // - Oh... Maybe this isn't the time for such chatter. I'd better get out of here while I still can.
                return -1;
            case (14, 0):
                // $script:0104110407012567$
                // - Not who, but what. Bastet is our cutting-edge surveillance satellite! There's nothing she can't spot. I think.
                return 14;
            case (14, 1):
                // $script:0104110407012568$
                // - She's technically still a prototype. When Kritias showed up from out of nowhere, it seemed like a good chance to put her through her paces.
                return 14;
            case (14, 2):
                // $script:0104110407012569$
                // - She can count your nose hairs from orbit!
                switch (selection) {
                    // $script:0104110407012570$
                    // - Impressive! Who came up with that?
                    case 0:
                        return 15;
                }
                return -1;
            case (15, 0):
                // $script:0104110407012571$
                // - Who do you think? $npcName:11004437[gender:0]$, of course! At Captain $npcName:11004434[gender:0]$ command, of course.
                return 15;
            case (15, 1):
                // $script:0104110407012572$
                // - The captain even came up with the name "Bastet," you see. I wonder what it means...?
                switch (selection) {
                    // $script:0114162007012707$
                    // - Beats me.
                    case 0:
                        return 17;
                }
                return -1;
            case (16, 0):
                // $script:0104110407012573$
                // - I'm here to research structures and facilities here on Kritias, of course. Unfortunately, the going hasn't exactly been easy.
                return 16;
            case (16, 1):
                // $script:0104110407012574$
                // - But it's definitely worth it! Look at this beauty of a building right here.
                return 16;
            case (16, 2):
                // $script:0104110407012575$
                // - Oh... Maybe this isn't the time for such chatter. I'd better get out of here while I still can.
                return -1;
            case (17, 0):
                // $script:0114162107012707$
                // - I'm sure it means <i>something</i>. The captain isn't the sort to name things all willy-nilly.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Next,
            (13, 1) => NpcTalkButton.Next,
            (13, 2) => NpcTalkButton.Next,
            (13, 3) => NpcTalkButton.Close,
            (14, 0) => NpcTalkButton.Next,
            (14, 1) => NpcTalkButton.Next,
            (14, 2) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.Next,
            (15, 1) => NpcTalkButton.SelectableDistractor,
            (16, 0) => NpcTalkButton.Next,
            (16, 1) => NpcTalkButton.Next,
            (16, 2) => NpcTalkButton.Close,
            (17, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
