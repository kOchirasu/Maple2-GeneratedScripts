using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004105: NPCNAME_11004105_NAME
/// </summary>
public class _11004105 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0718090507010452$
    // - SCRIPTNPCNAM_0718090507010452_NAME
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0718090407010444$
                // - SCRIPTNPCNAM_0718090407010444_NAME
                switch (selection) {
                    // $script:0718090407010445$
                    // - SCRIPTNPCNAM_0718090407010445_NAME
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0718090407010446$
                // - SCRIPTNPCNAM_0718090407010446_NAME
                switch (selection) {
                    // $script:0718090407010447$
                    // - SCRIPTNPCNAM_0718090407010447_NAME
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0718090407010448$
                // - SCRIPTNPCNAM_0718090407010448_NAME
                return 32;
            case (32, 1):
                // $script:0718090407010449$
                // - SCRIPTNPCNAM_0718090407010449_NAME
                return 32;
            case (32, 2):
                // $script:0718090407010450$
                // - SCRIPTNPCNAM_0718090407010450_NAME
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Next,
            (32, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
