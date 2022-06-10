using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001599: Allon
/// </summary>
public class _11001599 : NpcScript {
    internal _11001599(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006087$ 
                // - What brings you here?
                return true;
            case 10:
                // $script:0515180307006136$ 
                // - Everyone seems to be a little heated. Don't forget, this is official Expedition business.
                return true;
            default:
                return true;
        }
    }
}
