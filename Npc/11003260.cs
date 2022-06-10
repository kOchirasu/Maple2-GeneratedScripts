using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003260: Lian
/// </summary>
public class _11003260 : NpcScript {
    internal _11003260(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008196$ 
                // - Ah, $MyPCName$!
                return true;
            case 30:
                // $script:0403155707008197$ 
                // - Everyone's safe, thanks to you. I hope you won't mind if we call on your help again in the future.
                return true;
            default:
                return true;
        }
    }
}
