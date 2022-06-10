using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001569: Rejan
/// </summary>
public class _11001569 : NpcScript {
    internal _11001569(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0504151707006057$ 
                // - Hm... 
                return true;
            case 10:
                // $script:0515180307006112$ 
                // - Sob... 
                return true;
            default:
                return true;
        }
    }
}
