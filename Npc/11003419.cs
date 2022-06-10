using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003419: Namid
/// </summary>
public class _11003419 : NpcScript {
    internal _11003419(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008625$ 
                // - 
                return true;
            case 10:
                // $script:0706160807008626$ 
                // - 
                return true;
            default:
                return true;
        }
    }
}
