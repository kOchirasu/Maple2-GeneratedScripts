using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000607: Sudas
/// </summary>
public class _11000607 : NpcScript {
    internal _11000607(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002499$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407002502$ 
                // - Merchants like me and the palace workers are only allowed entry through the underground passageway. I wonder if I'll ever have the honor of passing through the main gates... 
                return true;
            default:
                return true;
        }
    }
}
