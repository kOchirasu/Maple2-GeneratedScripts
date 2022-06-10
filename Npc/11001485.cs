using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001485: Araxis
/// </summary>
public class _11001485 : NpcScript {
    internal _11001485(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0106143407005788$ 
                // - So, how can I help you?
                return true;
            case 30:
                // $script:0106143407005791$ 
                // - So... what do you think about demons?
                switch (selection) {
                    // $script:0106143407005792$
                    // - They must be vanquished!
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0106143407005793$
                    // - I hadn't really thought about them.
                    case 1:
                        Id = 50;
                        return false;
                }
                return true;
            case 40:
                // $script:0106143407005794$ 
                // - Indeed? That's what most people think about demons. I don't believe vanquishing them is the best solution. At the very least, we should learn more about their abilities first.
                switch (selection) {
                    // $script:0106143407005795$
                    // - What kinds of abilities do they have?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0106143407005796$ 
                // - Oh, many kinds indeed. Most involve temptations used to trick mortals into doing their bidding. The problem is the way those abilities are used, not the demons themselves. There are ways to use demonic abilities for good.
                switch (selection) {
                    // $script:0106143407005797$
                    // - How can you do that?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0106143407005798$ 
                // - Well... I can't really say yet. There's so much left unexplained about demons. And even if I found ways to use their powers, I'm not sure I could use them without dire consequences.
                return true;
            case 50:
                // $script:0106143407005799$ 
                // - What a shame! I can tell by your aura that you're strong enough to handle demons. But if you're not interested, it hardly matters. Remember, there are always demons around us.
                return true;
            default:
                return true;
        }
    }
}
