using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004145: Vanilla
/// </summary>
public class _11004145 : NpcScript {
    internal _11004145(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010561$ 
                // - Wait!
                return true;
            case 10:
                // $script:0806025707010562$ 
                // - An all-expenses paid trip to Mushtopia? Count me in!  I feel like dancing!
                return true;
            default:
                return true;
        }
    }
}
