using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000810: Amy
/// </summary>
public class _11000810 : NpcScript {
    internal _11000810(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002984$ 
                // - Sigh... 
                return true;
            case 20:
                // $script:0831180407002986$ 
                // - $MyPCName$, I don't know how to repay you and the Lumina Liberation Army for this. Thank you so much. 
                return true;
            default:
                return true;
        }
    }
}
