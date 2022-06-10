using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004717: Karkamelle
/// </summary>
public class _11004717 : NpcScript {
    internal _11004717(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0828194707015119$ 
                // - Oh oh, what have I gotten myself into in my old age? 
                return true;
            case 30:
                // $script:0828194607015110$ 
                // - Guard the cauldron. Deal with customers. Deal with customers. Guard the cauldron... 
                // $script:0828194607015111$ 
                // - $npcName:11000304[gender:1]$, that dratted old bat! Well, at least I don't have to worry about getting lonely...
                switch (selection) {
                    // $script:0828194607015112$
                    // - Who's $npcName:11000304[gender:1]$?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0828194607015113$
                    // - What's with the cauldron?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0828194607015114$ 
                // - She's only her exalted fancy-warts, the grand bossy-britches of all the witches! Oh, we were friends once, back in the day. But I wasted my time when she was mastering her grimoires, and... Well, no point regretting it now!
                switch (selection) {
                    // $script:0828194607015115$
                    // - What happened?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0828194607015116$ 
                // - This old thing? You see, once a year, a deep shadow covers the world, and all the demons and spirits rise from the netherworld to cavort and caper in the mortal realm. I think you humans call it Halloween. 
                // $script:0828194607015117$ 
                // - Anyway, this is the one time of the year when we can get all the ingredients for witch stew! And we witches, we've got to have our witch stew. It gives our magic that extra little OOMPH that makes us so wonderful.
                return true;
            case 33:
                // $script:0828194607015118$ 
                // - It's a long story. And an ugly one! Instead of nosing into my painful memories, why don't you help me with this cauldron?
                return true;
            default:
                return true;
        }
    }
}
