using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000871: Tuner
/// </summary>
public class _11000871 : NpcScript {
    internal _11000871(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003148$ 
                // - Huh?
                return true;
            case 20:
                // $script:0831180407003150$ 
                // - $MyPCName$, would you like to know what's going on here? You look a little... bewildered.
                return true;
            default:
                return true;
        }
    }
}
