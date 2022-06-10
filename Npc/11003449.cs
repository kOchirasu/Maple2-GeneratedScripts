using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003449: Namid
/// </summary>
public class _11003449 : NpcScript {
    internal _11003449(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008653$ 
                // -  
                return true;
            case 10:
                // $script:0706160807008654$ 
                // -  
                return true;
            default:
                return true;
        }
    }
}
