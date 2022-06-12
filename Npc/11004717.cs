using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004717: Karkamelle
/// </summary>
public class _11004717 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0828194707015119$
    // - Oh oh, what have I gotten myself into in my old age? 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0828194607015110$
                // - Guard the cauldron. Deal with customers. Deal with customers. Guard the cauldron... 
                return 30;
            case (30, 1):
                // $script:0828194607015111$
                // - $npcName:11000304[gender:1]$, that dratted old bat! Well, at least I don't have to worry about getting lonely...
                switch (selection) {
                    // $script:0828194607015112$
                    // - Who's $npcName:11000304[gender:1]$?
                    case 0:
                        return 31;
                    // $script:0828194607015113$
                    // - What's with the cauldron?
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0828194607015114$
                // - She's only her exalted fancy-warts, the grand bossy-britches of all the witches! Oh, we were friends once, back in the day. But I wasted my time when she was mastering her grimoires, and... Well, no point regretting it now!
                switch (selection) {
                    // $script:0828194607015115$
                    // - What happened?
                    case 0:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0828194607015116$
                // - This old thing? You see, once a year, a deep shadow covers the world, and all the demons and spirits rise from the netherworld to cavort and caper in the mortal realm. I think you humans call it Halloween. 
                return 32;
            case (32, 1):
                // $script:0828194607015117$
                // - Anyway, this is the one time of the year when we can get all the ingredients for witch stew! And we witches, we've got to have our witch stew. It gives our magic that extra little OOMPH that makes us so wonderful.
                return -1;
            case (33, 0):
                // $script:0828194607015118$
                // - It's a long story. And an ugly one! Instead of nosing into my painful memories, why don't you help me with this cauldron?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
