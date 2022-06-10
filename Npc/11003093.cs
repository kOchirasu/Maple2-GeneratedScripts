using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003093: Allon
/// </summary>
public class _11003093 : NpcScript {
    internal _11003093(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0207122607007938$ 
                // - The Lumiknights are always watching, $MyPCName$.
                return true;
            case 10:
                // $script:0207122607007939$ 
                // - I'll tell you more of the Lumiknights when the time is right.
                return true;
            default:
                return true;
        }
    }
}
