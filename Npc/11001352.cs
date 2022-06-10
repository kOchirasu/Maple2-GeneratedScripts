using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001352: Wei Hong
/// </summary>
public class _11001352 : NpcScript {
    internal _11001352(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005320$ 
                // - What brings you here?
                return true;
            case 30:
                // $script:1217012607005323$ 
                // - Heh. This place isn't as big a dump as I thought it'd be.
                return true;
            default:
                return true;
        }
    }
}
