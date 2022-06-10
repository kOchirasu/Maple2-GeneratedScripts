using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004515: Mannstad Driver
/// </summary>
public class _11004515 : NpcScript {
    internal _11004515(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012475$ 
                // - We don't have enough fuel for our cars. We don't have enough ammo for our weapons. We just don't have enough...
                return true;
            case 10:
                // $script:1228182607012476$ 
                // - We don't have enough fuel for our cars. We don't have enough ammo for our weapons. We just don't have enough...
                // $script:1228182607012477$ 
                // - Hey, you aren't carrying any aetherine on you, are you? Ugh, as if it'd just fall into our laps like that...
                return true;
            default:
                return true;
        }
    }
}
