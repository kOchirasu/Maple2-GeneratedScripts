using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004463: Safehold Guardsman
/// </summary>
public class _11004463 : NpcScript {
    internal _11004463(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012080$ 
                // - All... is... well!
                return true;
            case 10:
                // $script:1227192907012081$ 
                // - All... is... well!
                // $script:1227192907012082$ 
                // - I've been trying to get in this platoon for ages. They finally give me the transfer, and the whole platoon is shipped out to this crazy place. Man...
                switch (selection) {
                    // $script:1227192907012083$
                    // - Chin up, sad guard.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012084$ 
                // - Hearing those words from your mouth fills me with hope. Thank you, $MyPCName$! I'll fight my hardest!
                return true;
            default:
                return true;
        }
    }
}
