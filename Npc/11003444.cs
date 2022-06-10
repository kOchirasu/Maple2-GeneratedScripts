using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003444: Besherel
/// </summary>
public class _11003444 : NpcScript {
    internal _11003444(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008692$ 
                // - If you want something, you'll have to pay the price.
                return true;
            case 10:
                // $script:0721142007008710$ 
                // - If you want something, you'll have to pay the price.
                return true;
            default:
                return true;
        }
    }
}
