using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000320: Lyn
/// </summary>
public class _11000320 : NpcScript {
    internal _11000320(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001250$ 
                // - What is it?
                return true;
            case 40:
                // $script:0831180407001254$ 
                // - Everyone thinks they're special, but the world keeps turning without them.
                switch (selection) {
                    // $script:0831180407001255$
                    // - What's wrong?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001256$ 
                // - Nothing. I just understand the way of the world.
                // $script:0831180407001257$ 
                // - Dust thou art, and to dust shalt thou return. Come empty, return empty. In the end, there's nothing in this world that is truly yours.
                return true;
            default:
                return true;
        }
    }
}
