using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003087: Orde
/// </summary>
public class _11003087 : NpcScript {
    internal _11003087(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0207122607007928$ 
                // - Ugh, I hate field duty...
                return true;
            case 10:
                // $script:0207122607007929$ 
                // - It's dangerous outside the blanket, $MyPCName$.
                return true;
            default:
                return true;
        }
    }
}
