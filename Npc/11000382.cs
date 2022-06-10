using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000382: Kant Getdaun
/// </summary>
public class _11000382 : NpcScript {
    internal _11000382(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001559$ 
                // - What's up?
                return true;
            case 20:
                // $script:0831180407001561$ 
                // - Hello. My name is $npcName:11000382[gender:0]$, and I'm a member of the Wall Climbers.  We're a group of free-climbing enthusiasts who support each other on our quest to surmount the greatest of heights. Anyone with a passion for climbing is welcome.
                return true;
            default:
                return true;
        }
    }
}
