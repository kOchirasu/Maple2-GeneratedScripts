using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000381: Fredo Haights
/// </summary>
public class _11000381 : NpcScript {
    internal _11000381(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001556$ 
                // - What's up?
                return true;
            case 20:
                // $script:0831180407001558$ 
                // - Hey there! My name is $npcName:11000381[gender:0]$, and I'm a member of the Wall Climbers. We're a group of free-climbing enthusiasts who support each other on our quest to surmount the greatest of heights. Anyone with a passion for climbing is welcome.
                return true;
            default:
                return true;
        }
    }
}
