using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004524: Gentle Soldieretto
/// </summary>
public class _11004524 : NpcScript {
    internal _11004524(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0103163407012503$ 
                // - Beeep... Beeep...
                return true;
            case 10:
                // $script:0103163407012504$ 
                // - You appear malnourished.
                // $script:0103163407012505$ 
                // - Feel free to refuel at our aetherine station.
                return true;
            default:
                return true;
        }
    }
}
