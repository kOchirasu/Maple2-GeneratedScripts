using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003370: Kyle
/// </summary>
public class _11003370 : NpcScript {
    internal _11003370(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0516225807008487$ 
                // - Heheheh...
                return true;
            case 30:
                // $script:0516225807008489$ 
                // - Savor the moment.
                return true;
            default:
                return true;
        }
    }
}
