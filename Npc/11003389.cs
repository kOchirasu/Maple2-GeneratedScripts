using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003389: Namid
/// </summary>
public class _11003389 : NpcScript {
    internal _11003389(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008583$ 
                // - 
                return true;
            case 10:
                // $script:0706160807008584$ 
                // - 
                return true;
            default:
                return true;
        }
    }
}
