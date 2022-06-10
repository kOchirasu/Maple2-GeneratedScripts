using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004672: NPCNAME_11004672_NAME:[F]Event
/// </summary>
public class _11004672 : NpcScript {
    internal _11004672(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014973$ 
                // - SCRIPTNPCNAM_0603204607014973_NAME:[F]Event 
                return true;
            case 30:
                // $script:0613034407015027$ 
                // - SCRIPTNPCNAM_0613034407015027_NAME:[F]Event 
                switch (selection) {
                    // $script:0613034407015028$
                    // - SCRIPTNPCNAM_0613034407015028_NAME:[F]Event
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0613033007015015$ 
                // - SCRIPTNPCNAM_0613033007015015_NAME:[F]Event 
                switch (selection) {
                    // $script:0613034407015029$
                    // - SCRIPTNPCNAM_0613034407015029_NAME:[F]Event
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0613033007015017$
                    // - SCRIPTNPCNAM_0613033007015017_NAME:[F]Event
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0613033007015018$ 
                // - SCRIPTNPCNAM_0613033007015018_NAME:[F]Event 
                return true;
            case 33:
                // $script:0613033007015019$ 
                // - SCRIPTNPCNAM_0613033007015019_NAME:[F]Event 
                return true;
            default:
                return true;
        }
    }
}
