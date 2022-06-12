using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004492: Pantanal
/// </summary>
public class _11004492 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012337$
    // - Ah, $MyPCName$! I'm here researching the plants of Kritias.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012338$
                // - Ah, $MyPCName$! I'm here researching the plants of Kritias.
                switch (selection) {
                    // $script:1227192907012339$
                    // - What have you learned?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012340$
                // - So much! All of the plants in Kritias have at least a little bit of aetherine in them.
                return 11;
            case (11, 1):
                // $script:1227192907012341$
                // - And the plants react to each other's aetherine. It seems like they use the aetherine to communicate with each other!
                switch (selection) {
                    // $script:1227192907012342$
                    // - So what... talking plants?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012343$
                // - Not precisely, but the idea of plants being able to communicate with each other isn't exactly new. The ecosystem in Kritias may be the most concrete evidence we've ever seen.
                return 12;
            case (12, 1):
                // $script:1227192907012344$
                // - The plants are all giving off the same aetherine wavelength. It's almost as if they're singing a chorus!
                switch (selection) {
                    // $script:0114164007012721$
                    // - Incredible!
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:0114164007012722$
                // - Astonishing, too!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
