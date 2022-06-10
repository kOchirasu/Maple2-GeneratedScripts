using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004110: Oska
/// </summary>
public class _11004110 : NpcScript {
    internal _11004110(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010461$ 
                // - I'm ready for anything.
                return true;
            case 10:
                // $script:0720125407010462$ 
                // - The Green Hoods are always ready.
                return true;
            default:
                return true;
        }
    }
}
