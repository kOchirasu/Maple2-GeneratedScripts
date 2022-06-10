using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000647: Prisoner 160920
/// </summary>
public class _11000647 : NpcScript {
    internal _11000647(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002646$ 
                // - Get me out of here... 
                return true;
            case 30:
                // $script:0831180407002650$ 
                // - What are you lookin' at? This ain't no zoo, and I ain't no animal! Ahhh, I hate alla you!
                return true;
            default:
                return true;
        }
    }
}
