using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004482: Wariki
/// </summary>
public class _11004482 : NpcScript {
    internal _11004482(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0104110407012553$ 
                // - I've never seen such a place... Huh? Where'd you come from?
                return true;
            case 10:
                // $script:0104110407012554$ 
                // - I've never seen such a place... Huh? Where'd you come from?
                switch (selection) {
                    // $script:0104110407012555$
                    // - Who are you?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0104110407012556$ 
                // - Oh, you kidder. You know me. We boarded Sky Fortress together!
                switch (selection) {
                    // $script:0104110407012557$
                    // - I'm pretty sure I've never met you before.
                    case 0:
                        Id = 12;
                        return false;
                    // $script:0104110407012558$
                    // - Of course! I'd never forget a face like yours.
                    case 1:
                        Id = 13;
                        return false;
                }
                return true;
            case 12:
                // $script:0104110407012559$ 
                // - You scatterbrain! I was the facility manager at the $map:52010059$. I can't believe you forgot about me...
                // $script:0104110407012560$ 
                // - Anyway, Bastet picked up this structure during a routine scan. I thought I'd check it out, but this place is thick with monsters...
                switch (selection) {
                    // $script:0104110407012561$
                    // - Who's Bastet?
                    case 0:
                        Id = 14;
                        return false;
                    // $script:0104110407012562$
                    // - Why are you here, anyway?
                    case 1:
                        Id = 16;
                        return false;
                }
                return true;
            case 13:
                // $script:0104110407012563$ 
                // - Of course you didn't forget me! I'm unforgettable, as my mother always said.
                // $script:0104110407012564$ 
                // - Anyway, Bastet picked up this structure during a routine scan. I thought I'd check it out, but this place is thick with monsters...
                // $script:0104110407012565$ 
                // - I've never seen such a building. The architecture is breathtaking...
                // $script:0104110407012566$ 
                // - Oh... Maybe this isn't the time for such chatter. I'd better get out of here while I still can.
                return true;
            case 14:
                // $script:0104110407012567$ 
                // - Not who, but what. Bastet is our cutting-edge surveillance satellite! There's nothing she can't spot. I think.
                // $script:0104110407012568$ 
                // - She's technically still a prototype. When Kritias showed up from out of nowhere, it seemed like a good chance to put her through her paces.
                // $script:0104110407012569$ 
                // - She can count your nose hairs from orbit!
                switch (selection) {
                    // $script:0104110407012570$
                    // - Impressive! Who came up with that?
                    case 0:
                        Id = 15;
                        return false;
                }
                return true;
            case 15:
                // $script:0104110407012571$ 
                // - Who do you think? $npcName:11004437[gender:0]$, of course! At Captain $npcName:11004434[gender:0]$ command, of course.
                // $script:0104110407012572$ 
                // - The captain even came up with the name "Bastet," you see. I wonder what it means...?
                switch (selection) {
                    // $script:0114162007012707$
                    // - Beats me.
                    case 0:
                        Id = 17;
                        return false;
                }
                return true;
            case 16:
                // $script:0104110407012573$ 
                // - I'm here to research structures and facilities here on Kritias, of course. Unfortunately, the going hasn't exactly been easy.
                // $script:0104110407012574$ 
                // - But it's definitely worth it! Look at this beauty of a building right here.
                // $script:0104110407012575$ 
                // - Oh... Maybe this isn't the time for such chatter. I'd better get out of here while I still can.
                return true;
            case 17:
                // $script:0114162107012707$ 
                // - I'm sure it means <i>something</i>. The captain isn't the sort to name things all willy-nilly.
                return true;
            default:
                return true;
        }
    }
}
