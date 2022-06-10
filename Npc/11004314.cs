using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004314: Schatten
/// </summary>
public class _11004314 : NpcScript {
    internal _11004314(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0928133807011354$ 
                // - I am the shadow that evil fears.
                return true;
            case 10:
                // $script:0928133807011355$ 
                // - My agents can't get past the insane AI that's controlling most of Kritias! I feel so... frustrated.
                return true;
            default:
                return true;
        }
    }
}
