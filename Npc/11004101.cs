using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004101: NPCNAME_11004101_NAME
/// </summary>
public class _11004101 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0705145607010421$
    // - SCRIPTNPCNAM_0705145607010421_NAME
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0705145607010423$
                // - SCRIPTNPCNAM_0705145607010423_NAME
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
