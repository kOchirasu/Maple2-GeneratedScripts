using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001712: Tinchai
/// </summary>
public class _11001712 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0728022507006964$
    // - Mm? Yes?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0728024507006998$
                // - The artifact must be hidden somewhere nearby. Or something related to it, at the very least.
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
