using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004673: NPCNAME_11004673_NAME:[F]Event
/// </summary>
public class _11004673 : NpcScript {
    internal _11004673(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014976$ 
                // - SCRIPTNPCNAM_0603204607014976_NAME:[F]Event 
                return true;
            case 30:
                // $script:0603204607014977$ 
                // - SCRIPTNPCNAM_0603204607014977_NAME:[F]Event 
                switch (selection) {
                    // $script:0613033007015021$
                    // - SCRIPTNPCNAM_0613033007015021_NAME:[F]Event
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0613033007015022$ 
                // - SCRIPTNPCNAM_0613033007015022_NAME:[F]Event 
                switch (selection) {
                    // $script:0613033007015023$
                    // - SCRIPTNPCNAM_0613033007015023_NAME:[F]Event
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0613033007015024$ 
                // - SCRIPTNPCNAM_0613033007015024_NAME:[F]Event 
                switch (selection) {
                    // $script:0613033007015025$
                    // - SCRIPTNPCNAM_0613033007015025_NAME:[F]Event
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0613033007015026$ 
                // - SCRIPTNPCNAM_0613033007015026_NAME:[F]Event 
                return true;
            default:
                return true;
        }
    }
}
