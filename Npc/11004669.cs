using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004669: NPCNAME_11004669_NAME:[F]Event
/// </summary>
public class _11004669 : NpcScript {
    internal _11004669(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014964$ 
                // - SCRIPTNPCNAM_0603204607014964_NAME:[F]Event
                return true;
            case 30:
                // $script:0603204607014966$ 
                // - SCRIPTNPCNAM_0603204607014966_NAME:[F]Event
                // $script:0613033007015002$ 
                // - SCRIPTNPCNAM_0613033007015002_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007015003$
                    // - SCRIPTNPCNAM_0613033007015003_NAME:[F]Event
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0613033007015004$
                    // - SCRIPTNPCNAM_0613033007015004_NAME:[F]Event
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0613033007015005$ 
                // - SCRIPTNPCNAM_0613033007015005_NAME:[F]Event
                return true;
            case 32:
                // $script:0613033007015006$ 
                // - SCRIPTNPCNAM_0613033007015006_NAME:[F]Event
                return true;
            default:
                return true;
        }
    }
}
