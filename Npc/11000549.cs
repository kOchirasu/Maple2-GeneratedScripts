using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000549: Tau
/// </summary>
public class _11000549 : NpcScript {
    internal _11000549(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002328$ 
                // - What?
                return true;
            case 30:
                // $script:0831180407002331$ 
                // - Is today some kind of holiday? Why is everyone so busy? I think I've met more people today than in my entire life.
                return true;
            default:
                return true;
        }
    }
}
