using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000590: Kazimar
/// </summary>
public class _11000590 : NpcScript {
    internal _11000590(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000849$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1121222006000850$ 
                // - When can I build my own house? 
                return true;
            default:
                return true;
        }
    }
}
