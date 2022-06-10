using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004562: Rolling Thunder
/// </summary>
public class _11004562 : NpcScript {
    internal _11004562(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014515$ 
                // - Hey! 
                return true;
            case 10:
                // $script:0220211107014516$ 
                // - Ha! I should've known you'd be here. Someone like you can't resist a good rumble. 
                switch (selection) {
                    // $script:0220211107014517$
                    // - You've got me there.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0220211107014518$ 
                // - That's the $MyPCName$ I remember! Hold on... This means we might have to fight each other. 
                // $script:0220211107014519$ 
                // - Well, well. Now I've got some real competition! Let's do our best, okay? 
                return true;
            default:
                return true;
        }
    }
}
