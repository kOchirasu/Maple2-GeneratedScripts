using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000149: Collin
/// </summary>
public class _11000149 : NpcScript {
    internal _11000149(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000635$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407000637$ 
                // - Have you seen a puppy around here?
                switch (selection) {
                    // $script:0831180407000638$
                    // - Nope.
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407000639$ 
                // - Ahhh... Whitey, where are you? I should never have taken him outside. 
                return true;
            default:
                return true;
        }
    }
}
