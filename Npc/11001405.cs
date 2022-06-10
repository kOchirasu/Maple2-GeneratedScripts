using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001405: Bomar
/// </summary>
public class _11001405 : NpcScript {
    internal _11001405(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217025507005337$ 
                // - Sigh...
                return true;
            case 40:
                // $script:1217025507005341$ 
                // - P-please don't talk to me. I d-don't know anything!
                return true;
            default:
                return true;
        }
    }
}
