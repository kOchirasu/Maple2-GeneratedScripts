using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001915: Lennon
/// </summary>
public class _11001915 : NpcScript {
    internal _11001915(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1116181807007416$ 
                // - I'm glad you're here.
                return true;
            case 20:
                // $script:1116181807007418$ 
                // - I can't believe it...
                return true;
            default:
                return true;
        }
    }
}
