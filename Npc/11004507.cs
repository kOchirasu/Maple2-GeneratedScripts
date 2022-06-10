using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004507: Mannstad Sentry
/// </summary>
public class _11004507 : NpcScript {
    internal _11004507(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012441$ 
                // - I haven't seen you before. You that outlander everyone's talking about?
                return true;
            case 10:
                // $script:1228182607012442$ 
                // - I haven't seen you before. You that outlander everyone's talking about?
                // $script:1228182607012443$ 
                // - Anyway, watch yourself out there. Our enemy won't hesitate to shoot you down.
                return true;
            default:
                return true;
        }
    }
}
