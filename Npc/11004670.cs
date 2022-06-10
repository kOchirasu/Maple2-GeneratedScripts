using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004670: NPCNAME_11004670_NAME:[F]Event
/// </summary>
public class _11004670 : NpcScript {
    internal _11004670(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0603204607014967$ 
                // - SCRIPTNPCNAM_0603204607014967_NAME:[F]Event 
                return true;
            case 30:
                // $script:0613033007015007$ 
                // - SCRIPTNPCNAM_0613033007015007_NAME:[F]Event 
                // $script:0613033007015008$ 
                // - SCRIPTNPCNAM_0613033007015008_NAME:[F]Event 
                // $script:0613033007015009$ 
                // - SCRIPTNPCNAM_0613033007015009_NAME:[F]Event 
                return true;
            default:
                return true;
        }
    }
}
