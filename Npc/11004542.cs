using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004542: Keian
/// </summary>
public class _11004542 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0110183907012678$
    // - I can't believe my luck...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0110183907012679$
                // - I can't believe my luck...
                return 10;
            case (10, 1):
                // $script:0110183907012680$
                // - This place is <i>amazing</i>! Just this morning alone, I discovered three new molecules and a new kind of superconductor!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
