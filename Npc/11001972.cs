using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001972: Blackeye
/// </summary>
public class _11001972 : NpcScript {
    internal _11001972(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0625222407010369$ 
                // - We must harden our resolve.
                return true;
            case 10:
                // $script:0625222407010370$ 
                // - We must harden our resolve.
                return true;
            default:
                return true;
        }
    }
}
