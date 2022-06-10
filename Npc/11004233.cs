using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004233: Pemberton
/// </summary>
public class _11004233 : NpcScript {
    internal _11004233(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010916$ 
                // - You've protected the lady from harm once again. I'm in your debt. 
                return true;
            case 10:
                // $script:0809223207010917$ 
                // - You've protected the lady from harm once again. I'm in your debt. 
                // $script:0809223207010918$ 
                // - The lady's happiness is my happiness. Please accept my thanks on her behalf. 
                return true;
            default:
                return true;
        }
    }
}
