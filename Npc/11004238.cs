using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004238: Junta
/// </summary>
public class _11004238 : NpcScript {
    internal _11004238(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0809223207010932$ 
                // - Hmph.
                return true;
            case 10:
                // $script:0809223207010933$ 
                // - Hmph.
                // $script:0809223207010934$ 
                // - I'm sorry I wasn't of more help...
                return true;
            default:
                return true;
        }
    }
}
