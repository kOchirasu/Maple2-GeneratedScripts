using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000630: Kibu
/// </summary>
public class _11000630 : NpcScript {
    internal _11000630(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002533$ 
                // - Screeeeech!
                return true;
            case 20:
                // $script:0831180407002535$ 
                // - Have you heard how some people coddle their children? It's ridiculous to me! You've got to toughen up your kids, so they can fend for themselves in any situation!
                return true;
            default:
                return true;
        }
    }
}
