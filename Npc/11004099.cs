using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004099: NPCNAME_11004099_NAME
/// </summary>
public class _11004099 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0705145607010390$
    // - SCRIPTNPCNAM_0705145607010390_NAME
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0705145607010393$
                // - SCRIPTNPCNAM_0705145607010393_NAME
                switch (selection) {
                    // $script:0705154107010429$
                    // - SCRIPTNPCNAM_0705154107010429_NAME
                    case 0:
                        return 31;
                    // $script:0705154107010430$
                    // - SCRIPTNPCNAM_0705154107010430_NAME
                    case 1:
                        return 35;
                }
                return -1;
            case (31, 0):
                // $script:0705145607010397$
                // - SCRIPTNPCNAM_0705145607010397_NAME
                return 31;
            case (31, 1):
                // $script:0705145607010398$
                // - SCRIPTNPCNAM_0705145607010398_NAME
                return 31;
            case (31, 2):
                // $script:0705145607010399$
                // - SCRIPTNPCNAM_0705145607010399_NAME
                return -1;
            case (35, 0):
                // $script:0705145607010400$
                // - SCRIPTNPCNAM_0705145607010400_NAME
                switch (selection) {
                    // $script:0705145607010401$
                    // - SCRIPTNPCNAM_0705145607010401_NAME
                    case 0:
                        return 36;
                }
                return -1;
            case (36, 0):
                // $script:0705145607010402$
                // - SCRIPTNPCNAM_0705145607010402_NAME
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.Close,
            (35, 0) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
