using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003095: Oska
/// </summary>
public class _11003095 : NpcScript {
    internal _11003095(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0207122607007942$ 
                // - $MyPCName$, you came. 
                return true;
            case 10:
                // $script:0207122607007943$ 
                // - The Green Hood will always protect you. 
                return true;
            default:
                return true;
        }
    }
}
