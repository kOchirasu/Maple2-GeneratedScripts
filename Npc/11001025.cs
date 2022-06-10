using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001025: Eve
/// </summary>
public class _11001025 : NpcScript {
    internal _11001025(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003479$ 
                // - Ah... 
                return true;
            case 30:
                // $script:0831180407003482$ 
                // - It's not over until we catch $npcName:11000044[gender:0]$. 
                return true;
            default:
                return true;
        }
    }
}
