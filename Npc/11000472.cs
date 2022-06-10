using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000472: Tonk
/// </summary>
public class _11000472 : NpcScript {
    internal _11000472(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002065$ 
                // - Hmph. WHAT? 
                return true;
            case 20:
                // $script:0831180407002067$ 
                // - Real men aren't scared of spiders! They squash them flat as soon as they see them! 
                return true;
            case 30:
                // $script:0831180407002068$ 
                // - This place behind me is loaded with spiders. If you're in a hurry, you can squash them yourself. 
                return true;
            default:
                return true;
        }
    }
}
