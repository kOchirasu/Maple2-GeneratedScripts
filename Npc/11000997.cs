using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000997: Ravel
/// </summary>
public class _11000997 : NpcScript {
    internal _11000997(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003425$ 
                // - Ring, ring! Out of the way!
                return true;
            case 30:
                // $script:0831180407003428$ 
                // - Whew, that was close. You almost startled me right off the clock!
                return true;
            default:
                return true;
        }
    }
}
