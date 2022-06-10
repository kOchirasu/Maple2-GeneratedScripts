using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000837: Dennis
/// </summary>
public class _11000837 : NpcScript {
    internal _11000837(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003064$ 
                // - Shush, I'm on a mission right now. Please don't interrupt me. 
                return true;
            case 30:
                // $script:0831180407003067$ 
                // - Even the slipperiest suspect can't escape from me once I set my sights on them. 
                return true;
            default:
                return true;
        }
    }
}
