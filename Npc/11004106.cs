using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004106: Beatrice
/// </summary>
public class _11004106 : NpcScript {
    internal _11004106(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010453$ 
                // - Welcome, $MyPCName$, my soulbond.
                return true;
            case 10:
                // $script:0720125407010454$ 
                // - $MyPCName$, my kin, you've come.
                return true;
            default:
                return true;
        }
    }
}
