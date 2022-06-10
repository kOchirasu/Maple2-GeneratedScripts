using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001139: Lavoy
/// </summary>
public class _11001139 : NpcScript {
    internal _11001139(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911192907003897$ 
                // - I'm selling these fine leather jackets. 
                return true;
            case 30:
                // $script:0911192907003900$ 
                // - Hey, I've seen you hunting monsters around here before, haven't I? 
                switch (selection) {
                    // $script:0911192907003901$
                    // - Yep!
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0911192907003902$
                    // - Nope!
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0911192907003903$ 
                // - Haha! I could tell just by looking at you! A great adventurer, surely in need of Lavoy's fine leather goods! 
                switch (selection) {
                    // $script:0911192907003904$
                    // - I'm not interested.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0911192907003905$ 
                // - Don't be silly, I know a famous adventurer when I see one! A great adventurer deserves a great outfit. How many leather jackets can I put you down for? 
                switch (selection) {
                    // $script:0911192907003906$
                    // - Sorry, not interested.
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0911192907003907$ 
                // - Hahaha! You say that now, but you'll find no finer leatherwork around. Return to me once you've changed your mind. 
                return true;
            default:
                return true;
        }
    }
}
