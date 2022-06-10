using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000431: Ronin
/// </summary>
public class _11000431 : NpcScript {
    internal _11000431(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;41
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001797$ 
                // - I'd better rest while I can!
                return true;
            case 30:
                // $script:0831180407001799$ 
                // - I've heard stories of treasure chests under the sea, but I've never seen one. How about you, $MyPCName$?
                return true;
            case 40:
                // $script:0831180407001800$ 
                // - Yes?
                switch (selection) {
                    // $script:0831180407001801$
                    // - $npcName:11000362[gender:0]$'s special...
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001802$ 
                // - Go away.
                return true;
            default:
                return true;
        }
    }
}
