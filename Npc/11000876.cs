using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000876: Belhi
/// </summary>
public class _11000876 : NpcScript {
    internal _11000876(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003184$ 
                // - Do you know how the fairfolk greet each other?
                return true;
            case 20:
                // $script:0831180407003186$ 
                // - Forests are the cradle of life for woodland creatures like us fairfolk. If they get cut down, we'll fall with them.
                return true;
            default:
                return true;
        }
    }
}
