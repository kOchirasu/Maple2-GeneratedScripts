using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004377: Snowleaf Fairfolk
/// </summary>
public class _11004377 : NpcScript {
    internal _11004377(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011791$ 
                // - Happy holidays!
                return true;
            case 10:
                // $script:1109213607011792$ 
                // - Happy holidays!
                return true;
            default:
                return true;
        }
    }
}
