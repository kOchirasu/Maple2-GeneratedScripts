using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000362: Stan
/// </summary>
public class _11000362 : NpcScript {
    internal _11000362(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001502$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0831180407001505$ 
                // - Not many people know this, but cooked $npcName:21000059$ can be incredible. I'm getting ready to sell $npcName:21000059$ dishes made from my own secret recipe.
                return true;
            default:
                return true;
        }
    }
}
