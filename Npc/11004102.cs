using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004102: NPCNAME_11004102_NAME
/// </summary>
public class _11004102 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0705145607010425$
    // - SCRIPTNPCNAM_0705145607010425_NAME
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0705145607010427$
                // - SCRIPTNPCNAM_0705145607010427_NAME
                return 30;
            case (30, 1):
                // $script:0705145607010428$
                // - SCRIPTNPCNAM_0705145607010428_NAME
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
