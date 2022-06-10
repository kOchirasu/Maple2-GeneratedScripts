using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001948: Mrs. O of Middleton
/// </summary>
public class _11001948 : NpcScript {
    internal _11001948(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007494$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:1208184307007542$ 
                // - My darling children are practically virtuosos. That's why I think it's time they learned how to play.
                return true;
            default:
                return true;
        }
    }
}
