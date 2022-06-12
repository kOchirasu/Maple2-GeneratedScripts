using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001397: Akamorro
/// </summary>
public class _11001397 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;50
    }

    // Select 0:
    // $script:1217193307005397$
    // - What brings you here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1226235907005601$
                // - I like quiet places. Real quiet places.
                switch (selection) {
                    // $script:1226235907005602$
                    // - Why's that?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1226235907005603$
                // - I've got my reasons.
                switch (selection) {
                    // $script:1226235907005604$
                    // - Such as...?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1226235907005605$
                // - I like quiet places because then I don't have to deal with nosy people like you. But I guess it's time for me to look for a new quiet place.
                return -1;
            case (40, 0):
                // $script:1227015507005609$
                // - Hm? Who are you?
                switch (selection) {
                    // $script:1227015507005610$
                    // - $npcName:11001396[gender:1]$ wants this slab translated.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1227015507005611$
                // - Oh, yes, I remember her. Clever girl. It didn't even occur to her that I might not be able to translate this.
                switch (selection) {
                    // $script:1227015507005612$
                    // - You can't do it?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1227015507005613$
                // - I didn't say that! Child's play, mere child's play. Now be quiet while I work...
                return 42;
            case (42, 1):
                // $script:1227015507005614$
                // - Yes... Mm-hmm... Now, that is interesting.
                switch (selection) {
                    // $script:1227015507005615$
                    // - What is?!
                    case 0:
                        return 43;
                }
                return -1;
            case (43, 0):
                // $script:1227015507005616$
                // - Be quiet, you! Your jabbering is distracting.
                switch (selection) {
                    // $script:1227015507005617$
                    // - (Make an exaggerated lip-zipping motion.)
                    case 0:
                        return 44;
                }
                return -1;
            case (44, 0):
                // $script:1227015507005618$
                // - Yes, I see. This will be quite helpful... I've got something for you. Wait just a while longer. 
                switch (selection) {
                    // $script:1227015507005619$
                    // - (Wait several moments.)
                    case 0:
                        return 45;
                }
                return -1;
            case (45, 0):
                // $script:1227015507005620$
                // - If I do this, then... Is the formula off? Then I should try this, and...
                return 45;
            case (45, 1):
                // $script:1227015507005621$
                // - It is done! I don't know who made this slab, but it contained the answer to a new formula I've been trying to perfect.
                return 45;
            case (45, 2):
                // $script:1227015507005622$
                // - This record describes a method for stimulating the nerves and triggering a transformation in the body. I reverse-engineered the method to create a restorative tincture!
                switch (selection) {
                    // $script:1227015507005623$
                    // - Yes, and?
                    case 0:
                        return 46;
                }
                return -1;
            case (46, 0):
                // $script:1227015507005624$
                // - So impertinent! I was just getting to the good part. In short...
                return 46;
            case (46, 1):
                // $script:1227015507005625$
                // - I've created a potion that can alleviate the ailments that $npcName:11001396[gender:1]$ told me about. Note that I am being most humble here. When I say alleviate, I mean completely cure.
                switch (selection) {
                    // $script:1227015507005626$
                    // - Thank you.
                    case 0:
                        // TODO: goto 47
                        // TODO: gotoFail 48
                        return -1;
                }
                return -1;
            case (47, 0):
                // functionID=1 openTalkReward=True 
                // $script:1227015507005627$
                // - Take this to $npcName:11001396[gender:1]$. And tell her she's welcome.
                return -1;
            case (48, 0):
                // $script:1230110007005751$
                // - I don't think you have enough space in your bag. Lighten your load first.
                return -1;
            case (50, 0):
                // $script:1227033507005628$
                // - Is there anything else you need?
                switch (selection) {
                    // $script:1227033507005629$
                    // - No.
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:1227033507005630$
                // - Good, good. You may leave.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.SelectableDistractor,
            (43, 0) => NpcTalkButton.SelectableDistractor,
            (44, 0) => NpcTalkButton.SelectableDistractor,
            (45, 0) => NpcTalkButton.Next,
            (45, 1) => NpcTalkButton.Next,
            (45, 2) => NpcTalkButton.SelectableDistractor,
            (46, 0) => NpcTalkButton.Next,
            (46, 1) => NpcTalkButton.SelectableDistractor,
            (47, 0) => NpcTalkButton.Close,
            (48, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
