using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000705: Moya
/// </summary>
public class _11000705 : NpcScript {
    internal _11000705(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002837$ 
                // - What? If you have something to say, say it. 
                return true;
            case 30:
                // $script:0831180407002840$ 
                // - What? Do you have business with me? 
                return true;
            default:
                return true;
        }
    }
}
