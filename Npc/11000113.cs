using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000113: Shogi
/// </summary>
public class _11000113 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000467$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000470$
                // - $MyPCName$, are you here to make a buck too?
                switch (selection) {
                    // $script:0831180407000471$
                    // - Why would I want to make money?
                    case 0:
                        return 31;
                    // $script:0831180407000472$
                    // - How can I make money here?
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000473$
                // - Oh, you didn't hear? The empress has called for an open court. If you want to get to the mainland to see it, you'll need a lot of money.
                return -1;
            case (32, 0):
                // $script:0831180407000474$
                // - Well, I usually check the boxes and jars laying around the village. You can find all kinds of cash or stuff to sell in 'em.
                return 32;
            case (32, 1):
                // $script:0831180407000475$
                // - If you want to make money quickly, you can always gather clams at $map:63000002$ over there. I've heard some of them hide expensive pearls and starfish.
                return 32;
            case (32, 2):
                // $script:0831180407000476$
                // - Be careful, though. Monsters are milling about the beach. I'd rather make money slowly than be beaten up by those things.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Next,
            (32, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
