using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001365: Dunba
/// </summary>
public class _11001365 : NpcScript {
    internal _11001365(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215222907005048$ 
                // - Sigh... I'm so glad that everyone's safe.
                return true;
            case 10:
                // $script:1230171207005755$ 
                // - I hope the Blackstars leave me alone this time... I don't want a rematch with Vasara Chen...
                return true;
            default:
                return true;
        }
    }
}
