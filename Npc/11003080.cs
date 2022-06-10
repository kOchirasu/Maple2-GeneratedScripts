using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003080: Columbo
/// </summary>
public class _11003080 : NpcScript {
    internal _11003080(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0113143107007757$ 
                // - Ahhh, I want to get better soon so I can go on adventures again!
                return true;
            case 30:
                // $script:0113143107007760$ 
                // - How soon until I can sail again? Cough, cough! I want to be well so I can set off to find the wonders of the world.
                return true;
            case 40:
                // $script:0113143107007761$ 
                // - $MyPCName$, thank you for telling me about your adventures! I hope I can get better so I can have my own adventures, too.
                return true;
            default:
                return true;
        }
    }
}
