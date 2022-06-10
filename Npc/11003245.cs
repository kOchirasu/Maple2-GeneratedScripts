using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003245: Oska
/// </summary>
public class _11003245 : NpcScript {
    internal _11003245(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008150$ 
                // - No... $npcName:11000001[gender:0]$...
                return true;
            case 30:
                // $script:0403155707008151$ 
                // - Ah... $npcName:11000001[gender:0]$...
                return true;
            default:
                return true;
        }
    }
}
