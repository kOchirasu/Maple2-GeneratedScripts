using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004103: Orde
/// </summary>
public class _11004103 : NpcScript {
    internal _11004103(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0704125907010388$ 
                // - Ugh, I hate field duty...
                return true;
            case 20:
                // $script:0704125907010389$ 
                // - It's dangerous outside the blanket, $MyPCName$.
                return true;
            default:
                return true;
        }
    }
}
