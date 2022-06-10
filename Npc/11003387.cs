using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003387: Rolling Thunder
/// </summary>
public class _11003387 : NpcScript {
    internal _11003387(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0719181607008677$ 
                // - We've got to act fast!
                return true;
            case 10:
                // $script:0719181607008678$ 
                // - We've got to act fast!
                return true;
            default:
                return true;
        }
    }
}
