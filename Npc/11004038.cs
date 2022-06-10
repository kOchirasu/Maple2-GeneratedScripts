using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004038: Ishura
/// </summary>
public class _11004038 : NpcScript {
    internal _11004038(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010061$ 
                // - Ah, you're here. It's thanks to you that we were all able to find common ground and work as one. Terrun Calibre will do whatever it can to help you with the matter of Madrakan.
                return true;
            case 20:
                // $script:0614185307010062$ 
                // - Ah, you're here. It's thanks to you that we were all able to find common ground and work as one. Terrun Calibre will do whatever it can to help you with the matter of Madrakan.
                return true;
            default:
                return true;
        }
    }
}
