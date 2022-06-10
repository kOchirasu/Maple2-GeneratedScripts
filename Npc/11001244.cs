using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001244: Ishura
/// </summary>
public class _11001244 : NpcScript {
    internal _11001244(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1203181207004687$ 
                // - There's a lingering aura of runic magic... I must be close. 
                return true;
            case 30:
                // $script:1203181207004690$ 
                // - $MyPCName$?! What are you doing here? You  were a fool to come!  
                return true;
            default:
                return true;
        }
    }
}
