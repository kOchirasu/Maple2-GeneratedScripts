using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001139: Lavoy
/// </summary>
public class _11001139 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0911192907003897$
    // - I'm selling these fine leather jackets.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0911192907003900$
                // - Hey, I've seen you hunting monsters around here before, haven't I?
                switch (selection) {
                    // $script:0911192907003901$
                    // - Yep!
                    case 0:
                        return 31;
                    // $script:0911192907003902$
                    // - Nope!
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0911192907003903$
                // - Haha! I could tell just by looking at you! A great adventurer, surely in need of Lavoy's fine leather goods!
                switch (selection) {
                    // $script:0911192907003904$
                    // - I'm not interested.
                    case 0:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0911192907003905$
                // - Don't be silly, I know a famous adventurer when I see one! A great adventurer deserves a great outfit. How many leather jackets can I put you down for?
                switch (selection) {
                    // $script:0911192907003906$
                    // - Sorry, not interested.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0911192907003907$
                // - Hahaha! You say that now, but you'll find no finer leatherwork around. Return to me once you've changed your mind.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
