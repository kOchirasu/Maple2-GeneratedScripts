using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004401: Marlene
/// </summary>
public class _11004401 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1213154907011982$
    // - Welcome.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1213154907011983$
                // - You have my full support.
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
