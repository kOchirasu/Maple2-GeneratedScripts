using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000500: Flat Rock
/// </summary>
public class _11000500 : NpcScript {
    internal _11000500(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002177$ 
                // - Not just anyone can sit on me. 
                return true;
            case 10:
                // $script:0831180407002178$ 
                // - You kick me, and I'm not going to be the one in pain. 
                // $script:0626205807010385$ 
                // - You better leave while I'm still in a good mood. I'm no ordinary rock. 
                return true;
            default:
                return true;
        }
    }
}
