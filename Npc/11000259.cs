using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000259: Dark Wind Agent
/// </summary>
public class _11000259 : NpcScript {
    internal _11000259(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001069$ 
                // - What seems to be the problem? 
                return true;
            case 10:
                // $script:0831180407001070$ 
                // - I'd keep a low profile if I were you. 
                return true;
            case 20:
                // $script:0831180407001071$ 
                // - It's going to be tough, but we have to comb through the records for clues. We can't let them catch us off guard again. 
                return true;
            default:
                return true;
        }
    }
}
