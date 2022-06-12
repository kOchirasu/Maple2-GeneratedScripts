using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004489: Leppens
/// </summary>
public class _11004489 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012303$
    // - Oh, hello. You must be here for my report. I'm afraid it's not very good...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012304$
                // - Oh, hello. You must be here for my report. I'm afraid it's not very good...
                switch (selection) {
                    // $script:1227192907012305$
                    // - Something wrong?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012306$
                // - I'm looking into the soil contamination that started spreading around here not too long ago.
                return 11;
            case (11, 1):
                // $script:1227192907012307$
                // - What do you know about the mechanical monster that roams this area?
                switch (selection) {
                    // $script:1227192907012308$
                    // - I know all about it!
                    case 0:
                        return 12;
                    // $script:1227192907012309$
                    // - Not a whole lot.
                    case 1:
                        return 13;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012313$
                // - Then you're aware of how big a problem Gigantica is for us.
                return 12;
            case (12, 1):
                // $script:1227192907012314$
                // - Wherever Gigantica appears, the soil becomes tainted. We've actually had to abandoned a camp because the toxins got so bad!
                return 12;
            case (12, 2):
                // $script:1227192907012315$
                // - That's why I'm needed. If I can analyze the contamination, we may be able to counteract it—or, at the very least, predict where Gigantica will go next.
                return -1;
            case (13, 0):
                // $script:1227192907012310$
                // - Really? You must not read the crew newsletter. Our efforts to explore Kritias have been hindered by this giant robotic worm. We call it Gigantica.
                return 13;
            case (13, 1):
                // $script:1227192907012311$
                // - Wherever Gigantica appears, the soil becomes tainted. We've actually had to abandon a camp because the toxins got so bad!
                return 13;
            case (13, 2):
                // $script:1227192907012312$
                // - That's why I'm needed. If I can analyze the contamination, we may be able to counteract it—or, at the very least, predict where Gigantica will go next.
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
            (12, 1) => NpcTalkButton.Next,
            (12, 2) => NpcTalkButton.Close,
            (13, 0) => NpcTalkButton.Next,
            (13, 1) => NpcTalkButton.Next,
            (13, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
