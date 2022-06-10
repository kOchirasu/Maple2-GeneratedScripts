using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004668: NPCNAME_11004668_NAME:[F]Event
/// </summary>
public class _11004668 : NpcScript {
    internal _11004668(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014961$ 
                // - SCRIPTNPCNAM_0603204607014961_NAME:[F]Event
                return true;
            case 30:
                // $script:0613033007014996$ 
                // - SCRIPTNPCNAM_0613033007014996_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007014997$
                    // - SCRIPTNPCNAM_0613033007014997_NAME:[F]Event
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0613033007014998$ 
                // - SCRIPTNPCNAM_0613033007014998_NAME:[F]Event
                switch (selection) {
                    // $script:0613033007014999$
                    // - SCRIPTNPCNAM_0613033007014999_NAME:[F]Event
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0603204607014962$ 
                // - SCRIPTNPCNAM_0603204607014962_NAME:[F]Event
                return true;
            default:
                return true;
        }
    }
}
