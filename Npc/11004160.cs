using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004160: Pemberton
/// </summary>
public class _11004160 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0730132107010545$
    // - I am dutybound to protect the young mistress.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0730132107010546$
                // - For the lady, I would sacrifice anything.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
