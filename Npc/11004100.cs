using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004100: NPCNAME_11004100_NAME
/// </summary>
public class _11004100 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0705145607010403$
    // - SCRIPTNPCNAM_0705145607010403_NAME
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0705145607010406$
                // - SCRIPTNPCNAM_0705145607010406_NAME
                switch (selection) {
                    // $script:0705145607010407$
                    // - SCRIPTNPCNAM_0705145607010407_NAME
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0705145607010408$
                // - SCRIPTNPCNAM_0705145607010408_NAME
                switch (selection) {
                    // $script:0705145607010409$
                    // - SCRIPTNPCNAM_0705145607010409_NAME
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0705145607010410$
                // - SCRIPTNPCNAM_0705145607010410_NAME
                return 32;
            case (32, 1):
                // $script:0705145607010411$
                // - SCRIPTNPCNAM_0705145607010411_NAME
                switch (selection) {
                    // $script:0705145607010412$
                    // - SCRIPTNPCNAM_0705145607010412_NAME
                    case 0:
                        return 33;
                    // $script:0705145607010413$
                    // - SCRIPTNPCNAM_0705145607010413_NAME
                    case 1:
                        return 34;
                }
                return -1;
            case (33, 0):
                // $script:0705145607010414$
                // - SCRIPTNPCNAM_0705145607010414_NAME
                return 33;
            case (33, 1):
                // $script:0705145607010415$
                // - SCRIPTNPCNAM_0705145607010415_NAME
                return -1;
            case (34, 0):
                // $script:0705145607010416$
                // - SCRIPTNPCNAM_0705145607010416_NAME
                switch (selection) {
                    // $script:0705145607010417$
                    // - SCRIPTNPCNAM_0705145607010417_NAME
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:0705145607010418$
                // - SCRIPTNPCNAM_0705145607010418_NAME
                return 35;
            case (35, 1):
                // $script:0705145607010420$
                // - SCRIPTNPCNAM_0705145607010420_NAME
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.Close,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.Next,
            (35, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
