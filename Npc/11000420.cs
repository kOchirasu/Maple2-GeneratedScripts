using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000420: Moma
/// </summary>
public class _11000420 : NpcScript {
    internal _11000420(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 90;100
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001748$ 
                // - You got something to say? 
                return true;
            case 90:
                // $script:0831180407001754$ 
                // - Are you sightseeing? Head north to the condominium complex. The staff is nice, and it's really pretty around there. Just sayin'.
                return true;
            case 100:
                // $script:0831180407001755$ 
                // - $MyPCName$, do you like fish?
                switch (selection) {
                    // $script:0831180407001756$
                    // - Yep.
                    case 0:
                        Id = 101;
                        return false;
                    // $script:0831180407001757$
                    // - Nope.
                    case 1:
                        Id = 102;
                        return false;
                }
                return true;
            case 101:
                // $script:0831180407001758$ 
                // - Well $MyPCName$, you're more health-conscious than I thought. Fish is an excellent source of protein and other essential nutrients.
                return true;
            case 102:
                // $script:0831180407001759$ 
                // - Oh, you should eat fish regularly. I thought you knew that, $MyPCName$. Do you only eat red meat? It's too fatty. Eating fish helps you lose weight.
                return true;
            default:
                return true;
        }
    }
}
