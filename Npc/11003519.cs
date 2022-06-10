using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003519: Nimeisha
/// </summary>
public class _11003519 : NpcScript {
    internal _11003519(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0817044507008869$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0817044507008871$ 
                // - Can I help you?
                switch (selection) {
                    // $script:0817044507008872$
                    // - Tell me about the five auras.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0817044507008873$ 
                // - An aura has no physical form. It's intangible. Still, if you focus hard on one thing, you're bound to reach your peak.
                // $script:0817044507008874$ 
                // - When you focus one gathering one type of aura, you'll feel it build up. Once it's full, it can be placed in a bowl, like water.
                return true;
            default:
                return true;
        }
    }
}
