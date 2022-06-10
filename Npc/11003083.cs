using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003083: Celine
/// </summary>
public class _11003083 : NpcScript {
    internal _11003083(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0113143107007770$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0113143107007771$ 
                // - $MyPCName$, I'm sorry you came all the way here for nothing.
                return true;
            default:
                return true;
        }
    }
}
