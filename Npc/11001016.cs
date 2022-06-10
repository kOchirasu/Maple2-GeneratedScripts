using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001016: Kenken
/// </summary>
public class _11001016 : NpcScript {
    internal _11001016(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003463$ 
                // - This place belongs to me now! 
                return true;
            case 30:
                // $script:0831180407003466$ 
                // - Ahem, excuse me. Do you know how expensive these clothes I'm wearing are?  
                return true;
            default:
                return true;
        }
    }
}
