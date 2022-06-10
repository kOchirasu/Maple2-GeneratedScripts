using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004345: Evelyn
/// </summary>
public class _11004345 : NpcScript {
    internal _11004345(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011747$ 
                // - Why can't we just have a normal celebration? This is ridiculous!
                return true;
            case 10:
                // $script:1109213607011748$ 
                // - Have you seen my family? I... really miss them right now.
                return true;
            default:
                return true;
        }
    }
}
