using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003348: Ralph's Lackey
/// </summary>
public class _11003348 : NpcScript {
    internal _11003348(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0517164307008496$ 
                // - This place has really transformed, thanks to you!
                return true;
            case 20:
                // $script:0517164307008498$ 
                // - We're all serious now. You just wait and see. The boss'll make you pay!
                return true;
            default:
                return true;
        }
    }
}
