using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000379: Seymour Vistas
/// </summary>
public class _11000379 : NpcScript {
    internal _11000379(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001550$ 
                // - What's up?
                return true;
            case 20:
                // $script:0831180407001552$ 
                // - Heya! I'm $npcName:11000379[gender:0]$, and I'm a member of the Wall Climbers. We're a group of free-climbing enthusiasts who support each other on our quest to surmount the greatest of heights. Anyone with a passion for climbing is welcome.
                return true;
            default:
                return true;
        }
    }
}
