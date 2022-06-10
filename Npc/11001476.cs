using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001476: Wei Hong
/// </summary>
public class _11001476 : NpcScript {
    internal _11001476(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228113207005714$ 
                // - Betrayal is the quickest path to death.
                return true;
            case 20:
                // $script:1228113207005716$ 
                // - You're better than I thought. I never forget a debt... or a grudge. $MyPCName$...
                return true;
            default:
                return true;
        }
    }
}
