using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000444: Columbo
/// </summary>
public class _11000444 : NpcScript {
    internal _11000444(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001867$ 
                // - Ah... I want to get better soon, so I can go on adventures again.
                return true;
            case 30:
                // $script:0831180407001870$ 
                // - When can I sail again? Cough, cough! My leg had better heal quickly so I can get back to finding that pirate island.
                return true;
            case 60:
                // $script:0831180407001871$ 
                // - The sea may look calm from here, but it can destroy you in an instant.
                return true;
            default:
                return true;
        }
    }
}
