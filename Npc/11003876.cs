using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003876: Loana
/// </summary>
public class _11003876 : NpcScript {
    internal _11003876(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0417135107009868$ 
                // - What's up?
                return true;
            case 10:
                // $script:0417135107009869$ 
                // - Did you need something?
                return true;
            default:
                return true;
        }
    }
}
