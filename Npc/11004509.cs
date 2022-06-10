using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004509: Mannstad Sentry
/// </summary>
public class _11004509 : NpcScript {
    internal _11004509(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012451$ 
                // - Look what we have here. It's about time they sent us some reinforcements.
                return true;
            case 10:
                // $script:1228182607012452$ 
                // - Look what we have here. It's about time they sent us some reinforcements.
                switch (selection) {
                    // $script:1228182607012453$
                    // - I'm not your reinforcements.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1228182607012454$ 
                // - Tch... Figures. We don't have the numbers to hold this position for right now. Y'know, give a leshy a gun and I'd let it stand guard. That's how desperate we are!
                return true;
            default:
                return true;
        }
    }
}
