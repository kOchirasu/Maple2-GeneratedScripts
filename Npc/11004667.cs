using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004667: NPCNAME_11004667_NAME:[F]Event
/// </summary>
public class _11004667 : NpcScript {
    internal _11004667(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014958$ 
                // - SCRIPTNPCNAM_0603204607014958_NAME:[F]Event
                return true;
            case 30:
                // $script:0603204607014959$ 
                // - SCRIPTNPCNAM_0603204607014959_NAME:[F]Event
                // $script:0613033007014994$ 
                // - SCRIPTNPCNAM_0613033007014994_NAME:[F]Event
                return true;
            default:
                return true;
        }
    }
}
