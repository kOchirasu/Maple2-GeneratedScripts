using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000613: Louie
/// </summary>
public class _11000613 : NpcScript {
    internal _11000613(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002508$ 
                // - Huh? 
                return true;
            case 20:
                // $script:0831180407002510$ 
                // - No one knows what it's like to toil in this place. Only another captive could understand.  
                return true;
            default:
                return true;
        }
    }
}
