using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003068: Surnuny
/// </summary>
public class _11003068 : NpcScript {
    internal _11003068(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0102155907007655$ 
                // - Your Majesty...
                return true;
            case 30:
                // $script:0102155907007656$ 
                // - There are a great many things left to do. We should leave, for our next destination will be challenging.
                return true;
            default:
                return true;
        }
    }
}
