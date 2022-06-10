using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004358: Evelyn
/// </summary>
public class _11004358 : NpcScript {
    internal _11004358(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011769$ 
                // - Oh look, $MyPCName$. Snow!
                return true;
            case 10:
                // $script:1109213607011770$ 
                // - I always love snow for the holidays.
                return true;
            default:
                return true;
        }
    }
}
