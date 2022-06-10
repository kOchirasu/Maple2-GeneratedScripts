using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003785: Condor
/// </summary>
public class _11003785 : NpcScript {
    internal _11003785(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213192607009640$ 
                // - Let's get to business. 
                return true;
            case 10:
                // $script:1213192607009641$ 
                // - In my day, we protected the world just fine without these fancy gadgets. 
                return true;
            default:
                return true;
        }
    }
}
