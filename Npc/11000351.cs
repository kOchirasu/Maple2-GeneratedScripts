using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000351: Mirror
/// </summary>
public class _11000351 : NpcScript {
    internal _11000351(INpcScriptContext context) : base(context) {
        Id = 0;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000437$ functionID=1 
                // - Just look at that gorgeous reflection! Can you believe that's you? 
                return true;
            default:
                return true;
        }
    }
}
