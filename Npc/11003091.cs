using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003091: Orde
/// </summary>
public class _11003091 : NpcScript {
    internal _11003091(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0207122607007936$ 
                // - $MyPCName$, you're here! 
                return true;
            case 10:
                // $script:0207122607007937$ 
                // - I've learned so much about the world thanks to you, $MyPCName$. Thank you so much. 
                return true;
            default:
                return true;
        }
    }
}
