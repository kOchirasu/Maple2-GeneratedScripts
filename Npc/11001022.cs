using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001022: Raymon
/// </summary>
public class _11001022 : NpcScript {
    internal _11001022(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003472$ 
                // - Wh-what? You again?! 
                return true;
            case 30:
                // $script:0831180407003475$ 
                // - Y-yes, I'm $npcName:11000526[gender:0]$. 
                return true;
            default:
                return true;
        }
    }
}
