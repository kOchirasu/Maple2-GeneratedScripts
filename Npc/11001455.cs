using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001455: Melatina
/// </summary>
public class _11001455 : NpcScript {
    internal _11001455(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1222171407005450$ 
                // - Hello. 
                return true;
            case 30:
                // $script:1222171407005453$ 
                // - On $map:02010022$, hard work is considered a sin. Got nothing to do? Then soak in the majesty that surrounds us! 
                return true;
            default:
                return true;
        }
    }
}
