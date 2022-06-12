using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004375: Snowleaf Fairfolk
/// </summary>
public class _11004375 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011787$
    // - Did you know? The fairfolk love sweet things. LOVE them.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011788$
                // - Did you know? The fairfolk love sweet things. LOVE them.
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
