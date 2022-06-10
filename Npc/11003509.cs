using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003509: Troe
/// </summary>
public class _11003509 : NpcScript {
    internal _11003509(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009014$ 
                // - Ah... Hello...?
                return true;
            case 30:
                // $script:0816160115009015$ 
                // - Ah... Hello...? I want to make some monster friends...
                return true;
            default:
                return true;
        }
    }
}
