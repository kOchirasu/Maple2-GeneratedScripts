using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004665: NPCNAME_11004665_NAME:[F]Event
/// </summary>
public class _11004665 : NpcScript {
    internal _11004665(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014952$ 
                // - SCRIPTNPCNAM_0603204607014952_NAME:[F]Event 
                return true;
            case 30:
                // $script:0603204607014953$ 
                // - SCRIPTNPCNAM_0603204607014953_NAME:[F]Event 
                return true;
            default:
                return true;
        }
    }
}
