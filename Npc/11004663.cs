using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004663: NPCNAME_11004663_NAME:[F]Event
/// </summary>
public class _11004663 : NpcScript {
    internal _11004663(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014946$ 
                // - SCRIPTNPCNAM_0603204607014946_NAME:[F]Event
                return true;
            case 30:
                // $script:0603204607014947$ 
                // - SCRIPTNPCNAM_0603204607014947_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007014979$
                    // - SCRIPTNPCNAM_0613033007014979_NAME:[F]Event
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0613033007014980$
                    // - SCRIPTNPCNAM_0613033007014980_NAME:[F]Event
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0613033007014981$ 
                // - SCRIPTNPCNAM_0613033007014981_NAME:[F]Event
                // $script:0613033007014982$ 
                // - SCRIPTNPCNAM_0613033007014982_NAME:[F]Event
                // $script:0613033007014983$ 
                // - SCRIPTNPCNAM_0613033007014983_NAME:[F]Event
                // $script:0613033007014984$ 
                // - SCRIPTNPCNAM_0613033007014984_NAME:[F]Event
                // $script:0613033007014985$ 
                // - SCRIPTNPCNAM_0613033007014985_NAME:[F]Event
                // $script:0613033007014986$ 
                // - SCRIPTNPCNAM_0613033007014986_NAME:[F]Event
                return true;
            case 32:
                // $script:0613033007014987$ 
                // - SCRIPTNPCNAM_0613033007014987_NAME:[F]Event
                // $script:0613033007014988$ 
                // - SCRIPTNPCNAM_0613033007014988_NAME:[F]Event
                // $script:0613033007014989$ 
                // - SCRIPTNPCNAM_0613033007014989_NAME:[F]Event
                return true;
            default:
                return true;
        }
    }
}
