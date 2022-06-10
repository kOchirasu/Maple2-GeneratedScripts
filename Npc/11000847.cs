using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000847: Ozuma
/// </summary>
public class _11000847 : NpcScript {
    internal _11000847(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003099$ 
                // - What an interesting place. 
                return true;
            case 30:
                // $script:0831180407003102$ 
                // - I believe more than one timeline exists in Ludibrium at this moment. 
                return true;
            default:
                return true;
        }
    }
}
