using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004104: NPCNAME_11004104_NAME
/// </summary>
public class _11004104 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0718090507010451$
    // - SCRIPTNPCNAM_0718090507010451_NAME
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0718090407010434$
                // - SCRIPTNPCNAM_0718090407010434_NAME
                switch (selection) {
                    // $script:0718090407010435$
                    // - SCRIPTNPCNAM_0718090407010435_NAME
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0718090407010436$
                // - SCRIPTNPCNAM_0718090407010436_NAME
                switch (selection) {
                    // $script:0718090407010437$
                    // - SCRIPTNPCNAM_0718090407010437_NAME
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0718090407010438$
                // - SCRIPTNPCNAM_0718090407010438_NAME
                switch (selection) {
                    // $script:0718090407010439$
                    // - SCRIPTNPCNAM_0718090407010439_NAME
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0718090407010440$
                // - SCRIPTNPCNAM_0718090407010440_NAME
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
