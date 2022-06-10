using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004033: Orde
/// </summary>
public class _11004033 : NpcScript {
    internal _11004033(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010051$ 
                // - Ugh, I hate field duty... 
                return true;
            case 20:
                // $script:0614185307010052$ 
                // - It's dangerous outside the blanket, $MyPCName$. 
                return true;
            default:
                return true;
        }
    }
}
