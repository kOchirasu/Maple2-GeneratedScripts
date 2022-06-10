using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003094: Blackeye
/// </summary>
public class _11003094 : NpcScript {
    internal _11003094(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0207122607007940$ 
                // - Ahh it's you, $MyPCName$.
                return true;
            case 10:
                // $script:0207122607007941$ 
                // - Dark Wind is changing. It's not the same organization you once knew.
                return true;
            default:
                return true;
        }
    }
}
