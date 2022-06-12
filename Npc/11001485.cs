using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001485: Araxis
/// </summary>
public class _11001485 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0106143407005788$
    // - So, how can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0106143407005791$
                // - So... what do you think about demons?
                switch (selection) {
                    // $script:0106143407005792$
                    // - They must be vanquished!
                    case 0:
                        return 40;
                    // $script:0106143407005793$
                    // - I hadn't really thought about them.
                    case 1:
                        return 50;
                }
                return -1;
            case (40, 0):
                // $script:0106143407005794$
                // - Indeed? That's what most people think about demons. I don't believe vanquishing them is the best solution. At the very least, we should learn more about their abilities first.
                switch (selection) {
                    // $script:0106143407005795$
                    // - What kinds of abilities do they have?
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0106143407005796$
                // - Oh, many kinds indeed. Most involve temptations used to trick mortals into doing their bidding. The problem is the way those abilities are used, not the demons themselves. There are ways to use demonic abilities for good.
                switch (selection) {
                    // $script:0106143407005797$
                    // - How can you do that?
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:0106143407005798$
                // - Well... I can't really say yet. There's so much left unexplained about demons. And even if I found ways to use their powers, I'm not sure I could use them without dire consequences.
                return -1;
            case (50, 0):
                // $script:0106143407005799$
                // - What a shame! I can tell by your aura that you're strong enough to handle demons. But if you're not interested, it hardly matters. Remember, there are always demons around us.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
