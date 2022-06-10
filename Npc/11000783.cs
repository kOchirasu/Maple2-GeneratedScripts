using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000783: Loront
/// </summary>
public class _11000783 : NpcScript {
    internal _11000783(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002952$ 
                // - Eh? What in the world is going on? 
                return true;
            case 30:
                // $script:0831180407002955$ 
                // - What if time never starts flowing again? 
                return true;
            default:
                return true;
        }
    }
}
