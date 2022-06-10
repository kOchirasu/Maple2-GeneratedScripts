using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000710: Hudru
/// </summary>
public class _11000710 : NpcScript {
    internal _11000710(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002843$ 
                // - Did you call me?
                return true;
            case 30:
                // $script:0831180407002846$ 
                // - I think I can cross this bridge if I don't look down. But... what if I lose my footing because I can't see where I'm going?
                return true;
            default:
                return true;
        }
    }
}
