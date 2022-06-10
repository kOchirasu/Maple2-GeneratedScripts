using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004671: NPCNAME_11004671_NAME:[F]Event
/// </summary>
public class _11004671 : NpcScript {
    internal _11004671(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014970$ 
                // - SCRIPTNPCNAM_0603204607014970_NAME:[F]Event
                return true;
            case 30:
                // $script:0613033007015010$ 
                // - SCRIPTNPCNAM_0613033007015010_NAME:[F]Event
                // $script:0613033007015011$ 
                // - SCRIPTNPCNAM_0613033007015011_NAME:[F]Event
                // $script:0613033007015012$ 
                // - SCRIPTNPCNAM_0613033007015012_NAME:[F]Event
                return true;
            default:
                return true;
        }
    }
}
