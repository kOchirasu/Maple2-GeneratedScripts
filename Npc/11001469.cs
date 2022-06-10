using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001469: Arl
/// </summary>
public class _11001469 : NpcScript {
    internal _11001469(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1223040807005536$ 
                // - This must be the place. 
                return true;
            case 30:
                // $script:1223040807005539$ 
                // - Shhh! Don't tell my mom I'm here! 
                return true;
            default:
                return true;
        }
    }
}
