using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001841: Joddy
/// </summary>
public class _11001841 : NpcScript {
    internal _11001841(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1020165907007306$ 
                // - Ohhh... Ugh... I'm okay... 
                return true;
            case 30:
                // $script:1020165907007307$ 
                // - Aw man. I really don't think that went super great. Why can't I be more like you? 
                switch (selection) {
                    // $script:1111015907007384$
                    // - Maybe you need to take a break.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1020165907007308$ 
                // - Jeez, you think so? See, here I was thinking I gotta train harder. Otherwise, I'll never get strong enough to help you... 
                return true;
            default:
                return true;
        }
    }
}
