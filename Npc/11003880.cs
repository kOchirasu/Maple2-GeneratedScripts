using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003880: Gardener
/// </summary>
public class _11003880 : NpcScript {
    internal _11003880(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009876$ 
                // - Doesn't this flower look like me?
                return true;
            case 10:
                // $script:0417135107009877$ 
                // - Doesn't this flower look like me?
                return true;
            default:
                return true;
        }
    }
}
