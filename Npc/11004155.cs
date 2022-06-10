using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004155: Fufu
/// </summary>
public class _11004155 : NpcScript {
    internal _11004155(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010581$ 
                // - Ugh! 
                return true;
            case 10:
                // $script:0806025707010582$ 
                // - Ugh! I'm all stiff from standing around all day. I can't wait to get off work. 
                return true;
            default:
                return true;
        }
    }
}
