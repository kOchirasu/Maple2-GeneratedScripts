using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000367: Skittle
/// </summary>
public class _11000367 : NpcScript {
    internal _11000367(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001514$ 
                // - What is it, meow?
                return true;
            case 20:
                // $script:0831180407001516$ 
                // - Do you believe in love at first sight, meow? I do! Look at the cat next to me. Isn't she beautiful? Me-ow!
                return true;
            default:
                return true;
        }
    }
}
