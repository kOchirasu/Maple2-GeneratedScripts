using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000804: Liam
/// </summary>
public class _11000804 : NpcScript {
    internal _11000804(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002962$ 
                // - Do you have something to say to me? 
                return true;
            case 30:
                // $script:0831180407002965$ 
                // - $MyPCName$, never let your guard down. Not for an instant. You're a long way from Maple World. 
                return true;
            default:
                return true;
        }
    }
}
