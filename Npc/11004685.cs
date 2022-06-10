using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004685: NPCNAME_11004685_NAME:[F]Event
/// </summary>
public class _11004685 : NpcScript {
    internal _11004685(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0617094407015030$ 
                // - SCRIPTNPCNAM_0617094407015030_NAME:[F]Event
                return true;
            case 30:
                // $script:0617094407015033$ 
                // - SCRIPTNPCNAM_0617094407015033_NAME:[F]Event
                switch (selection) {
                    // $script:0617094407015034$
                    // - SCRIPTNPCNAM_0617094407015034_NAME:[F]Event
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0617094407015035$ 
                // - SCRIPTNPCNAM_0617094407015035_NAME:[F]Event
                switch (selection) {
                    // $script:0617095907015039$
                    // - SCRIPTNPCNAM_0617095907015039_NAME:[F]Event
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0617094407015036$ 
                // - SCRIPTNPCNAM_0617094407015036_NAME:[F]Event
                // $script:0617095907015038$ 
                // - SCRIPTNPCNAM_0617095907015038_NAME:[F]Event
                return true;
            default:
                return true;
        }
    }
}
