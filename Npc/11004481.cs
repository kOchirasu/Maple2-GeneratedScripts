using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004481: Macrandra
/// </summary>
public class _11004481 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012212$
    // - Hm? I didn't expect to see anyone outside the safety of the outpost.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012213$
                // - Hm? I didn't expect to see anyone outside the safety of the outpost.
                switch (selection) {
                    // $script:1227192907012214$
                    // - What are you doing here?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012215$
                // - Oh, well I was sent out to look for aetherine samples, but I found this weird machine. I'm pretty sure it's related to aetherine somehow, but I haven't quite worked it out.
                return 11;
            case (11, 1):
                // $script:1227192907012216$
                // - It's weak, but that ring is drawing aetherine power into its center. I took some initial scans, and I think it's actually capable of storing vast amounts of the stuff.
                switch (selection) {
                    // $script:1227192907012217$
                    // - That's strange.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012218$
                // - Isn't it? But I have theories!
                return 12;
            case (12, 1):
                // $script:1227192907012219$
                // - Based on the data I've collected so far, I have two ideas. Either this device is gathering aetherine and transporting it somewhere...
                return 12;
            case (12, 2):
                // $script:1227192907012220$
                // - Or it's a dimensional portal that's connected to a place far, far away.
                return 12;
            case (12, 3):
                // $script:1227192907012221$
                // - What kind of people live here, that they can make all this wild technology?
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
            (12, 2) => NpcTalkButton.Next,
            (12, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
