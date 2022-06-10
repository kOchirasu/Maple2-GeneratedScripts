using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000471: Vito
/// </summary>
public class _11000471 : NpcScript {
    internal _11000471(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002062$ 
                // - Ah, what is it? 
                return true;
            case 20:
                // $script:0831180407002064$ 
                // - I know height isn't everything, but I really don't like being shorter than most people...  
                return true;
            default:
                return true;
        }
    }
}
