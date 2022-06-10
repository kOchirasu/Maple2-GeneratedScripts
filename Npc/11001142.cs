using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001142: Meldy
/// </summary>
public class _11001142 : NpcScript {
    internal _11001142(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0914192507003920$ 
                // - Uh. Hi. 
                return true;
            case 30:
                // $script:0914192507003923$ 
                // - First the monsters start taking over the forest, and now my friends are all leaving in droves... Hmph. What do I care? I like being alone, anyway! 
                return true;
            default:
                return true;
        }
    }
}
