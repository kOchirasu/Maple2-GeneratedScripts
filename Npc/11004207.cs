using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004207: Koomkoom
/// </summary>
public class _11004207 : NpcScript {
    internal _11004207(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0803202415009087$ 
                // - Heheh, want to play with me? 
                return true;
            case 10:
                // $script:0803202415009088$ 
                // - Heheheh... I've got something real fun cooked up for those humans.  
                return true;
            default:
                return true;
        }
    }
}
