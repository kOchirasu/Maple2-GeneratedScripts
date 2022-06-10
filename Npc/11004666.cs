using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004666: NPCNAME_11004666_NAME:[F]Event
/// </summary>
public class _11004666 : NpcScript {
    internal _11004666(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014955$ 
                // - SCRIPTNPCNAM_0603204607014955_NAME:[F]Event
                return true;
            case 30:
                // $script:0603204607014956$ 
                // - SCRIPTNPCNAM_0603204607014956_NAME:[F]Event
                return true;
            default:
                return true;
        }
    }
}
