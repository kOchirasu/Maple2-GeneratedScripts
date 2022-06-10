using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004404: Oska
/// </summary>
public class _11004404 : NpcScript {
    internal _11004404(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1113161307011825$ 
                // - How may I help you?
                return true;
            case 10:
                // $script:1113161307011826$ 
                // - Worry not. The Green Hoods watch over this place.
                return true;
            default:
                return true;
        }
    }
}
