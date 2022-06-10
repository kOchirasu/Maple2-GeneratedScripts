using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000962: Rhys
/// </summary>
public class _11000962 : NpcScript {
    internal _11000962(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003342$ 
                // - Things aren't as good as they used to be. Ahh well. What did you want?
                return true;
            case 20:
                // $script:0831180407003344$ 
                // - The Green Hoods never surrender, no matter how bad the situation is. 
                return true;
            default:
                return true;
        }
    }
}
