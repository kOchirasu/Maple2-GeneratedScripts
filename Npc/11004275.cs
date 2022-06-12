using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004275: Numero
/// </summary>
public class _11004275 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011264$
    // - Ugh, this sucks. When can I get out of here?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011265$
                // - Ugh, this sucks. When can I get out of here?
                switch (selection) {
                    // $script:0911203207011266$
                    // - What's wrong?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:0911203207011267$
                // - Who are you, and why is that any of your business?
                switch (selection) {
                    // $script:0911203207011268$
                    // - C'mon. Just tell me what's bothering you.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:0911203207011269$
                // - If you must know, I'm upset because I'm trapped here. There's no way out, and...
                switch (selection) {
                    // $script:0913151207011304$
                    // - Maybe I can help you get free!
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0913151207011305$
                // - What? 
                return 13;
            case (13, 1):
                // $script:0911203207011270$
                // - Never mind. It's not worth explaining to you. Just move along.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Next,
            (13, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
