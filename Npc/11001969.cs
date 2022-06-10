using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001969: Ereve
/// </summary>
public class _11001969 : NpcScript {
    internal _11001969(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0201161807007915$ 
                // - Welcome, $MyPCName$. 
                return true;
            case 10:
                // $script:0201161807007916$ 
                // - $MyPCName$, I'm looking forward to hearing more great stories of your heroism. 
                return true;
            default:
                return true;
        }
    }
}
