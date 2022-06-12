using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004272: Aesop
/// </summary>
public class _11004272 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011245$
    // - I've been duped! Everyone said this was the best vacation spot, but no one told me about the snakes!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011246$
                // - I've been duped! Everyone said this was the best vacation spot, but no one told me about the snakes!
                return 10;
            case (10, 1):
                // $script:0911203207011247$
                // - I knew I should've done more research. But things were so busy at work...
                switch (selection) {
                    // $script:0911203207011248$
                    // - Is this place really that popular?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011249$
                // - Oh, yeah, it's all the rage. Everyone talks about the treasure chests in the water, so I had to see them for myself. But... the snakes! Why are there so many snakes?
                switch (selection) {
                    // $script:0911203207011250$
                    // - Are they poisonous?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0911203207011251$
                // - Everyone says they're not, but I'm not so sure. I took out a second mortgage to afford this trip. I can't believe this is happening!
                return 12;
            case (12, 1):
                // $script:0911203207011252$
                // - Forget the treasure chests... I'll be happy to get out of here alive! My vacation is ruined!!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
