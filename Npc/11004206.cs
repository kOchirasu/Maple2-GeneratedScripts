using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004206: Dodo
/// </summary>
public class _11004206 : NpcScript {
    internal _11004206(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0803202415009085$ 
                // - Mushrooms make mistakes, too...
                return true;
            case 10:
                // $script:0803202415009086$ 
                // - I don't feel like chatting today...
                return true;
            default:
                return true;
        }
    }
}
