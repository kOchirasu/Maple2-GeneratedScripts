using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003848: Condor
/// </summary>
public class _11003848 : NpcScript {
    internal _11003848(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0117175907009811$ 
                // - Let's get to business. 
                return true;
            case 10:
                // $script:0117175907009812$ 
                // - In my day, we protected the world just fine without these fancy gadgets. 
                return true;
            default:
                return true;
        }
    }
}
