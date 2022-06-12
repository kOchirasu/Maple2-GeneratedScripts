using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000531: Zorba
/// </summary>
public class _11000531 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407002284$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002287$
                // - Cough, cough... It's so dusty in here! I've had it with all these old books. 
                switch (selection) {
                    // $script:0831180407002288$
                    // - Are you really going to close your bookstore?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407002289$
                // - Well, I'm certainly thinking about it. Ha ha... My bookstore is the oldest business on $map:02000147$, you know. I'd rather keep it open, but I'm getting too old to run it on my own.
                return -1;
            case (40, 0):
                // $script:0831180407002290$
                // - Do you like books?
                switch (selection) {
                    // $script:0831180407002291$
                    // - Yep!
                    case 0:
                        return 41;
                    // $script:0831180407002292$
                    // - Nope!
                    case 1:
                        return 42;
                }
                return -1;
            case (41, 0):
                // $script:0831180407002293$
                // - Ha, do you? People like you amaze me. I've owned this store for over thirty years, but reading always puts me right to sleep. It's so boring.
                return 41;
            case (41, 1):
                // $script:0831180407002294$
                // - I'm glad not everyone feels like I do. I'd have long since shut down, ha!
                return -1;
            case (42, 0):
                // $script:0831180407002295$
                // - You don't? Ha, you're just like me. I've owned this store for over thirty years, but reading always puts me right to sleep. It's so boring. Just between you and me, I've never finished a single book in my whole life.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Next,
            (41, 1) => NpcTalkButton.Close,
            (42, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
