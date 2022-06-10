using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000297: Quinny
/// </summary>
public class _11000297 : NpcScript {
    internal _11000297(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001181$ 
                // - How may I help you?
                return true;
            case 40:
                // $script:0831180407001184$ 
                // - I like $map:02000023$. All the trees and fairies are so pretty.
                return true;
            default:
                return true;
        }
    }
}
