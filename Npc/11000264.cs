using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000264: Ladin
/// </summary>
public class _11000264 : NpcScript {
    internal _11000264(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001077$ 
                // - Need something?
                return true;
            case 30:
                // $script:0831180407001080$ 
                // - After the Blue Lapenta broke, top scholars from across the world descended on the $map:02000026$. Ultimately, I am confident that it will be an alchemist to uncover the secrets of the Land of Darkness and the Shadow World.
                return true;
            case 40:
                // $script:0831180407001081$ 
                // - Can't you see I'm trying to focus?
                return true;
            default:
                return true;
        }
    }
}
