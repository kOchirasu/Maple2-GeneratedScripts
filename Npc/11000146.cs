using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000146: Andy
/// </summary>
public class _11000146 : NpcScript {
    internal _11000146(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000622$ 
                // - Oh, no...
                return true;
            case 30:
                // $script:0831180407000625$ 
                // - I'm getting tired of ending up in unfamiliar places!
                return true;
            case 40:
                // $script:0831180407000626$ 
                // - I want out of this jungle the first chance I get. I can't wait to go back home.
                return true;
            case 50:
                // $script:0831180407000627$ 
                // - Sigh, I'm tired of traveling through time. I always end up in places that I don't want to be
                return true;
            default:
                return true;
        }
    }
}
