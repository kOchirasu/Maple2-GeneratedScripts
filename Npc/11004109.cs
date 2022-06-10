using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004109: Blackeye
/// </summary>
public class _11004109 : NpcScript {
    internal _11004109(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010459$ 
                // - We'll always do our best.
                return true;
            case 10:
                // $script:0720125407010460$ 
                // - I'll do whatever I can to aid you.
                return true;
            default:
                return true;
        }
    }
}
