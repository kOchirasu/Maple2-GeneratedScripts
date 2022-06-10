using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003520: Duckling
/// </summary>
public class _11003520 : NpcScript {
    internal _11003520(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009021$ 
                // - ...
                return true;
            case 30:
                // $script:0816160115009024$ 
                // - ...
                return true;
            case 40:
                // $script:0816160115009025$ 
                // - Quack...?
                return true;
            default:
                return true;
        }
    }
}
