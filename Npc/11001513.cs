using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001513: Paulie
/// </summary>
public class _11001513 : NpcScript {
    internal _11001513(INpcScriptContext context) : base(context) {
        Id = 1;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0419105410001487$ 
                // - How may I help you look amazing? 
                return true;
            case 1:
                // $script:0420153110001493$ functionID=1 
                // - Looking for some head-turning hair? Then you came to the right place, $MyPCName$. My special hairstyles are unmatched! 
                switch (selection) {
                    // $script:0420153110001494$
                    // - I leave my special hairstyle to you, maestro.
                    case 0:
                        Id = 0;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
